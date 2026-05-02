# W14 Science - Computational Thinking With Scratch And SPIKE Essential

This student document contains the science and food-system knowledge for the week. For robot building and programming work, see `robotics.md`.

## Big Question
How do we turn a Mission Meals idea into clear robot logic?

## Why This Week Matters
A robot can only act autonomously if its program is clear. Scratch and SPIKE-style block coding help you build logic step by step. The important ideas are sequence, event, loop, condition, variable, state, and debugging.

This week connects food-system thinking to robot-system logic. A food-system problem becomes a mission model. A mission model becomes robot actions. Robot actions become program logic.

## The One-Minute Idea
Computational thinking means solving problems in a structured way so a computer or robot can follow the steps. A robot needs exact instructions, but a good team also needs abstraction: hiding unnecessary details so the main plan is clear.

A program is a recipe for a robot, but the robot follows the recipe very literally. If the recipe says the wrong step first, the robot does the wrong step first.

## Past, Present, Future

### Past
Early machines followed mechanical patterns, cams, gears, and fixed controls. Later computers made machines programmable. Educational programming languages such as Scratch made coding easier to learn through blocks.

Before block coding, programming often required typing exact text commands. Blocks help beginners focus on logic before worrying about punctuation.

### Present
Students can use Scratch-like blocks and LEGO SPIKE tools to program movement, sensors, lights, loops, and conditions. SPIKE Essential includes a hub, motors, sensors, and a coding app for introductory robotics work.

Scratch projects also teach computational thinking beyond robotics: events, sprites, loops, variables, debugging, and creative design.

### Future
Future robots may use AI and more advanced autonomy, but they still depend on good problem decomposition, clear states, reliable sensors, and testable logic.

Even AI systems need goals, data, constraints, safety checks, and debugging. Computational thinking remains important because it teaches you how to structure a problem.

## Deep Explanation

### 1. Decomposition Breaks A Big Mission Into Steps
Do not start with "solve Mission Meals." Start with smaller steps:

```text
leave base
follow route
detect marker
stop
lower tool
push crate
back up
turn
deliver object
release
return
```

A big mission becomes many small actions. Decomposition makes building, programming, and testing easier.

### 2. Patterns Help You Reuse Ideas
A pattern is something that repeats. Many robot missions share patterns:

```text
drive -> align -> act -> back up
```

or:

```text
sense -> choose -> move -> release
```

When you notice patterns, you can reuse code ideas. A delivery mission and a waste-sorting mission may use the same "drive to zone and release" pattern.

### 3. Abstraction Hides Unneeded Details
Abstraction means focusing on the important idea and hiding details for the moment. Instead of writing every motor movement, you can name a routine:

```text
deliver_crate_to_market()
```

Inside that routine are smaller steps. Abstraction helps teams discuss strategy without getting lost.

For a young student, abstraction can be as simple as naming a mission block: "collect," "deliver," "sort," or "return."

### 4. Algorithm Means Step-By-Step Method
An algorithm is a clear method for solving a problem. It does not have to be computer code. A recipe, route plan, or sorting rule can be an algorithm.

A robot algorithm must be precise. "Move a bit" is not precise. "Move forward 20 cm at speed 30" is more precise. "If colour sensor reads green, stop" is a clear condition.

### 5. Sequence Is Order
Sequence means one instruction happens after another. Robots are sensitive to order. If the robot opens a gripper before reaching the object, the mission fails. If it turns before backing away, it may hit the model.

Good teams read programs like stories: first, next, then, finally. If the story order is wrong, fix the sequence before changing the hardware.

### 6. Events Start Actions
An event is something that starts a script or action. In Scratch, an event might be clicking the green flag. In robotics, an event might be pressing start, detecting a colour, reaching a time, or receiving a sensor value.

Events help programs respond. Instead of only fixed timing, a robot can wait for something to happen.

### 7. Loops Repeat Useful Actions
A loop repeats instructions. Use a loop when the robot must do the same action many times, such as moving three crates or checking several stations.

Loops reduce repeated code, but they must have clear stop conditions. An infinite loop that never stops can trap the robot.

Example:

```text
repeat until crate_count = 3:
    collect crate
    deliver crate
    add 1 to crate_count
```

### 8. Conditions Let The Robot Choose
A condition is an if-then rule:

