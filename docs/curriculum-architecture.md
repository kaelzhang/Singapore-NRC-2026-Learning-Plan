# Singapore NRC 2026 Mission Meals Curriculum Architecture

## Purpose
This document defines the 16-week structure for a four-month student learning plan for Singapore NRC 2026 "Mission Meals".

The weekly student materials should be readable by students directly. Teacher notes can add classroom pacing, extension choices, and competition alignment, but the main weekly learning path must not depend on teacher-only explanation.

## Source Baseline
The curriculum starts from `reference/deep-research.pdf` and extends it with current authoritative sources checked on 2026-05-02:

- Science Centre Singapore confirms NRC 2026, the regular category hardware groups, autonomous field challenges, and the challenge document entrypoint.
- The official Science Centre Singapore NRC page provides the competition entrypoint, while the food-system learning frame connects the theme to global food security and SDG 2.
- Singapore's Food Story 2 now frames local food resilience through import diversification, growing local, stockpiling, and global partnerships.
- Singapore's revised 2035 local production targets focus on 20% of local fibre consumption and 30% of local protein consumption from local farms.
- SOFI 2025 estimates that about 673 million people experienced hunger in 2024, while 2.3 billion people experienced moderate or severe food insecurity.
- UNEP's Food Waste Index Report 2024 estimates 1.05 billion tonnes of food waste in 2022, about 19% of food available to consumers.
- FAO and WMO's 2026 extreme heat assessment warns that extreme heat is now a major risk multiplier for crops, livestock, fisheries, aquaculture, forests, and agricultural workers.

## Curriculum Design Principles
1. Use accurate professional vocabulary, then explain it in clear, concrete language.
2. Keep each week focused on one main domain so students can build a coherent mental model.
3. Include past, present, and future in every week.
4. Connect food-system knowledge to robot-system thinking every week.
5. Use one early framework week and one late framework week to connect the whole course.
6. Give students 5 to 6 non-repeated video links per week in `resources.md`.
7. Prefer official, educational, university, museum, NGO, or maintained industry sources.
8. Treat technologies as tradeoffs, not magic solutions.

## Student Learning Loop
Each week should use the same mental loop:

```text
What problem are people trying to solve?
What science helps us understand it?
What changed from the past to today?
What data shows why it matters now?
What future challenge or research direction is still open?
How could a robot sense, move, decide, or handle objects in this part of the system?
```

## File Pattern
Each weekly directory should contain:

- `README.md`: weekly student entrypoint with document links and suggested learning order.
- `science.md`: printable student-facing science and food-system lesson in English.
- `science-brief.md`: condensed student-facing science review in English, normally 30% to 50% of `science.md`, rewritten by meaning rather than paragraph-by-paragraph compression.
- `science-brief-cn.md`: Chinese translation of `science-brief.md` for bilingual review, using natural Chinese and required project terminology.
- `keywords.md`: weekly bilingual core keyword index with English and Chinese keywords, specific meanings, simple explanations, and examples.
- `robotics.md`: student-facing robot building, mechanism, programming, mission-design, or testing work in English.
- `teacher-notes.md`: teacher-facing notes, allowed to be Chinese or bilingual.
- `resources.md`: pure reference links, further reading, and video shelf.

The student-facing `science.md` should include:

- Big question.
- Why this matters for Mission Meals.
- Past, present, and future.
- Deep explanation.
- Core terminology.
- Student thinking tasks.

`science.md` should not contain standalone reference-link, further-reading, resource-list, or video sections. It may keep inline links on meaningful keywords inside explanatory prose, but pure links and link-focused bullet lists belong in `resources.md` so `science.md` remains printable.
`science-brief.md` should stay print-friendly and easy to read directly. It should keep the highest-value concepts, examples, past-present-future frame, and Mission Meals links from `science.md`, but use shorter wording and avoid rare vocabulary unless the term is a learning target.
`science-brief-cn.md` should follow the structure and meaning of `science-brief.md`, not introduce new source sections, and must translate `Food Security` as `食品保障` while reserving `食品安全` for `Food Safety`.
Core keywords should be bolded in `science.md`. The same keyword set should appear in `keywords.md` as bilingual English/Chinese content with the current keyword list, the meaning of each keyword, a simple explanation, and an example. Keyword index cells should use bilingual table headings and line breaks instead of repeated column labels. Translate `Food Security` as `食品保障`; reserve `食品安全` for `Food Safety`.

The student-facing `robotics.md` should include:

- Robot connection.
- Build, programming, mechanism, mission-design, or testing tasks.
- Engineering notebook prompt.

The weekly `README.md` should include:

- Links to `science.md`, `science-brief.md`, `science-brief-cn.md`, `keywords.md`, `robotics.md`, `teacher-notes.md`, and `resources.md`.
- Weekly question.
- Suggested learning order.

The weekly `resources.md` should include:

- core science reference links,
- sources for further reading,
- 5 to 6 non-repeated video links.

