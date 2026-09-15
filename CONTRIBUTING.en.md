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

`Project | ★ | NVIDIA | One-liner | License`

- Link the official repo; use the current GitHub org / name.
- Stars column uses a shields badge: `[![Stars](https://img.shields.io/github/stars/ORG/REPO)](https://github.com/ORG/REPO)`.
- NVIDIA column is one of: `required` (official local path needs NVIDIA CUDA), `optional` (CPU / Apple Silicon / AMD also work), `no` (cloud API, CPU, or CPU rendering). Use `需要` / `可选` / `不需要` in Chinese. Use `—` for lists.
- After adding, re-sort that section's table by current star count (high → low).
- One-liner ≤ 40 characters / ~12 words. Say what it does; no marketing copy. Keep the Chinese and English blurbs aligned.
- License is SPDX (`Apache-2.0`, `MIT`, …). If the official license is `Other` or undeclared, write `见仓库` in Chinese and `see repo` in English.
- Do not invent a new section unless it is truly independent.

Then update the “Last checked” date at the top of both READMEs.