```text
if colour is green, stop
if count equals 3, return to base
if object is detected, close gripper
```

Conditions make a robot more autonomous. But conditions depend on reliable sensors and clear thresholds. If the colour sensor is confused by shadows, the condition may choose the wrong action.

### 9. Variables Store Information
A variable stores information. Examples:

```text
crate_count = 0
mission_time = 0
state = "collecting"
```

Variables help the robot remember. Without variables, the robot may not know how many objects it has delivered or which stage it is in.

### 10. State Describes The Current Phase
A state describes what mode the robot is in. For a Mission Meals robot:

```text
state = "leaving_base"
state = "collecting_food"
state = "delivering_food"
state = "returning"
```

States help teams organize multi-step missions. If the robot fails, you can ask which state failed.

### 11. Debugging Is Part Of Programming
Debugging means finding and fixing mistakes. A bug can be in code, mechanism, sensor placement, battery level, starting position, or strategy.

Debugging is not guessing randomly. It should follow a loop:

```text
observe -> name the problem -> guess cause -> change one thing -> test -> record
```

### 12. Food-System Logic Becomes Robot Logic
Food problem: cold food must go to cold storage.

Robot logic:

```text
if item_type = "cold":
    deliver to cold zone
else:
    deliver to dry storage
```

Food problem: stressed plants need inspection.

Robot logic:

```text
if plant_marker = "yellow":
    move tray to inspection zone
else:
    move tray to harvest zone
```

Food problem: safe surplus should be rescued.

Robot logic:

```text
if food_status = "safe_surplus":
    deliver to rescue zone
else:
    deliver to compost or disposal zone
```

Programming is the translation from meaning to action.


## Expanded Knowledge Notes

### Pseudocode Helps Before Blocks
Pseudocode means writing program logic in plain language before building it with blocks. It is not exact code. It is a plan.

Example:

```text
start
move to farm zone
if plant marker is yellow:
    move tray to inspection
else:
    move tray to market
return to base
```

Pseudocode helps teams agree before dragging blocks into a program.

### Sensor Logic Needs Thresholds
Sensors give values. Programs must decide what values mean. A colour sensor may read green, yellow, red, or reflected light numbers. A distance sensor may report centimetres. A force sensor may report pressed or not pressed.

A threshold is a boundary value. Example: if distance is less than 5 cm, stop. Thresholds need testing because real readings can change.

A sensor without a tested threshold can make unreliable decisions.

### State Machines
A state machine is a way to organize a system by states and transitions. A state is the current phase. A transition changes the state.

Example:

```text
state: leaving_base
transition: reaches line
state: following_line
transition: sees green marker
state: delivering
transition: object released
state: returning
```

State machines help when missions have several stages. They prevent the robot from trying to do everything at once.

### Functions Or My Blocks
Many block systems allow custom blocks or functions. A function is a named group of instructions. It helps reuse code.

Example functions:

```text
drive_to_farm()
align_to_wall()
lower_gripper()
deliver_crate()
return_to_base()
```

Functions make programs easier to read and debug. If `align_to_wall()` fails, you can test that part separately.

### Timing Versus Sensor-Based Control
A timing program says: drive for 2 seconds. A sensor-based program says: drive until you see the line. Timing can be simple, but it may fail if battery, friction, or start position changes. Sensor-based control can adapt, but sensors can be noisy or misread.

Good robots often combine methods: motor degrees for distance, sensors for correction, and physical alignment for reliability.

### Line Following As Feedback
Line following is a feedback system. The robot reads the line, compares the reading to the goal, turns slightly, reads again, and adjusts.

This is similar to precision agriculture: measure, compare, decide, act, check. Computational thinking appears in both farms and robots.

### Parallel Thinking: Robot And Food System
A food system can also be written like logic:

```text
if food is perishable:
    use cold chain
if food is safe surplus:
    rescue
if plant is stressed:
    inspect
if route is blocked:
    use backup route
```

Programming helps you express system rules clearly. It makes hidden decision-making visible.

### Debugging Code And Debugging Systems
When a robot fails, the bug may not be in code. It may be in the mechanism, sensor placement, mat friction, start position, or mission strategy.

