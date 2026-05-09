# W14 Science Brief - Computational Thinking With Scratch And SPIKE

This brief keeps the main ideas from `science.md` for shorter review.

## Big Idea
A robot can only act clearly if its program is clear. **Computational thinking** means breaking a problem into parts, finding patterns, choosing the important details, writing step-by-step rules, and debugging.

A food-system idea becomes a robot mission only when you translate meaning into actions the robot can follow.

## Past, Present, And Future
In the past, machines followed fixed mechanical patterns, cams, gears, and simple controls. Later, computers made machines programmable. Scratch-style blocks helped beginners learn logic without first typing difficult code syntax.

Today, Scratch and LEGO SPIKE-style block coding let students program motors, sensors, lights, sounds, loops, conditions, variables, and events. The same logic ideas appear in real robotics.

In the future, robots may use more AI, but they will still need clear goals, states, data, constraints, safety checks, and debugging. Good thinking still matters.

## Decomposition
**Decomposition** means breaking a big mission into smaller steps. Do not start with "solve Mission Meals." Start with steps such as leave base, follow route, detect marker, stop, lower tool, push crate, back up, turn, release, and return.

Small steps are easier to build, program, test, and explain.

## Patterns And Abstraction
A **pattern** is a repeated structure. Many missions follow patterns such as:

```text
drive -> align -> act -> back up
```

or:

```text
sense -> choose -> move -> release
```

**Abstraction** means focusing on the important idea and hiding details for now. A real food-waste system is complex, but a robot model might use four markers: fresh food, soon-to-expire food, unsafe food, and compostable scraps. That is acceptable if the model keeps the important decision.

## Algorithms And Sequence
An **algorithm** is a clear step-by-step method. A recipe, route plan, sorting rule, or robot program can be an algorithm.

**Sequence** means the order of instructions. Robots follow order very literally. If the robot opens the gripper before reaching the object, it fails. If it turns before backing away, it may hit a model.

Read a program like a story: first, next, then, finally.

## Events, Loops, And Conditions
An **event** starts an action. In Scratch, clicking the green flag is an event. In robotics, pressing start, detecting a colour, touching a sensor, or reaching a time can be an event.

A **loop** repeats instructions. It is useful for line following, checking sensors, moving several objects, or repeating a delivery. A loop needs an exit rule, such as "repeat until destination reached" or "repeat until count equals 3."

A **condition** is an if-then rule. For example:

```text
if marker is yellow, deliver to rescue
if marker is red, deliver to inspection
if distance is less than 5 cm, stop
```

Conditions make a robot choose, but they depend on reliable sensors and tested thresholds.

## Variables And State
A **variable** stores information, such as crate count, mission time, sensor reading, or current route.

A **state** is the current phase of a system: searching, identifying, carrying, delivering, releasing, returning, or stopping. A **state machine** organizes a mission so the robot does not try to do everything at once.

If a robot fails, ask which state failed. That makes debugging easier.

## Sensors Need Meaning
A sensor does not understand the world like a person. A colour sensor measures reflected light. The program gives that reading meaning.

This is why thresholds and **calibration** matter. If yellow sometimes reads like green, the team may need better lighting, a closer sensor, a larger marker, or a rule that checks more than once.

A food system works the same way. A temperature sensor warns that a cold room is warm, but people still need a rule for what action follows.

## Debugging
**Debugging** means finding and fixing mistakes. The bug may be in code, mechanism, sensor placement, battery level, start position, or strategy.

Use a calm loop:

```text
observe -> name the problem -> guess cause -> change one thing -> test -> record
```

Changing many things at once makes it hard to learn.

## Food-System Logic Becomes Robot Logic
Food-system rules can become code rules.

Cold chain:

```text
if item is cold food, deliver to cold storage
else deliver to dry storage
```

Waste sorting:

```text
if food is safe surplus, rescue
else if compostable, compost
else inspect or dispose
```

Climate resilience:

```text
if route is blocked, use backup route
if heat marker is seen, deliver shade resource
```

Programming is the translation from meaning to action.

## Mission Meals Connections
A strong robot program has a clear mission, small steps, reusable patterns, tested sensor rules, named variables, states, and a debugging record.

Pseudocode helps before blocks. It lets builders, programmers, and presenters agree on the plan before coding.

## Extra Details To Remember
Pseudocode helps before blocks. It is plain-language program logic, not final code. A team can write: go to shelf, scan marker, if yellow deliver to rescue, else leave it, return to checkpoint. Builders, programmers, and presenters can all understand it.

Data flow is the path information takes inside a program:

```text
sensor reading -> variable -> condition -> action -> new sensor reading
```

If one link is weak, the robot may behave strangely. Debugging often means finding the weak link.

Programs should handle more than the happy path. A happy path is what happens when everything goes perfectly. Real missions may need backup states: retry, reverse, stop, realign, or ask for reset.

A programming notebook should record the version, what changed, why it changed, test result, and next idea. This shows that the team improved by evidence instead of random guessing.

## Key Takeaways
Computational thinking helps you turn a big food problem into robot logic. The robot needs exact instructions, but the team needs the bigger meaning. Good programs are readable, testable, and connected to the science story.

Final check: choose one mission. Write one sequence, one condition, one variable, and three possible states.
