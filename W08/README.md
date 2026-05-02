# W08 - Labour-Intensive Farming And Agricultural Robots

## Big Question
Which farm jobs are hard for people, and how can robots help without pretending to be complete farmers?

## Why This Week Matters
Many farm tasks are repetitive, time-sensitive, physically tiring, or difficult to staff. NRC's Labour-Intensive Farming challenge area is about noticing these tasks and translating them into robot actions.

This week is about automation, but with realistic thinking.

## The One-Minute Idea
Agricultural robots are usually task specialists. One robot may weed, another may harvest fruit, another may spray, another may carry crates. A good farm robot is designed for a clear job, crop, environment, and cost.

For an eight-year-old: a farm robot is often a very good helper for one kind of job, not a magic robot that does everything.

## Past, Present, Future
### Past
Farm labour used to depend heavily on hand tools, animal power, and many workers. Machines such as tractors reduced some heavy work, but many tasks like picking delicate fruits, weeding near crops, and sorting produce remained difficult to automate.

### Present
Robots and automated machines can now use cameras, GPS, lasers, arms, grippers, and machine learning. Some systems target weeds. Some help with spraying. Some test harvesting, packing, or transport.

### Future
Future agricultural robots may become smaller, safer, more modular, easier to repair, and better at working near plants and people. Big research problems remain: recognizing crops in messy environments, gripping without damage, moving on uneven ground, and making systems affordable.

## Deep Explanation
### 1. Labour-Intensive Means High Human Effort
A labour-intensive task needs a lot of human time or physical effort. Examples include:

- hand weeding,
- harvesting delicate crops,
- carrying crates,
- sorting produce,
- checking plant health,
- pollination in some systems,
- cleaning and packing.

These jobs can be tiring because they repeat thousands of times.

### 2. Robots Like Repetition, But Farms Are Messy
Factories are structured. Farms are not. Plants grow in different shapes. Fruit can hide behind leaves. Soil can be muddy. Sunlight changes. Objects are not always in the same place.

That is why agricultural robotics is hard.

### 3. A Robot Needs Sensing, Movement, And Action
Most farm robots need three abilities:

```text
sense: find the crop, weed, row, or object
move: travel to the right position
act: cut, pull, spray, pick, push, carry, or sort
```

The action part often depends on the end-effector, which you will study deeply in W09.

### 4. Automation Can Help Workers, Not Only Replace Them
A robot may reduce dangerous or tiring tasks. It may let workers focus on supervision, maintenance, quality checking, and decision-making. But if automation is too expensive or poorly designed, it can increase inequality.

### 5. Good Robot Design Starts With The Crop
A strawberry, mushroom, egg, fish, lettuce head, and tomato all need different handling. The robot must fit the object and the environment.

## Core Terms
### Automation
Using machines or control systems to perform tasks with less direct human effort.

### Agricultural Robot
A robot designed for farming, harvesting, monitoring, handling, or other agrifood tasks.

### Labour-Intensive
Requiring a lot of human work, time, or physical effort.

### End-Effector
The tool at the working end of a robot, such as a gripper, cutter, sprayer, or pusher.

### Machine Learning
A way for computers to improve pattern recognition from data and examples.

### Navigation
How a robot finds and follows a path.

### Payload
The amount of weight a robot can carry or handle.

### Safety Zone
The space a robot must respect so it does not harm people, crops, or equipment.

## Robot Connection
Start with one task:

```text
Weeding -> find weeds -> move tool over weed -> remove or mark weed
Harvesting -> find ripe crop -> grip gently -> detach -> place in container
Crate transport -> pick route -> carry load -> dock -> release
```

In NRC, your model does not need real crop recognition. But your design should represent the same idea:

- detect marker,
- move to object,
- use tool,
- place object correctly,
- repeat reliably.

## Student Tasks
1. List five farm jobs that are labour-intensive.
2. Pick one and break it into sense, move, act.
3. Decide whether the object is fragile, heavy, slippery, or easy to push.
4. Sketch a robot that does only that task.
5. Write one sentence about how the robot helps people and one concern about the robot.

## Video Shelf
1. Carbon Robotics - LaserWeeder: https://www.youtube.com/watch?v=eDUu48YCUy4
2. Carbon Robotics - LaserWeeder G2 600: https://www.youtube.com/watch?v=1fOMy7PcSgg
3. Cheddar - Farm robot uses lasers to destroy weeds: https://www.youtube.com/watch?v=H47F_dTvKkY
4. Agro BG Farmers MK - Autonomous robot for harvest apples: https://www.youtube.com/watch?v=BxdHyMke2JM
5. JAKA Robotics - Robot picking tomatoes: https://www.youtube.com/watch?v=7zpIeGihmKE
6. XMACHINES - Agricultural Robot for Spraying, Weeding and Mowing: https://www.youtube.com/watch?v=7pafixynoZo

## Sources For Further Reading
- FAO - Agricultural robotics and automated equipment: https://www.fao.org/sustainable-agricultural-mechanization/resources/publications/details/en/c/1363243/
- FAO SOFA 2022 automation report: https://www.fao.org/agrifood-economics/publications/detail/en/c/1613500/
- arXiv survey of robotic harvesting systems: https://arxiv.org/abs/2207.10457