Computational thinking still helps because you can isolate the problem. Is the sequence wrong? Is the condition wrong? Is the variable not updating? Is the state changing too early? Is the sensor unreliable?

### Readability Matters
A program that works but nobody understands is risky. Use clear names, comments when helpful, and organized blocks. Avoid giant tangled scripts.

Team robotics is collaborative. Your teammates need to understand the program when you are not holding the laptop.

### Mission Logic Examples
Cold-chain logic:

```text
if item = cold_food:
    drive to cold_storage
else:
    drive to dry_storage
```

Waste logic:

```text
if food_status = safe_surplus:
    rescue
else if food_status = compostable:
    compost
else:
    disposal
```

Climate logic:

```text
if route_blocked:
    use_backup_route
if heat_marker_seen:
    deliver_shade_resource
```

These examples show how science becomes robot decisions.

## Further Deep-Dive Notes

### From A Real Food Problem To A Robot Program
Computational thinking begins before you touch the robot. Suppose the real-world problem is food waste. A store has fresh food, soon-to-expire food, unsafe food, and compostable scraps. A human can look, smell, read labels, and make a decision. A robot cannot magically understand all of this. The team must translate the big problem into signals the robot can detect.

The translation might look like this:

1. Fresh food is represented by a green marker.
2. Soon-to-expire food is represented by a yellow marker.
3. Unsafe food is represented by a red marker.
4. Compostable scraps are represented by a brown marker.
5. The robot's job is to read the marker and deliver the object to the correct area.

This is abstraction. The real world is complex, but the model keeps the most important idea: different food states need different actions. Abstraction is not pretending details do not exist. It is choosing which details belong in the model right now.

After abstraction, the team writes an algorithm. A beginner algorithm might be:

```text
go forward
pick food
look at color
if green, deliver to market
if yellow, deliver to rescue
if red, deliver to inspection
if brown, deliver to compost
return home
```

This algorithm can become a Scratch, SPIKE, or block program. But before programming, you should ask whether each step is clear enough. "Look at color" may need sensor calibration. "Pick food" may need a motor position. "Return home" may need line following, angle turning, or a route made from distances.

### Data Flow: How Information Moves Through A Program
Data flow means the path information takes inside a program. A food system has data flow too. A temperature sensor sends data to a storage worker. A label sends data to a buyer. A shipping record sends data to a warehouse. In a robot, the same idea appears in a smaller form.

A color sensor may read reflected light. The program stores the reading in a variable. A condition checks the variable. The robot chooses a motor action. Then the robot changes the world by moving an object. The world changes the next sensor reading. This loop is called feedback.

Here is a simple data-flow chain:

```text
sensor reading -> variable -> condition -> action -> new position -> new sensor reading
```

If the chain breaks, the robot behaves strangely. If the sensor reading is noisy, the variable is unreliable. If the condition uses the wrong threshold, the robot makes the wrong decision. If the action is too fast, the robot may overshoot. Debugging often means finding which link in the chain is weak.

### State Tables Help You Avoid Confusion
A state is what mode the robot is currently in. For example, a food-rescue robot might have these states:

| State | What the robot is doing | What changes the state |
| --- | --- | --- |
| Search | Looking for a food token | Token detected |
| Identify | Reading the marker | Color decision made |
| Carry | Holding the token | Route begins |
| Deliver | Moving to the destination | Destination reached |
| Release | Dropping the token | Token released |
| Return | Going back to start | Start reached |

A state table helps because a robot cannot do everything at the same time. It should not release a token while it is still searching. It should not return home before delivery. When your code is confusing, write a state table in your notebook. Then each program block has a job.

State machines are common in real robotics. A warehouse robot, farm robot, or food-delivery robot may have states such as waiting, navigating, avoiding obstacle, picking, charging, and reporting error. A state machine is a map of possible modes and how the robot moves between them.

### Conditions Are Scientific Decisions
An `if` block looks simple, but it is actually a decision rule. In science, a decision rule must match evidence. If a food item is unsafe above a certain temperature, the system needs a threshold. A threshold is a boundary number where the decision changes.

For a robot, a threshold might be:

```text
if reflected_light < 25:
    black_line_detected
```

For a food system, a threshold might be:

```text
if storage_temperature is too high:
    send_alert
```

