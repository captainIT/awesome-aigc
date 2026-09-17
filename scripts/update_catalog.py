#!/usr/bin/env python3
"""从 GitHub 刷新 awesome-aigc 清单：核对数、按 star 重排、发现并择优收录相关仓库。"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README.en.md"
BLOCKLIST = ROOT / "data" / "blocklist.txt"
CANDIDATES = ROOT / "data" / "candidates.json"

CST = timezone(timedelta(hours=8))
USER_AGENT = "awesome-aigc-updater"
API = "https://api.github.com"
REPO_URL_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
DATE_ZH_RE = re.compile(r"最近核对：\d{4}-\d{2}-\d{2}")
DATE_EN_RE = re.compile(r"Last checked: \d{4}-\d{2}-\d{2}")

NVIDIA_ZH = {"required": "需要", "optional": "可选", "no": "不需要", "list": "—"}
NVIDIA_EN = {"required": "required", "optional": "optional", "no": "no", "list": "—"}
LICENSE_FALLBACK = {"zh": "见仓库", "en": "see repo"}
GLOBAL_REJECT = re.compile(
    r"\bawesome\b|awesome-|cheatsheet|tutorial|course|lecture|bootcamp|"
    r"transformers|unsloth|moneyprinter|open-generative-ai",
    re.I,
)

# 「本工作区已在用」不是 star 清单，脚本不改那张表
SKIP_REFRESH: set[str] = set()
SKIP_DISCOVER = {"lists"}


@dataclass(frozen=True)
class SectionSpec:
    key: str
    heading_zh: str
    heading_en: str
    min_auto: int
    min_candidate: int
    queries: tuple[str, ...]
    match: re.Pattern[str]
    reject: re.Pattern[str] | None = None
    nvidia_default: str = "required"


SECTIONS: tuple[SectionSpec, ...] = (
    SectionSpec(
        "video",
        "视频生成",
        "Video generation",
        4000,
        1500,
        (
            "text-to-video stars:>1500",
            "image-to-video stars:>1500",
            "topic:video-generation stars:>1500",
            "Wan2.2 OR Wan2.1 OR HunyuanVideo OR CogVideoX OR LTX-Video stars:>1500",
        ),
        re.compile(
            r"text-?to-?video|image-?to-?video|video[- ]generat|t2v|i2v|s2v|"
            r"open-?sora|wan2|hunyuanvideo|cogvideo|ltx-?video|animatediff|"
            r"mochi|helios|sora.?style",
            re.I,
        ),
        re.compile(r"\bawesome\b|tutorial|course|cheatsheet|awesome-", re.I),
    ),
    SectionSpec(
        "lowvram",
        "低显存与加速",
        "Low VRAM and acceleration",
        2500,
        800,
        (
            "Wan2GP OR ComfyUI-WanVideoWrapper OR LightX2V stars:>800",
            "low VRAM video generation stars:>800",
        ),
        re.compile(r"low.?vram|wan2gp|lightx2v|comfyui-.*(wan|ltx|hunyuan)|quantiz|distill", re.I),
        re.compile(r"\bawesome\b|tutorial", re.I),
    ),
    SectionSpec(
        "lipsync",
        "口型、数字人、动态人像",
        "Lip-sync, digital humans, animated portraits",
        2500,
        800,
        (
            "talking face OR lip sync OR liveportrait stars:>800",
            "topic:talking-head stars:>800",
        ),
        re.compile(r"lip.?sync|talking.?face|liveportrait|sadtalker|musetalk|latentsync|digital human|portrait", re.I),
        re.compile(r"\bawesome\b|text-to-video|image-to-video", re.I),
    ),
    SectionSpec(
        "tts",
        "语音合成 TTS",
        "Speech synthesis (TTS)",
        3000,
        1000,
        (
            "text-to-speech stars:>1000",
            "topic:text-to-speech stars:>1000",
            "voice cloning TTS stars:>1000",
        ),
        re.compile(r"\btts\b|text-to-speech|voice.?clon|speech synthes|sovits|chattts|cosyvoice|kokoro|fish-speech|index-tts|spark-tts|bert-vits|edge-tts", re.I),
        re.compile(r"\bawesome\b|whisper|speech-to-text|asr\b", re.I),
        "optional",
    ),
    SectionSpec(
        "music",
        "音乐与音效",
        "Music and sound effects",
        2500,
        800,
        (
            "text-to-music OR audiocraft OR ACE-Step stars:>800",
            "topic:music-generation stars:>800",
        ),
        re.compile(r"music|audiocraft|audio.?gen|stable.?audio|ace-step|sound.?effect|text-to-music", re.I),
        re.compile(r"\bawesome\b|text-to-speech|\btts\b", re.I),
        "optional",
    ),
    SectionSpec(
        "asr",
        "语音识别",
        "Speech recognition",
        8000,
        2000,
        ("speech recognition whisper stars:>2000", "topic:speech-recognition stars:>2000"),
        re.compile(r"whisper|funasr|faster-whisper|speech-to-text|speech.?recognition|\basr\b", re.I),
        re.compile(r"\bawesome\b|text-to-speech|\btts\b", re.I),
        "no",
    ),
    SectionSpec(
        "comic",
        "漫画与故事可视化",
        "Comics and story visualization",
        1500,
        400,
        (
            "comic generation OR storydiffusion OR manga translator stars:>400",
            "topic:comic-generation stars:>400",
        ),
        re.compile(r"comic|manga|story.?diffus|storyboard|motion.?comic|explainer|diffsensei", re.I),
        re.compile(r"\bawesome\b|text-to-video", re.I),
    ),
    SectionSpec(
        "image",
        "图像生成与角色一致性",
        "Image generation and character consistency",
        4000,
        1500,
        (
            "FLUX.1 OR InstantID OR PuLID OR IP-Adapter OR ControlNet stars:>1500",
            "character consistency image generation stars:>1500",
        ),
        re.compile(
            r"flux|controlnet|instantid|pulid|ip-adapter|qwen-image|hunyuan3d|dreamo|"
            r"character consist|identit|face.?id|subject.?driven",
            re.I,
        ),
        re.compile(r"\bawesome\b|webui|automatic1111|fooocus|invokeai|text-to-video", re.I),
    ),
    SectionSpec(
        "tooling",
        "工作流与工具链",
        "Workflows and tooling",
        8000,
        2500,
        (
            "ComfyUI stars:>2500",
            "diffusers OR remotion OR sd-scripts stars:>2500",
        ),
        re.compile(r"comfyui|diffusers|remotion|sd-scripts|webui-forge|lora", re.I),
        re.compile(r"\bawesome\b|wrapper|wanvideo|ltxvideo", re.I),
        "optional",
    ),
    SectionSpec(
        "lists",
        "相关清单",
        "Related lists",
        1500,
        400,
        ("awesome text-to-video OR awesome aigc stars:>400",),
        re.compile(r"awesome|curated list", re.I),
        None,
        "list",
    ),
)


@dataclass
class Row:
    repo: str
    nvidia: str
    blurb: str
    license: str | None
    raw: str
    stars: int = -1
    official: str = ""


@dataclass
class Table:
    spec: SectionSpec
    lang: str
    header: str
    sep: str
    rows: list[Row] = field(default_factory=list)
    has_license: bool = True


class GitHub:
    def __init__(self, token: str | None) -> None:
        self.token = token
        self._cache: dict[str, dict[str, Any] | None] = {}

    def _headers(self) -> dict[str, str]:
        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        url = API + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, headers=self._headers())
        for attempt in range(5):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                if exc.code in {403, 429} and attempt < 4:
                    wait = int(exc.headers.get("Retry-After") or (2 ** attempt) * 2)
                    time.sleep(wait)
                    continue
                if exc.code == 404:
                    return None
                detail = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"GitHub {exc.code} {path}: {detail[:300]}") from exc
            except TimeoutError as exc:
                if attempt < 4:
                    time.sleep(2 ** attempt)
                    continue
                raise RuntimeError(f"GitHub timeout {path}") from exc
        return None

    def repo(self, full_name: str) -> dict[str, Any] | None:
        key = full_name.lower()
        if key not in self._cache:
            time.sleep(0.15)
            self._cache[key] = self.get(f"/repos/{full_name}")
        return self._cache[key]

    def search(self, query: str, per_page: int = 12) -> list[dict[str, Any]]:
        time.sleep(2.0)
        data = self.get(
            "/search/repositories",
            {"q": query, "sort": "stars", "order": "desc", "per_page": per_page},
        )
        if not data:
            return []
        return list(data.get("items") or [])


def today() -> str:
    return datetime.now(CST).date().isoformat()


def resolve_token() -> str | None:
    for key in ("GITHUB_TOKEN", "GH_TOKEN"):
        value = os.environ.get(key)
        if value:
            return value
    for gh in ("gh", "/opt/homebrew/bin/gh", "/usr/local/bin/gh"):
        try:
            out = subprocess.check_output([gh, "auth", "token"], text=True, timeout=8)
            token = out.strip()
            if token:
                return token
        except (OSError, subprocess.SubprocessError):
            continue
    return None


def load_blocklist() -> set[str]:
    if not BLOCKLIST.exists():
        return set()
    names: set[str] = set()
    for line in BLOCKLIST.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip().lower()
        if line:
            names.add(line)
    return names


def clip(text: str, limit: int) -> str:
    text = re.sub(r"\s+", " ", (text or "").replace("|", "/")).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def parse_repo(cell: str) -> str | None:
    match = REPO_URL_RE.search(cell)
    if not match:
        return None
    return f"{match.group(1)}/{match.group(2)}"


def split_row(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [part.strip() for part in body.split("|")]


def is_sep(line: str) -> bool:
    return bool(re.match(r"^\s*\|?\s*:?-{3,}", line))


def parse_table(lines: list[str], spec: SectionSpec, lang: str) -> Table:
    header, sep, data = lines[0], lines[1], lines[2:]
    cols = split_row(header)
    has_license = any(c in {"许可", "License"} for c in cols)
    rows: list[Row] = []
    for line in data:
        cells = split_row(line)
        if len(cells) < 3:
            continue
        repo = parse_repo(cells[0])
        if not repo:
            continue
        nvidia = cells[2] if len(cells) > 2 else ""
        blurb = cells[3] if len(cells) > 3 else ""
        license_cell = cells[4] if has_license and len(cells) > 4 else None
        rows.append(
            Row(
                repo=repo,
                nvidia=nvidia,
                blurb=blurb,
                license=license_cell,
                raw=line,
            )
        )
    return Table(spec=spec, lang=lang, header=header, sep=sep, rows=rows, has_license=has_license)


def find_heading(text: str, heading: str) -> int:
    marker = f"## {heading}"
    idx = text.find(marker)
    if idx < 0:
        raise ValueError(f"找不到标题：{heading}")
    return idx


def next_heading(text: str, start: int) -> int:
    match = re.search(r"\n## ", text[start + 3 :])
    return start + 3 + match.start() if match else len(text)


def extract_table_block(section: str) -> tuple[int, int, list[str]] | None:
    lines = section.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if "★" in line and ("|" in line) and i + 1 < len(lines) and is_sep(lines[i + 1]):
            start = i
            break
    if start is None:
        return None
    end = start + 2
    while end < len(lines) and lines[end].lstrip().startswith("|"):
        end += 1
    return start, end, lines


def license_text(spdx: str | None, lang: str) -> str:
    if not spdx or spdx in {"NOASSERTION", "OTHER", "Other", "none"}:
        return LICENSE_FALLBACK[lang]
    return spdx


def infer_nvidia(repo: dict[str, Any], default: str) -> str:
    blob = " ".join(
        [
            repo.get("description") or "",
            " ".join(repo.get("topics") or []),
            repo.get("full_name") or "",
        ]
    ).lower()
    if default == "list":
        return "list"
    if any(k in blob for k in ("edge-tts", "remotion", "javascript", "typescript")) and "cuda" not in blob:
        return "no"
    if any(k in blob for k in ("apple silicon", "mps", "amd", "rocm", "cpu inference", "mlx")):
        return "optional"
    return default


def format_row(row: Row, table: Table) -> str:
    name = row.official or row.repo
    url = f"https://github.com/{name}"
    project = f"[{name}]({url})"
    badge = f"[![Stars](https://img.shields.io/github/stars/{name})]({url})"
    cells = [project, badge, row.nvidia, row.blurb]
    if table.has_license:
        cells.append(row.license or LICENSE_FALLBACK[table.lang])
    return "| " + " | ".join(cells) + " |"


def refresh_row(row: Row, meta: dict[str, Any] | None, lang: str) -> Row:
    if not meta:
        return row
    official = meta.get("full_name") or row.repo
    license_info = (meta.get("license") or {}).get("spdx_id")
    license_cell = row.license
    if row.license in {LICENSE_FALLBACK["zh"], LICENSE_FALLBACK["en"]}:
        license_cell = license_text(license_info, lang)
    return Row(
        repo=official,
        nvidia=row.nvidia,
        blurb=row.blurb,
        license=license_cell,
        raw=row.raw,
        stars=int(meta.get("stargazers_count") or 0),
        official=official,
    )


def listed_names(tables: list[Table]) -> set[str]:
    names: set[str] = set()
    for table in tables:
        for row in table.rows:
            names.add(row.repo.lower())
            if row.official:
                names.add(row.official.lower())
    return names


def discover(
    gh: GitHub,
    tables_zh: list[Table],
    blocklist: set[str],
    enable: bool,
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]]]:
    extras: dict[str, list[dict[str, Any]]] = {spec.key: [] for spec in SECTIONS}
    candidates: list[dict[str, Any]] = []
    if not enable:
        return extras, candidates

    known = listed_names(tables_zh)
    seen: set[str] = set(known)
    for spec in SECTIONS:
        if spec.key in SKIP_DISCOVER or not spec.queries:
            continue
        found: list[dict[str, Any]] = []
        for query in spec.queries:
            print(f"  搜索 [{spec.key}] {query}", flush=True)
            for item in gh.search(query):
                full = (item.get("full_name") or "").lower()
                if not full or full in seen or full in blocklist:
                    continue
                if item.get("fork") or item.get("archived"):
                    continue
                if not item.get("description"):
                    continue
                blob = f"{item.get('full_name', '')} {item.get('description', '')} {' '.join(item.get('topics') or [])}"
                if GLOBAL_REJECT.search(blob):
                    continue
                if spec.reject and spec.reject.search(blob):
                    continue
                if not spec.match.search(blob):
                    continue
                pushed = item.get("pushed_at") or item.get("updated_at") or ""
                stars = int(item.get("stargazers_count") or 0)
                fresh = True
                if pushed:
                    try:
                        pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
                        fresh = pushed_dt >= datetime.now(timezone.utc) - timedelta(days=540)
                    except ValueError:
                        fresh = True
                if not fresh and stars < 12000:
                    continue
                record = {
                    "repo": item.get("full_name"),
                    "stars": stars,
                    "section": spec.key,
                    "description": item.get("description") or "",
                    "url": item.get("html_url"),
                    "license": (item.get("license") or {}).get("spdx_id"),
                    "nvidia": infer_nvidia(item, spec.nvidia_default),
                }
                seen.add(full)
                if stars >= spec.min_auto:
                    found.append(record)
                elif stars >= spec.min_candidate:
                    candidates.append(record)
        found.sort(key=lambda r: r["stars"], reverse=True)
        extras[spec.key] = found[:2]
        for leftover in found[2:]:
            if leftover["stars"] >= spec.min_candidate:
                candidates.append(leftover)
    candidates.sort(key=lambda r: r["stars"], reverse=True)
    return extras, candidates


def add_discovered(table: Table, extras: list[dict[str, Any]]) -> int:
    existing = {row.repo.lower() for row in table.rows}
    added = 0
    lang = table.lang
    limit = 40 if lang == "zh" else 90
    for item in extras:
        name = item["repo"]
        if name.lower() in existing:
            continue
        nvidia = NVIDIA_ZH[item["nvidia"]] if lang == "zh" else NVIDIA_EN[item["nvidia"]]
        blurb = clip(item["description"], limit)
        license_cell = license_text(item.get("license"), lang) if table.has_license else None
        table.rows.append(
            Row(
                repo=name,
                nvidia=nvidia,
                blurb=blurb,
                license=license_cell,
                raw="",
                stars=item["stars"],
                official=name,
            )
        )
        existing.add(name.lower())
        added += 1
    return added


def render_table(table: Table) -> str:
    if table.spec.key not in SKIP_REFRESH:
        table.rows.sort(key=lambda r: (r.stars < 0, -r.stars if r.stars >= 0 else 0, r.repo.lower()))
    lines = [table.header.rstrip("\n"), table.sep.rstrip("\n")]
    for row in table.rows:
        if table.spec.key in SKIP_REFRESH:
            lines.append(row.raw.rstrip("\n"))
        else:
            lines.append(format_row(row, table))
    return "\n".join(lines) + "\n"


def replace_tables(text: str, tables: list[Table], lang: str) -> str:
    for table in tables:
        heading = table.spec.heading_zh if lang == "zh" else table.spec.heading_en
        start = find_heading(text, heading)
        end = next_heading(text, start)
        section = text[start:end]
        block = extract_table_block(section)
        if block is None:
            continue
        line_start, line_end, lines = block
        new_section = "".join(lines[:line_start]) + render_table(table) + "".join(lines[line_end:])
        text = text[:start] + new_section + text[end:]
    return text


def stamp_date(text: str, lang: str) -> str:
    day = today()
    if lang == "zh":
        return DATE_ZH_RE.sub(f"最近核对：{day}", text, count=1)
    return DATE_EN_RE.sub(f"Last checked: {day}", text, count=1)


def load_tables(text: str, lang: str) -> list[Table]:
    tables: list[Table] = []
    for spec in SECTIONS:
        heading = spec.heading_zh if lang == "zh" else spec.heading_en
        start = find_heading(text, heading)
        end = next_heading(text, start)
        block = extract_table_block(text[start:end])
        if block is None:
            raise ValueError(f"{heading} 下没有表格")
        line_start, line_end, lines = block
        table_lines = [ln.rstrip("\n") for ln in lines[line_start:line_end]]
        tables.append(parse_table(table_lines, spec, lang))
    return tables


def write_candidates(items: list[dict[str, Any]]) -> None:
    CANDIDATES.parent.mkdir(parents=True, exist_ok=True)
    payload = {"updated": today(), "items": items}
    CANDIDATES.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="刷新 awesome-aigc 的 GitHub 清单")
    parser.add_argument("--no-discover", action="store_true", help="只刷新已收录仓库，不搜索新仓")
    parser.add_argument(
        "--adopt",
        action="store_true",
        help="把达到门槛的新仓写入主表（默认只写入 data/candidates.json）",
    )
    parser.add_argument("--dry-run", action="store_true", help="只打印摘要，不写文件")
    args = parser.parse_args()

    token = resolve_token()
    if not token:
        print("警告：未找到 GITHUB_TOKEN / gh auth，GitHub API 限额很低。", file=sys.stderr)
    else:
        print("已拿到 GitHub token，开始刷新。", flush=True)

    gh = GitHub(token)
    blocklist = load_blocklist()
    zh_text = README_ZH.read_text(encoding="utf-8")
    en_text = README_EN.read_text(encoding="utf-8")
    tables_zh = load_tables(zh_text, "zh")
    tables_en = load_tables(en_text, "en")

    by_key_zh = {t.spec.key: t for t in tables_zh}
    by_key_en = {t.spec.key: t for t in tables_en}

    fetched = 0
    missing: list[str] = []
    metas: dict[str, dict[str, Any] | None] = {}
    for table in tables_zh:
        if table.spec.key in SKIP_REFRESH:
            continue
        for row in table.rows:
            key = row.repo.lower()
            if key not in metas:
                metas[key] = gh.repo(row.repo)
                fetched += 1
    for table in tables_zh + tables_en:
        if table.spec.key in SKIP_REFRESH:
            continue
        for row in table.rows:
            meta = metas.get(row.repo.lower())
            if meta is None:
                missing.append(row.repo)
                continue
            refreshed = refresh_row(row, meta, table.lang)
            row.repo = refreshed.repo
            row.nvidia = refreshed.nvidia
            row.blurb = refreshed.blurb
            row.license = refreshed.license
            row.stars = refreshed.stars
            row.official = refreshed.official

    print("已收录仓库元数据拉取完成，开始搜索新仓。", flush=True)
    extras, candidates = discover(gh, tables_zh, blocklist, enable=not args.no_discover)
    added = 0
    if args.adopt:
        for key, items in extras.items():
            if not items:
                continue
            added += add_discovered(by_key_zh[key], items)
            add_discovered(by_key_en[key], items)
        extras_for_log = extras
    else:
        for key, items in extras.items():
            candidates.extend(items)
        extras_for_log = extras if args.adopt else {}
        candidates.sort(key=lambda r: r["stars"], reverse=True)

    new_zh = stamp_date(replace_tables(zh_text, tables_zh, "zh"), "zh")
    new_en = stamp_date(replace_tables(en_text, tables_en, "en"), "en")

    print(f"已查询仓库：{fetched}")
    print(f"自动新收录：{added}")
    print(f"候选（未写入主表）：{len(candidates)}")
    if missing:
        print("未取到元数据：", ", ".join(sorted(set(missing))))
    if extras_for_log:
        for key, items in extras_for_log.items():
            if items:
                print(f"  + {key}: " + ", ".join(f"{i['repo']}({i['stars']})" for i in items))

    if args.dry_run:
        return 0

    README_ZH.write_text(new_zh, encoding="utf-8")
    README_EN.write_text(new_en, encoding="utf-8")
    if not args.no_discover:
        write_candidates(candidates)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
