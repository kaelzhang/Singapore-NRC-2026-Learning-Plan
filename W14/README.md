# W14 - Computational Thinking With Scratch And SPIKE Essential

## Big Question
How do we turn a Mission Meals idea into clear robot logic?

## Why This Week Matters
A robot can only act autonomously if its program is clear. Scratch and SPIKE-style block coding help you build logic step by step. The important ideas are sequence, event, loop, condition, variable, state, and debugging.

This week connects food-system thinking to robot-system logic.

## The One-Minute Idea
Computational thinking means solving problems in a structured way so a computer or robot can follow the steps. A robot needs exact instructions, but a good team also needs abstraction: hiding unnecessary details so the main plan is clear.

For an eight-year-old: a program is a recipe for a robot, but the robot follows the recipe very literally.

## Past, Present, Future
### Past
Early machines followed mechanical patterns, cams, gears, and fixed controls. Later computers made machines programmable. Educational programming languages such as Scratch made coding easier to learn through blocks.

### Present
Students can use Scratch-like blocks and LEGO SPIKE tools to program movement, sensors, lights, loops, and conditions. SPIKE Essential is designed for young learners and includes a hub, motors, sensors, and a coding app.

### Future
Future robots may use AI and more advanced autonomy, but they still depend on good problem decomposition, clear states, reliable sensors, and testable logic.

## Deep Explanation
### 1. Decomposition Breaks A Big Mission Into Steps
Do not start with "solve Mission Meals." Start with:

```text
leave base
drive to marker
stop
lower tool
push crate
back up
turn
deliver object
return
```

A big mission becomes many small actions.

### 2. Sequence Is Order
Sequence means one instruction happens after another. Robots are sensitive to order. If the robot opens a gripper before reaching the object, the mission fails.

### 3. Loops Repeat Useful Actions
A loop repeats instructions. Use a loop when the robot must do the same action many times, such as moving three crates or checking several stations.

### 4. Conditions Let The Robot Choose
A condition is an if-then rule:

```text
if colour is green, stop
if count equals 3, return to base
if object is detected, close gripper
```

Conditions make a robot more autonomous.

### 5. Variables And States Help Multi-Step Missions
A variable stores information. A state describes what phase the robot is in.

Example:

```text
state = "collecting"
crate_count = 0
```

When a robot does several missions, states help the team avoid confusing one phase with another.

## Core Terms
### Computational Thinking
Solving problems using decomposition, patterns, abstraction, algorithms, and debugging.

### Algorithm
A clear step-by-step method for solving a problem.

### Sequence
Instructions in order.

### Loop
Instructions that repeat.

### Condition
An if-then rule that lets a program choose.

### Variable
A named place to store information.

### State
The current phase or mode of a system.

### Debugging
Finding and fixing mistakes in a program or system.

## Robot Connection
Take a food logistics mission:

```text
Goal: deliver three crates to cold storage.

Set crate_count to 0.
Repeat until crate_count = 3:
  drive to pickup
  collect crate
  drive to cold storage
  release crate
  change crate_count by 1
return to base
```

This is not just code. It is a thinking tool.

## Student Tasks
1. Choose one mission from earlier weeks.
2. Break it into 6 to 10 steps.
3. Add one loop.
4. Add one condition.
5. Add one variable or state.
6. Explain where debugging would likely be needed.

## Video Shelf
1. Scratch Team - Minute with Mitch, Getting Started: https://www.youtube.com/watch?v=0Qb9UFiwH64
2. LEGO Education - Getting Started with SPIKE Portfolio: https://www.youtube.com/watch?v=VPtLZj4vgG0
3. The Moment Makers Robotics - Getting Started with LEGO SPIKE Essential: https://www.youtube.com/watch?v=ZkG1v1owSq4
4. Creator Academy Australia - Getting Started With SPIKE Essential: https://www.youtube.com/watch?v=T6VI_bb7biQ
5. griffpatch - Scratch Basics, A Beginners Guide to Scratch: https://www.youtube.com/watch?v=zOa5o9Yq_ZU
6. Mike Neumire - Meet Computational Thinking Standards with Scratch: https://www.youtube.com/watch?v=hkcMm5YGKig

## Sources For Further Reading
- Scratch Learning Library: https://www.scratchfoundation.org/learn/learning-library
- Scratch Getting Started: https://www.scratchfoundation.org/learn/learning-library/getting-started
- LEGO Education SPIKE Essential: https://education.lego.com/en-us/products/lego-education-spike-essential-set/45345/
- LEGO Education SPIKE Essential support: https://education.lego.com/en-us/product-resources/45345-spike-essential-resource-page/
