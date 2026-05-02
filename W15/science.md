# W15 Science - Testing, Reliability, Debugging, And Evidence

This student document contains the science and food-system knowledge for the week. For robot building and programming work, see `robotics.md`.

## Big Question
How do we know a robot works, instead of just getting lucky once?

## Why This Week Matters
In robotics competitions, one successful run is not enough. A team needs evidence that the robot can repeat the task under realistic conditions. This week teaches the engineering discipline behind reliability.

## The One-Minute Idea
Testing means trying a system in a planned way. Reliability means it works repeatedly. Debugging means finding and fixing the cause of failure. Evidence means records that show what happened.

For an eight-year-old: if your robot works once, say "interesting." If it works 10 times with records, say "we have evidence."

## Past, Present, Future

### Past
Engineers have always tested bridges, machines, ships, and tools because real systems can fail. Trial and error became stronger when people learned to record results and change one thing at a time.

### Present
Modern engineering uses test plans, control variables, failure analysis, checklists, version records, and reliability statistics. Robotics teams use run logs, battery checks, alignment marks, and slow-motion videos.

### Future
Future robots may test themselves with built-in sensors, simulation, digital twins, and automatic logs. But humans will still need to decide what matters, what failure means, and when a design is good enough.

## Deep Explanation

### 1. A Test Must Have A Question
Bad test: "Let's see what happens."

Better test: "At speed 40, can the robot deliver the crate to the target zone 5 times in a row?"

A test question tells you what to measure.

### 2. Change One Variable At A Time
If you change speed, wheel size, tool angle, and start position all at once, you will not know what caused the result. A variable is something that can change. Good testing changes one main variable and keeps the rest controlled.

### 3. Failure Modes Have Names
A failure mode is a specific way something fails:

- robot misses line,
- wheel slips,
- gripper opens early,
- object jams,
- sensor reads wrong colour,
- battery low,
- start position inconsistent.

Naming failure modes helps you fix causes, not symptoms.

### 4. Reliability Needs Repetition
A 5-run test is a useful first check. A 10-run test is stronger. Record each run:

```text
run number, setup, result, time, failure mode, change made
```

### 5. Debugging Is A Loop
Debugging is not random guessing. Use this loop:

```text
observe -> name failure -> form hypothesis -> change one thing -> test -> record
```

## Core Terms

### Test Plan
A planned set of checks that answers a clear question.

### Reliability
How consistently a system works over repeated trials.

### Variable
Something that can change, such as speed, angle, or start position.

### Control
Something kept the same during a test.

### Failure Mode
A specific way a system fails.

### Root Cause
The deeper reason a failure happens.

### Iteration
One cycle of improving a design.

### Evidence
Recorded information that supports a claim.

## Sources For Further Reading
- LEGO Education SPIKE Essential lessons: https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/
- Scratch Learning Library debugging resources: https://www.scratchfoundation.org/learn/learning-library/getting-started
- NRC official page: https://www.science.edu.sg/for-schools/competitions/national-robotics-competition