The exact threshold should be tested. If it is too strict, the robot may reject good readings. If it is too loose, the robot may accept bad readings. This is why programming and testing belong together. You do not only write logic. You measure whether the logic works.

### Loops Need Exit Rules
A loop repeats actions. Loops are powerful because robots need repeated checking. A line follower repeatedly reads a sensor and corrects motor speed. A sorting robot repeatedly checks for new food tokens. A timer loop repeatedly asks whether a mission time has ended.

But every important loop needs an exit rule. An exit rule tells the program when to stop repeating. Without one, the robot may get stuck. Examples:

```text
repeat until food_detected
repeat until destination_reached
repeat until timer > 60 seconds
repeat until touch_sensor_pressed
```

In food systems, exit rules exist too. A drying process stops when moisture is low enough. A delivery route ends when all packages are delivered. A recall investigation ends only when the source is found and affected products are removed. Good loops protect systems from unfinished work.

### Common Programming Mistakes In Robotics Missions
Mistake 1: The program uses distance only, but the wheel slips. Better design: combine distance with sensor feedback or physical guides.

Mistake 2: The robot turns too fast near a target. Better design: slow down before precision actions.

Mistake 3: The code has many repeated blocks. Better design: use a custom block or function for repeated moves.

Mistake 4: The robot checks a sensor once and trusts it. Better design: read several times or confirm with a second condition.

Mistake 5: The program handles the happy path but not errors. Better design: include backup states, such as retry, reverse, or stop.

Mistake 6: The team changes many things at once. Better design: change one variable, test, and record the result.

These are not only robot lessons. They match food-system thinking. A farm, factory, or delivery network also fails when it depends on one fragile step, has no backup rule, or changes too many variables without evidence.

### Pseudocode Can Become Team Language
Pseudocode is a bridge between human thought and computer code. It does not need perfect programming syntax. It needs clear logic. Good pseudocode helps builders, programmers, and presenters speak the same language.

For example:

```text
mission: rescue soon-to-expire food
go to shelf
scan food marker
if marker is yellow:
    move food to rescue truck
else:
    leave food in place
return to checkpoint
```

The builder can ask, "Where does the robot scan?" The programmer can ask, "Which sensor reading means yellow?" The presenter can ask, "What food problem does yellow represent?" The team can improve the mission before building a complicated program.

### Programming Notebook Habits
Keep a simple programming notebook. Each entry should include:

1. Date and program version.
2. What changed.
3. Why the team changed it.
4. Test result.
5. Next idea.

Example:

```text
Version 4
Change: lower speed from 50 to 30 near delivery zone
Reason: robot pushed food token too far
Result: 8/10 successful deliveries
Next: add short reverse after release
```

This notebook is also evidence. It shows that your team used computational thinking, not random guessing. In a competition, strong thinking is visible in the way you explain your program.

### Sensors Are Helpful, But Not Magical
A sensor is a measuring tool. It does not understand the world the way a person does. A color sensor does not know "this is rescue food." It only measures reflected light or color information. A distance sensor does not know "this is a shelf." It only measures how far away something appears to be. Your program gives meaning to the measurement.

This is why calibration matters. Calibration means comparing sensor readings with known examples and choosing rules that work. If a yellow marker sometimes reads like green, the team may need better lighting, a closer sensor position, a larger marker, or a decision rule that checks more than once.

In food systems, sensors also need interpretation. A temperature sensor can warn that a cold room is too warm, but people still need rules for what to do next. Should the food be moved, inspected, sold quickly, or discarded? Computational thinking connects measurement to action.

## Core Terms

### Computational Thinking
Solving problems using decomposition, patterns, abstraction, algorithms, and debugging.

### Decomposition
Breaking a big problem into smaller parts.

### Pattern
A repeated structure or action that can be reused.

### Abstraction
Focusing on the important idea while hiding unnecessary detail.

### Algorithm
A clear step-by-step method for solving a problem.

### Sequence
Instructions in order.

### Event
Something that starts an action or script.

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

## Student Thinking Tasks

1. Choose one Mission Meals task and decompose it into at least eight steps.
2. Identify one repeated pattern in the task.
3. Write one if-then condition for the robot.
4. Create one variable that would help the robot remember progress.
5. Name three possible states for the mission.
6. Write a debugging plan for one likely failure.
