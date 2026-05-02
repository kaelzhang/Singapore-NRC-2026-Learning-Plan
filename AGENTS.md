# AGENTS.md

## Purpose
This repository is a single-owner documentation workspace for a 16-week student learning plan for Singapore NRC 2026 "Mission Meals".

Agents use this file as the local entrypoint before reading or changing project documents.

## Source Authority
Follow sources in this order:

1. Current repository documents.
2. Organization standards under `/Users/kael/Codes/ost/standards`.
3. `reference/deep-research.pdf`.
4. Official NRC, Singapore government, LEGO Education, Scratch, FAO, UN, and other authoritative public sources.
5. High-quality educational or industry sources used only as supporting material.

## Required Reading
For normal work in this repository, read:

- `README.md`
- `reference/deep-research.pdf`
- Relevant weekly directory documents under `W01/` through `W16/`, when they exist.

For organization rules, follow the loading instructions in `/Users/kael/Codes/ost/standards/AGENTS.md`.

## Authorized Scope
This repository intentionally does not use a multi-agent inbox or subagent registry for this project.

The active agent may edit these paths:

- `AGENTS.md`
- `README.md`
- `reference/`
- `W01/` through `W16/`
- `docs/`
- other root-level project documentation files that support this learning plan

Do not create `tasks/`, inbox threads, or multi-agent coordination artifacts unless the user explicitly changes that decision.

## Documentation Rules
- Student-facing weekly learning materials must be written in English, except `keywords.md`, which may include Chinese explanations for review.
- Teacher-only notes may be written in Chinese or bilingual English/Chinese when that improves classroom use.
- Each week must live in its own directory named `W01`, `W02`, and so on through `W16`.
- Each weekly directory must separate science content from robotics work:
  - `science.md` for student-facing science and food-system knowledge.
  - `keywords.md` for the weekly core keyword index with Chinese explanations and concrete meanings.
  - `robotics.md` for robot building, mechanism, programming, mission-design, or testing work.
  - `README.md` for the weekly entrypoint, document links, and learning order.
  - `resources.md` for pure reference links, further-reading links, and video shelves.
- Keep `science.md` print-friendly: it should be readable as a continuous paper document. Inline links on meaningful keywords are allowed when they support the sentence, but do not add standalone reference-link, further-reading, resource-list, or video sections to `science.md`.
- Bold the weekly core keywords in `science.md` and keep the matching keyword explanations in `keywords.md`.
- Weekly content should stay cohesive around one main domain or question.
- Core terms should use accurate professional vocabulary, then explain the ideas in clear, concrete language.
- Each weekly directory should include 5 to 6 non-repeated student-watchable video links in `resources.md`.
- Prefer official, educational, museum, university, NGO, or well-maintained organization sources.
- Record pure source URL lists in `resources.md` instead of relying on chat history.

## Commit Discipline
Changes should be committed in phases:

1. Project entrypoints and agent instructions.
2. Curriculum architecture and 16-week overview.
3. Detailed weekly materials, committed in reviewable batches.
4. Cleanup, validation, and final documentation sync.

Before each documentation-only commit, run `git diff --check` and inspect staged changes.
Commit messages must follow the organization standard: `type(scope): imperative summary`.
Do not add tool, model, assistant, or co-author attribution trailers.
