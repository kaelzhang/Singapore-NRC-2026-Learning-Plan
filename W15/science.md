# W15 Science - Testing, Reliability, Debugging, And Evidence

This student document contains the science and food-system knowledge for the week. For robot building and programming work, see `robotics.md`.

## Big Question
How do we know a robot works, instead of just getting lucky once?

## Why This Week Matters
In robotics competitions, one successful run is not enough. A team needs evidence that the robot can repeat the task under realistic conditions. This week teaches the engineering discipline behind reliability.

Food systems also need reliability. A cold chain cannot work only once. A warehouse cannot sort correctly only once. A farm sensor cannot be trusted only on perfect days. Testing is the bridge between a good idea and a dependable system.

## Key Reference Links For This Week
Use these links for reliable background:

- [NASA eClips Engineering Design Packets](https://science.nasa.gov/science-research/earth-science/engineering-design-packets/) - student engineering design process materials.
- [NASA Software, Robotics, and Simulation Division](https://www.nasa.gov/software-robotics-and-simulation-division/) - real robotics reliability and testing context.
- [Scratch Getting Started](https://www.scratchfoundation.org/learn/learning-library/getting-started) - debugging and iteration in creative coding.
- [Scratch Learning Library](https://www.scratchfoundation.org/learn/learning-library) - official learning resources.
- [LEGO Education SPIKE Essential](https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/) - student robotics platform context.
- [Science Centre Singapore NRC](https://www.science.edu.sg/for-schools/competitions/national-robotics-competition) - competition context.

## The One-Minute Idea
Testing means trying a system in a planned way. Reliability means it works repeatedly. Debugging means finding and fixing the cause of failure. Evidence means records that show what happened.

If your robot works once, say "interesting." If it works 10 times with records, say "we have evidence."

## Past, Present, Future

### Past
Engineers have always tested bridges, machines, ships, tools, and food systems because real systems can fail. Trial and error became stronger when people learned to record results and change one thing at a time.

Farmers also tested ideas over seasons: different seeds, planting dates, irrigation methods, tools, storage methods, and preservation techniques. Good records helped people learn.

### Present
Modern engineering uses test plans, control variables, failure analysis, checklists, version records, reliability statistics, simulations, and safety reviews. Robotics teams use run logs, battery checks, alignment marks, sensor calibration, and slow-motion videos.

Food systems use lab tests, temperature logs, recall records, inspection checklists, shelf-life studies, and traceability records.

### Future
Future robots may test themselves with built-in sensors, simulation, digital twins, automatic logs, and predictive maintenance. Food systems may use real-time temperature sensors, AI inspection, and automated alerts.

But humans will still need to decide what matters, what failure means, what evidence is trustworthy, and when a design is good enough.

## Deep Explanation

### 1. A Test Must Have A Question
Bad test: "Let's see what happens."

Better test: "At speed 40, can the robot deliver the crate to the target zone 5 times in a row?"

A test question tells you what to measure. Without a question, you may watch the robot without learning much.

### 2. Success Criteria Define What Counts
Success criteria are rules for deciding whether a test passed. For a delivery mission, success might mean:

- object starts in correct place,
- robot starts from marked base,
- object reaches target zone fully,
- no other models are knocked over,
- time is under 20 seconds,
- release is clean,
- robot can be reset safely.

If criteria are unclear, teams may argue about whether a run was good. Clear criteria make evidence stronger.

### 3. Change One Variable At A Time
If you change speed, wheel size, tool angle, and start position all at once, you will not know what caused the result. A variable is something that can change. Good testing changes one main variable and keeps the rest controlled.

A control is something kept the same. For example, keep the same battery level, start position, mat location, program version, and object position while testing motor speed.

### 4. Failure Modes Have Names
A failure mode is a specific way something fails:

- robot misses line,
- wheel slips,
- gripper opens early,
- object jams,
- sensor reads wrong colour,
- battery low,
- start position inconsistent,
- tool bends,
- release drags object,
- route hits another model.

Naming failure modes helps you fix causes, not symptoms.

### 5. Root Cause Is Deeper Than Symptom
A symptom is what you see. A root cause is the deeper reason.

Symptom: the robot misses the target.

Possible root causes: start position changes, wheel slip, turn angle too large, attachment pushes robot sideways, battery level changed, mat is wrinkled, or the program uses time instead of motor rotation.

Debugging tries to find the root cause. Fixing symptoms may hide the problem for one run but not solve it.

### 6. Reliability Needs Repetition
A 5-run test is a useful first check. A 10-run test is stronger. A 20-run test is stronger still, but may take more time.

Record each run:

```text
run number, setup, result, time, failure mode, change made
```

A robot that succeeds 9 out of 10 times is different from a robot that succeeds 3 out of 10 times. The average time also matters, but consistency matters more than one fast lucky run.

### 7. Battery, Start Position, And Reset Are Variables
Robotics teams often forget hidden variables.

Battery level changes motor performance. Start position changes route accuracy. Reset quality changes attachment position. Mat bumps change wheel movement. Loose parts change mechanism timing.

A good test plan controls these or tests them deliberately. For example, test at full battery and lower battery. Test with the object slightly shifted. Test after a quick reset.

### 8. Debugging Is A Loop
Debugging is not random guessing. Use this loop:

```text
observe -> name failure -> form hypothesis -> change one thing -> test -> record
```

Example:

```text
observe: crate stops short
failure: under-delivery
hypothesis: wheel slip during acceleration
change: lower acceleration and speed
result: 8/10 successful instead of 4/10
```

### 9. Evidence-Based Claims Are Stronger
Weak claim: our robot is reliable.

Stronger claim: our robot delivered the cold box successfully in 9 out of 10 test runs using the same start position and battery range.

Strongest claim: our robot delivered the cold box successfully in 9 out of 10 test runs. The failed run happened when the box started 1 cm forward, so our next improvement is a wider lead-in guide.

Evidence makes claims honest.

### 10. Testing Connects To Food Systems
Food systems also test reliability. A cold chain uses temperature logs. A farm trial compares plant growth. A warehouse checks inventory accuracy. A food safety system tests for hazards. A waste programme measures how much waste changed.

Testing is not only a robotics habit. It is how real food systems protect people.

### 11. Version Control For Students
Version control means knowing what changed. You can use simple version names:

```text
Gripper V1: two-finger claw
Gripper V2: wider contact pads
Program V3: slower turn before delivery
```

If you do not record versions, you may forget which design worked. Teams should photograph builds, save programs, and write changes in the notebook.

### 12. Stop Rules Prevent Endless Tweaking
A stop rule tells you when a design is good enough for now. Example: if the robot succeeds 8 out of 10 times for two sessions, stop changing that mission and work on the next one.

Without stop rules, teams may keep changing a working design and accidentally make it worse.


## Expanded Knowledge Notes

### Qualitative And Quantitative Evidence
Qualitative evidence describes what happened in words, photos, or videos. Example: "The robot's left wheel slipped during the turn."

Quantitative evidence uses numbers. Example: "The robot succeeded in 7 out of 10 runs" or "average time was 18.4 seconds."

Strong engineering notebooks use both. Numbers show patterns. Words explain causes.

### Success Rate
Success rate is the fraction or percentage of successful runs.

```text
success rate = successful runs / total runs
```

If the robot succeeds 8 out of 10 times, the success rate is 80%. This is more informative than saying "it usually works."

But success rate alone is not enough. You should also record failure modes.

### Average And Spread
Average time tells the typical performance. Spread tells how much results vary. A robot that finishes in 20, 21, 20, 21, and 20 seconds is more predictable than one that finishes in 10, 35, 18, 40, and 12 seconds, even if averages are similar.

For competition, predictable performance is valuable because strategy depends on time.

### Stress Testing
Stress testing means testing a system under harder conditions. For NRC, stress tests might include:

- object shifted 1 cm,
- lower battery,
- faster reset,
- slightly different start angle,
- mat seam or bump,
- running after several previous missions,
- noisy room or rushed team setup.

Stress tests reveal whether a design is fragile.

### Regression
Regression means a new change breaks something that used to work. Example: you improve the gripper but now the robot turns poorly because the attachment is heavier.

After major changes, retest old missions. Do not assume they still work.

### Checklists Reduce Human Error
A checklist is a simple reliability tool. Pilots, engineers, doctors, and food-safety workers use checklists because humans forget things under pressure.

A robotics pre-run checklist might include:

- battery checked,
- correct program selected,
- attachment locked,
- start position aligned,
- mission objects reset,
- wires clear,
- team roles ready.

Checklists are not childish. They are professional.

### Sensor Calibration Tests
A sensor calibration test checks whether sensor readings are trustworthy. For a colour sensor, test readings under competition lighting. For a distance sensor, test known distances. For motor rotation, test whether 360 degrees moves the expected distance.

Calibration should be recorded. If readings drift, the program may need thresholds adjusted.

### Failure Analysis: Five Whys
Five Whys is a simple root-cause method. Ask why repeatedly.

Problem: robot dropped crate.

Why? Gripper opened early.

Why? Program reached release block too soon.

Why? Robot turned less than expected and reached the condition early.

Why? Wheel slipped during acceleration.

Why? Speed was too high for the turn.

Possible fix: reduce speed or change turn method.

You do not always need exactly five whys. The point is to go deeper than the first symptom.

### Evidence For Judges
Judges may not see all your practice. Your notebook can show evidence. Good evidence includes tables, photos, version notes, graphs, and short explanations of changes.

A clear chart showing success rate improvement is powerful:

```text
V1: 3/10 successful
V2: 6/10 successful after wider guide
V3: 9/10 successful after slower approach
```

This shows learning, not just final performance.

### Testing Food-System Claims
If your project says it models cold-chain reliability, test delivery time and correct destination. If it says it reduces waste, test sorting accuracy. If it says it handles fragile food, test drops and contact force ideas. If it says it responds to climate disruption, test the backup route.

The evidence should match the claim.

## Further Deep-Dive Notes

### A Test Matrix Makes Practice More Scientific
A test matrix is a table that shows what you will test and what you will measure. It prevents practice from becoming random driving. It also helps your team notice patterns.

Example test matrix:

| Test question | Variable changed | What stays the same | Evidence collected |
| --- | --- | --- | --- |
| Does slower speed improve delivery? | Motor speed | Route, object, battery level | Success count and time |
| Does a wider attachment reduce drops? | Attachment width | Speed, object, route | Number of drops |
| Does sensor threshold work in different light? | Room lighting | Program, robot, marker | Correct readings |
| Does backup route help? | Route choice | Object, destination | Success when obstacle appears |

The variable changed is the thing you are testing. What stays the same is the control. A control is important because if everything changes, you cannot tell what caused the result. If the robot succeeds after you changed speed, attachment, route, and battery at the same time, you do not know which change helped.

### Success Rate, Average, And Spread
Success rate tells how often something works. If a robot completes a mission 8 times out of 10, the success rate is 80 percent. This is useful, but it is not the whole story. Time also matters. A robot that succeeds 8/10 but takes 90 seconds may be less useful than a robot that succeeds 8/10 in 45 seconds, depending on the mission.

Average is a typical value. If delivery times are 41, 43, 44, 46, and 46 seconds, the average is 44 seconds. Spread tells how different the results are from each other. If times are 20, 35, 44, 61, and 60 seconds, the average may still look acceptable, but the spread is large. Large spread means the robot is unpredictable.

For competition readiness, predictability is valuable. A predictable robot lets the team plan. An unpredictable robot creates stress because the same program may behave very differently each run.

### Reliability Is Built By Repetition
One successful run is encouraging, but it is weak evidence. Ten successful runs are stronger. Thirty runs are stronger still. Reliability means the system keeps working when small things change.

In real food systems, reliability protects people. A cold chain must keep food cold not just once, but every day. A sorting machine must identify products not just in a demonstration, but across thousands of items. A food-safety alarm must work when workers are tired, when the room is busy, and when a delivery is late.

For your robot, repetition can reveal hidden problems:

1. Battery level changes motor strength.
2. Tires collect dust and slip.
3. Attachments loosen.
4. Markers move slightly.
5. A cable rubs against a wheel.
6. The robot starts at a slightly different angle.
7. The table surface reflects light differently.

These are not excuses. They are data. A strong team treats surprises as evidence about the system.

### Stress Testing Finds Weak Points
Stress testing means testing under harder conditions than usual. You do this carefully, not to break the robot, but to learn what conditions make the design fail.

Robot stress tests might include:

1. Start the robot 1 centimeter left or right of the usual position.
2. Use a slightly heavier food token.
3. Run the program with lower battery.
4. Add a small obstacle marker.
5. Try the mission under different room lighting.
6. Repeat the run after moving the attachment slightly.

Food-system stress tests also exist. A warehouse may test what happens if a freezer loses power. A delivery company may test a blocked road. A farm may plan for drought. A food-rescue network may test what happens when donations arrive late. Stress testing helps people prepare before a real problem happens.

### Root Cause Examples
Root cause analysis asks why a failure really happened. The first answer is often too shallow.

Example 1:

```text
Problem: robot missed the delivery zone
Why 1: it turned too far
Why 2: the wheel slipped during the turn
Why 3: the turn speed was high
Why 4: the program used the same speed for travel and precision
Root cause idea: no slow mode for precision movement
```

Example 2:

```text
Problem: robot sorted a green token as yellow
Why 1: color sensor reading was wrong
Why 2: reflected light changed
Why 3: the sensor was too high above the token
Why 4: the attachment bent during pickup
Root cause idea: sensor distance was not controlled
```

Example 3:

```text
Problem: food-rescue mission is hard to explain
Why 1: the mission has too many actions
Why 2: actions do not match one clear science idea
Why 3: the team added ideas without choosing a main problem
Root cause idea: project scope is too broad
```

Good root cause analysis connects robot behavior, physical design, program logic, and science meaning.

### Regression Testing Protects Improvements
Regression testing means checking that a new change did not break something that used to work. For example, you make the claw stronger. Now it grabs better, but it may also hit a wall during turning. The old route must be tested again.

Use a short regression checklist:

1. Can the robot still leave base correctly?
2. Can it still find the line or marker?
3. Can it still pick the object?
4. Can it still deliver to the old destination?
5. Did the new part change the robot's size?
6. Did the new code change a shared variable?

Regression testing is common in software engineering. It is also useful in food systems. If a factory changes packaging, it must check that labels still fit, barcodes still scan, cooling still works, and transport boxes still stack safely.

### Evidence Graphs Tell A Story
Graphs can show improvement better than long sentences. A line graph can show success rate by program version. A bar graph can compare delivery time before and after a design change. A scatter plot can show whether faster speed causes more drops.

Do not make graphs only for decoration. A graph should answer a question. Good graph titles are specific:

1. "Delivery Success Improved After Speed Reduction"
2. "Wider Scoop Reduced Drops During Turns"
3. "Sensor Error Increased Under Bright Light"
4. "Backup Route Took Longer But Avoided Blocked Path"

When explaining a graph, use claim-evidence-reasoning:

```text
Claim: The slower approach improved delivery reliability.
Evidence: Success increased from 5/10 to 9/10.
Reasoning: Lower speed reduced overshoot near the target.
```

This is the same kind of thinking used in science communication.

### Avoid Overfitting To One Perfect Setup
Overfitting means a solution works only for one very specific situation. A robot may work perfectly only when the starting position is exact, the table is clean, the battery is full, and the judge places pieces in exactly the expected position. That is risky.

To reduce overfitting, build tolerance. Tolerance means the robot can handle small differences. A wider guide may tolerate a token being slightly off-center. A sensor-based stop may tolerate small distance changes. A slower final approach may tolerate wheel slip. Clear alignment tools may help the team start consistently.

In food systems, overfitting also happens. A supply chain designed only for normal weather may fail during heatwaves. A menu designed for one ingredient may fail when that ingredient becomes expensive. A food rescue plan designed for one store may not work for a whole city. Robust systems handle variation.

### Competition Readiness Checklist
Before the final week, test more than the robot. Test the whole team system:

1. Is the robot build strong enough for repeated handling?
2. Are spare parts ready?
3. Is the program version clearly named?
4. Does the team know which program to run?
5. Can each student explain one science idea?
6. Can each student explain one robot decision?
7. Does the notebook show evidence, not only pictures?
8. Has the team practiced after a failed run?
9. Is the mission story short and clear?
10. Does the robot behavior match the story?

The goal is not perfection. The goal is a system that can be understood, tested, repaired, and explained.

## Core Terms

### Test Plan
A planned set of checks that answers a clear question.

### Reliability
How consistently a system works over repeated trials.

### Variable
Something that can change, such as speed, angle, or start position.

### Control
Something kept the same during a test.

### Success Criteria
The rules that define whether a test passed.

### Failure Mode
A specific way a system fails.

### Root Cause
The deeper reason a failure happens.

### Iteration
One cycle of improving a design.

### Evidence
Recorded information that supports a claim.

### Calibration
Checking or adjusting a sensor or system so measurements are trustworthy.

### Version
A named stage of a design or program.

### Stop Rule
A rule that tells the team when to stop changing and move on.

## Student Thinking Tasks

1. Choose one robot mission and write a test question.
2. Define success criteria.
3. Make a 10-run table with columns for result, time, and failure mode.
4. Identify one hidden variable to control.
5. Write one hypothesis for a failure.
6. Write an evidence-based claim using imaginary or real test results.

## Sources For Further Reading
- NASA eClips Engineering Design Packets: https://science.nasa.gov/science-research/earth-science/engineering-design-packets/
- NASA Software, Robotics, and Simulation Division: https://www.nasa.gov/software-robotics-and-simulation-division/
- Scratch Getting Started: https://www.scratchfoundation.org/learn/learning-library/getting-started
- Scratch Learning Library: https://www.scratchfoundation.org/learn/learning-library
- LEGO Education SPIKE Essential: https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/
- Science Centre Singapore NRC: https://www.science.edu.sg/for-schools/competitions/national-robotics-competition