## The 16-Week Sequence
| Week | Directory | Main focus | Role in the course | Key NRC translation |
| --- | --- | --- | --- | --- |
| 1 | `W01` | Mission Meals and the whole food system | Framework week 1 | Translate theme language into food-system and robot-system maps. |
| 2 | `W02` | Singapore's Food Story and urban food resilience | Local context | Connect import dependence, local production, stockpiling, and partnerships to competition missions. |
| 3 | `W03` | Agriculture from domestication to the Green Revolution | Historical foundation | See farming as a sequence of tools for controlling water, energy, labour, time, and information. |
| 4 | `W04` | Food security today: hunger, nutrition, affordability, and productivity | Global data | Connect SDG 2 data to why production alone is not enough. |
| 5 | `W05` | Plant growth science: photosynthesis, light, water, soil, and nutrients | Biology foundation | Understand what a production-infrastructure robot is helping plants control. |
| 6 | `W06` | Controlled environment agriculture, hydroponics, and vertical farms | Urban farming technology | Connect greenhouses and plant factories to sensors, lights, pumps, and resource tradeoffs. |
| 7 | `W07` | Precision agriculture, sensors, remote sensing, drones, and data | Information layer | Translate "look carefully before acting" into color sensing, mapping, and state decisions. |
| 8 | `W08` | Labour-intensive farming and agricultural robots | Automation layer | Connect harvesting, weeding, sorting, and repetitive labour to robot mechanisms. |
| 9 | `W09` | End-effectors, grippers, levers, gears, and modular tools | Robot mechanism focus | Design tools that push, lift, sweep, hook, clamp, and release food-system objects. |
| 10 | `W10` | Food logistics, cold chain, warehouses, and traceability | Movement and safety layer | Translate storage, routing, docking, and delivery into robot paths and load handling. |
| 11 | `W11` | Food loss, food waste, circular economy, and recovery | Waste and reuse | Connect sorting, rescue, composting, and reuse to mission choices. |
| 12 | `W12` | Climate risk, extreme heat, water stress, and resilient agriculture | Risk layer | Ask how food systems keep working when weather becomes a constraint. |
| 13 | `W13` | Future foods: alternative proteins, fermentation, cultured meat, insects, and algae | Future production | Compare new food sources by safety, energy, land, cost, and acceptance. |
| 14 | `W14` | Computational thinking with Scratch and SPIKE Essential | Robot logic foundation | Use sequence, loops, conditions, variables, and states to make autonomous decisions. |
| 15 | `W15` | Testing, reliability, debugging, and evidence | Engineering discipline | Build 5-run and 10-run evidence instead of trusting one lucky run. |
| 16 | `W16` | From food system to robot system: capstone synthesis and future scenarios | Framework week 2 | Explain the final robot as a food-system solution backed by evidence. |

## Weekly Depth Targets
Each week should explain about 5 to 8 core terms. Terms should be chosen because students will need them to think clearly, not because they sound advanced.

Examples:

- Week 1: food system, food security, availability, access, utilization, stability, mission abstraction.
- Week 5: photosynthesis, chlorophyll, spectrum, photon, hydroponics, nutrient solution, transpiration.
- Week 9: end-effector, actuator, lever, gear ratio, degrees of freedom, compliance, modular interface.
- Week 15: reliability, variable, control test, failure mode, root cause, iteration, evidence.

## Pacing
Assume one 90 to 120 minute session per week:

1. 10 minutes: question and recap.
2. 30 to 40 minutes: student reading and discussion.
3. 20 to 30 minutes: small paper, Scratch, or LEGO-linked activity.
4. 15 minutes: terminology check.
5. 10 to 20 minutes: video selection, reflection, and notebook entry.

Students do not need to watch all videos during class. The weekly videos are a curated viewing shelf in `resources.md` for classroom use, home viewing, and extension.

## Video Policy
Weekly video links must not repeat across the 16 directories. Prefer videos from:

- Science Centre Singapore, SFA, MSE, or Singapore public education sources.
- FAO, WFP, UNEP, UN, NASA, USDA, or other public agencies.
- LEGO Education, Scratch Foundation, and reputable robotics education channels.
- Maintained industry channels only when they show a concrete technology students need to understand.

Avoid:

- unsupported hype videos,
- videos where the title promises certainty that current science does not support,
- videos that depend on fear, politics, or adult controversy rather than student learning,
- videos that are too long for young students unless they are teacher-selected segments.

## Assessment Artifacts
By the end of the 16 weeks, each student team should have:

- a food-system concept map,
- a Singapore food-resilience case note,
- a past-to-future agriculture timeline,
- a technical glossary notebook,
- at least one production, logistics, or waste mission abstraction,
- an end-effector sketch library,
- a Scratch or SPIKE logic map,
- a 10-run reliability table,
- a capstone explanation connecting problem, robot, evidence, and future improvement.

## Research Notes To Preserve
The detailed NRC challenge documents are linked from the official Science Centre page and may change or receive FAQ updates. Before final competition practice, teachers should re-check the official challenge documents, FAQ, field setup, prop list, and scoring details.

For this repository, the curriculum should avoid hard-coding final scoring claims unless they are copied from the latest official challenge document during a dedicated rules-check pass.

## Source Links
- Science Centre Singapore NRC page: https://www.science.edu.sg/for-schools/competitions/national-robotics-competition
- UN Sustainable Development Goal 2: https://sdgs.un.org/goals/goal2
- MSE revised production targets reply: https://www.mse.gov.sg/latest-news/oral-reply-to-parliamentary-question-on-revised-local-production-targets/
- SG101 Singapore's Food Challenge: https://www.sg101.gov.sg/economy/case-studies/sg-food-challenge/
- FAO SOFI page: https://www.fao.org/publications/fao-flagship-publications/the-state-of-food-security-and-nutrition-in-the-world/2024/en
- WFP SOFI 2025 release: https://www.wfp.org/news/global-hunger-declines-rises-africa-and-western-asia-un-report
- UNEP Food Waste Index Report 2024: https://www.unep.org/resources/publication/food-waste-index-report-2024
- WMO FAO extreme heat agriculture release: https://wmo.int/news/media-centre/extreme-heat-pushes-agrifood-systems-brink
- LEGO Education SPIKE Essential: https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/
- Scratch Learning Library: https://www.scratchfoundation.org/learn/learning-library
