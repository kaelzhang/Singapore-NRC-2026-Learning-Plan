# Singapore NRC 2026 Learning Plan

This repository contains a 16-week student learning plan for Singapore NRC 2026 "Mission Meals".

The plan connects food-system science with robotics thinking so that students understand why the competition tasks matter before they build mechanisms and programs.

## Project Goals
- Build a 4-month learning path split into 16 weekly modules.
- Write the main weekly science material for students in English.
- Make technical terms visible and useful instead of hiding them.
- Explain difficult concepts with accurate terms and clear, concrete language.
- Connect each topic to the past, present, current global data, pain points, and future research directions.
- Include 5 to 6 non-repeated video links in every weekly module.
- Keep each week focused on one coherent domain.
- Include 1 to 2 system-framework weeks that connect all other weeks.

## Repository Structure
```text
.
|-- AGENTS.md
|-- README.md
|-- reference/
|   `-- deep-research.pdf
|-- W01/
|-- W02/
|-- ...
`-- W16/
```

Weekly directories are created as the curriculum is written. A typical weekly directory should contain:

- `README.md`: weekly student entrypoint, document links, learning order, and video shelf.
- `science.md`: student-facing science and food-system knowledge.
- `robotics.md`: student-facing robot building, mechanism, programming, mission-design, or testing work.
- `teacher-notes.md`: optional teacher-only notes.

The weekly `README.md` keeps the 5 to 6 direct student video links. The learning content is split between `science.md` and `robotics.md`.

## Project Documents
- `docs/README.md`: entrypoint for durable project documentation.
- `docs/curriculum-architecture.md`: 16-week curriculum structure, source baseline, and weekly design rules.

## Reference Basis
The starting reference is `reference/deep-research.pdf`, a deep-research report about Singapore NRC 2026 "Mission Meals" for integrated teacher and student learning.

The reference frames the theme through four teaching challenge areas:

- Food Production Infrastructure.
- Labour-Intensive Farming.
- Food Logistics.
- End-Effector Design.

The 16-week plan should extend that foundation with current web research, official sources, and student-ready explanations.

## Curriculum Direction
The curriculum treats Mission Meals as a combined system:

- A food system: farming, food security, cities, climate, logistics, waste, and future foods.
- A robot system: sensing, mechanisms, end-effectors, sequencing, testing, reliability, and explanation.

Students should repeatedly practice this translation:

```text
real-world food-system problem
-> competition mission idea
-> robot task
-> mechanism
-> program logic
-> test evidence
-> explanation
```

## Documentation Workflow
Use phased commits:

1. Create or update project entrypoints.
2. Create the 16-week curriculum architecture.
3. Fill weekly learning materials in batches.
4. Verify links, formatting, and consistency.

For documentation-only changes, run:

```bash
git diff --check
```

Then inspect `git status --short`, unstaged diffs, and staged diffs before committing.
