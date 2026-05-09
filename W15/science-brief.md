# W15 Science Brief - Testing, Reliability, Debugging, And Evidence

This brief keeps the main ideas from `science.md` for shorter review.

## Big Idea
A robot that works once may be lucky. A robot that works many times with records has **evidence**. Testing shows whether a design is dependable, not only exciting.

Food systems need the same habit. A cold chain cannot work only once. A warehouse cannot sort correctly only on perfect days. A farm sensor cannot be trusted only when the room is quiet.

## Past, Present, And Future
In the past, farmers, builders, sailors, and toolmakers learned by trial, error, memory, and records. Better records helped people see which seeds, tools, storage methods, or routes worked best.

Today, engineers use test plans, variables, controls, failure analysis, checklists, version records, simulations, safety reviews, and reliability statistics. Robotics teams use run logs, battery checks, alignment marks, sensor calibration, slow-motion video, and program versions.

In the future, robots and food systems may use automatic logs, digital twins, real-time sensors, predictive maintenance, and AI inspection. Humans will still need to decide what counts as success and what evidence is trustworthy.

## Test Questions And Success Criteria
A good test starts with a clear question.

Weak: "Let's see what happens."

Stronger: "At speed 40, can the robot deliver the crate to the target zone five times in a row?"

**Success criteria** are the rules for passing. A delivery mission might require the object to reach the target fully, no other model to be knocked over, the time to be under 20 seconds, release to be clean, and reset to be safe.

Clear criteria stop arguments and make data useful.

## Variables And Controls
A **variable** is something that can change, such as speed, attachment angle, start position, battery level, object position, or sensor threshold.

A **control** is something kept the same during a test. If you change speed, wheel size, tool angle, and start position all at once, you will not know which change caused the result.

Good testing changes one main variable at a time and records the result.

## Failure Modes And Root Cause
A **failure mode** is a specific way something fails: wheel slip, missed line, early gripper release, object jam, wrong colour reading, low battery, loose tool, dragging release, or inconsistent start position.

A **root cause** is the deeper reason behind the failure. The symptom may be "robot missed target." The root cause might be wheel slip, too-fast turning, attachment wobble, low battery, or a start-position error.

Debugging tries to fix the root cause, not only hide the symptom.

## Reliability Needs Repetition
**Reliability** means the system works repeatedly. A 5-run test is a useful first check. A 10-run test is stronger. More runs are stronger when time allows.

Record each run with setup, result, time, failure mode, and change made. A robot that succeeds 9 out of 10 times is very different from one that succeeds 3 out of 10 times.

Consistency matters. One very fast lucky run is weaker than a slightly slower design that succeeds again and again.

## Hidden Variables
Teams often forget hidden variables. Battery level changes motor strength. Dust changes wheel grip. Starting angle changes the route. Loose parts change tool timing. Lighting changes sensor readings. A fast reset may place an attachment slightly wrong.

A good test plan controls these or stress-tests them on purpose.

## Debugging Loop
Use this loop:

```text
observe -> name failure -> form hypothesis -> change one thing -> test -> record
```

A **hypothesis** is a testable guess. Example: "The crate stops short because wheel slip happens during fast acceleration." Then change speed and test.

## Evidence-Based Claims
Weak claim: "Our robot is reliable."

Stronger claim: "Our robot delivered the cold box successfully in 9 out of 10 runs using the same start mark and battery range."

Strongest claim: "Our robot delivered the cold box successfully in 9 out of 10 runs. The failed run happened when the box started 1 cm forward, so our next improvement is a wider guide."

Evidence makes claims honest.

## Version Control And Stop Rules
**Version** control means knowing what changed: Gripper V1, Gripper V2, Program V3. Take photos, save programs, and write short notes.

A **stop rule** tells the team when to stop changing a design for now. For example: if a mission succeeds 8 out of 10 times for two practice sessions, stop changing it and work on the next problem. Without stop rules, teams may break a working design by endless tweaking.

## Stress Testing And Regression
**Stress testing** means testing under harder conditions: object shifted 1 cm, lower battery, different lighting, faster reset, slightly different start angle, or a small obstacle.

**Regression** means a new change breaks something that used to work. If a heavier attachment improves pickup but ruins turning, retest old missions.

Food systems do similar tests: freezer power loss, blocked routes, late donations, or packaging changes.

## Mission Meals Connections
If a project claims cold-chain reliability, test delivery time and correct destination. If it claims waste reduction, test sorting accuracy. If it claims fragile-food handling, test drops and release. If it claims climate resilience, test the backup route.

Evidence should match the claim.

## Extra Details To Remember
Evidence can be qualitative or quantitative. Qualitative evidence uses words, photos, or video, such as "the left wheel slipped during the turn." Quantitative evidence uses numbers, such as "8 out of 10 runs succeeded" or "average time was 18 seconds." Strong notebooks use both.

Average and spread both matter. If run times are 20, 21, 20, 21, and 20 seconds, the robot is predictable. If times are 10, 35, 18, 40, and 12 seconds, the average may look okay, but the spread is large and strategy becomes risky.

Checklists reduce human error. A pre-run checklist can include battery, correct program, locked attachment, start alignment, object reset, clear wires, and team roles. Professionals use checklists because people forget things under pressure.

Graphs should answer a question, not decorate a notebook. A useful graph might show that slower approach improved success from 5/10 to 9/10. Then explain it with claim, evidence, and reasoning.

## Key Takeaways
Testing turns ideas into trustworthy claims. A good engineering notebook includes questions, criteria, variables, controls, run records, failure modes, versions, and next improvements.

Final check: choose one robot mission. Write a test question, success criteria, one hidden variable, and one evidence-based claim using a 10-run result.
