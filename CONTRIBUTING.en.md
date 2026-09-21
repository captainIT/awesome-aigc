# How to contribute

**Language:** [中文](CONTRIBUTING.md) | English

This repo only lists **runnable open-source Git repositories**. It is not a paper index and not a closed-source product directory.

## Criteria

The more of these that apply, the better:

1. Runnable code or downloadable weights, not a landing page.
2. Directly related to video generation, audio generation, comic / story visualization, character consistency, or the tooling around those pipelines.
3. Clear license; commercial restrictions must be visible in the README.
4. Still maintained, or unmaintained but still the de facto standard in that niche.
5. Actually useful to this workspace's motion-comic, explainer-video, or voiceover pipelines.

Do not add:

- SaaS / app-store links with no source
- Pure mirrors, empty forks, or star farms
- Unverifiable “all-in-one miracle packs”

## How to submit

Add one row in the matching section, and **update both READMEs**:

`Project | ★ | NVIDIA | VRAM | One-liner | License`

- Link the official repo; use the current GitHub org / name.
- Stars column uses a shields badge: `[![Stars](https://img.shields.io/github/stars/ORG/REPO)](https://github.com/ORG/REPO)`.
- NVIDIA column is one of: `required` (official local path needs NVIDIA CUDA), `optional` (CPU / Apple Silicon / AMD also work), `no` (cloud API, CPU, or CPU rendering). Use `需要` / `可选` / `不需要` in Chinese. Use `—` for lists.
- VRAM is the minimum NVIDIA memory for this repo's official local inference path (including official offload / small variants), e.g. `8G` / `12G` / `16G` / `24G`. Use `—` when no NVIDIA GPU is required, and for lists. Chinese column name is `最低显存`.
- After adding, re-sort that section's table by current star count (high → low).
- One-liner ≤ 40 characters / ~12 words. Say what it does; no marketing copy. Keep the Chinese and English blurbs aligned.
- License is SPDX (`Apache-2.0`, `MIT`, …). If the official license is `Other` or undeclared, write `见仓库` in Chinese and `see repo` in English.
- Do not invent a new section unless it is truly independent.

Then update the “Last checked” date at the top of both READMEs.

## Auto-refresh

`scripts/update_catalog.py` calls the GitHub API to refresh listed repos, re-sort both READMEs by stars, and write high-star newcomers to `data/candidates.json` for human review. It does **not** add rows to the main tables unless you pass `--adopt`. Put repos you never want in `data/blocklist.txt`.

Existing one-liners, NVIDIA cells, and VRAM cells are not overwritten. Locally:

```bash
python3 scripts/update_catalog.py
```

GitHub Actions runs this every three days (or trigger it manually). Auto-added one-liners come from the GitHub description — edit them to say what the project actually does.
