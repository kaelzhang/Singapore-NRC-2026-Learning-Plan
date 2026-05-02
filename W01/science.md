# W01 Science - Mission Meals And The Whole Food System

This student document contains the science and food-system knowledge for the week. For robot building and programming work, see `robotics.md`.

## Big Question
What does "Mission Meals" really mean, and why is a robotics competition asking us to think about food?

## Why This Week Matters
Mission Meals is not just about moving toy food pieces on a playfield. It is about a real human problem: every meal reaches a person through a food system. A food system includes farms, water, soil, sunlight, workers, machines, roads, ships, ports, warehouses, shops, homes, food safety checks, cooking, leftovers, and waste handling.

For NRC, this means your robot is not just "doing a mission." Your robot is acting out one part of a real system. It might help produce food, move food, protect food, sort food, recover food, or use a better tool. If you understand the real system, your robot decisions will make more sense.

This week is a framework week. It gives you the map that will connect all other weeks. Later weeks will zoom in on Singapore, farming history, hunger data, plant science, vertical farms, precision agriculture, agricultural robots, end-effectors, logistics, food waste, climate risk, future foods, programming, testing, and your final capstone explanation.

## Key Reference Links For This Week
Use these links when you want to check the real-world idea behind this lesson:

- [Science Centre Singapore National Robotics Competition](https://www.science.edu.sg/for-schools/competitions/national-robotics-competition) - the official NRC entrypoint for current challenge documents.
- [UN Sustainable Development Goal 2](https://sdgs.un.org/goals/goal2) - global goal context for ending hunger and improving food systems.
- [FAO food security concept note](https://www.fao.org/docrep/013/al936e/al936e00.pdf) - a clear explanation of food security and its dimensions.
- [World Bank food security explainer](https://www.worldbank.org/en/topic/agriculture/brief/food-security-update/what-is-food-security) - another clear reference for availability, access, utilization, and stability.
- [FAO SOFI 2025 newsroom summary](https://www.fao.org/newsroom/detail/global-hunger-declines--but-rises-in-africa-and-western-asia--un-report/en) - current global hunger and food insecurity data.
- [UNEP Food Waste Index Report 2024](https://www.unep.org/resources/publication/food-waste-index-report-2024) - current global food waste data.

## The One-Minute Idea
A meal is the end of a long journey. Someone had to grow ingredients, harvest them, keep them safe, move them, sell or prepare them, and avoid wasting them.

When one part of that journey breaks, people may not get enough safe and healthy food. Robots can help in some parts, but only if we understand the whole system first.

Simple idea: Mission Meals asks you to think like a food detective and a robot engineer at the same time. First ask, "What food problem is happening?" Then ask, "What small job could a robot do to help this part of the problem?"

## Past, Present, Future

### Past
For most of human history, people found food by hunting, gathering, fishing, or farming near where they lived. Food was very local, and bad weather could quickly become a hunger problem. A flood, drought, pest attack, war, or storage failure could affect an entire community.

As farming improved, people learned to store grain, irrigate fields, use animals for work, preserve food, and trade food over longer distances. Grain stores were important because grains such as rice, wheat, barley, and maize could be dried and kept for months. Preservation methods such as drying, salting, smoking, pickling, and fermenting helped people keep food usable before modern refrigeration.

Food systems became bigger when people built towns, roads, markets, ports, and rules for trade. The bigger system solved some problems: people could get more kinds of food and move food from surplus areas to shortage areas. But bigger systems also created new risks: a city could depend on distant farms, transport routes, and storage systems that ordinary people could not see.

### Present
Today, food systems are global. Singapore imports most of its food, and a meal in Singapore may depend on farmers, ports, cold rooms, ships, trucks, supermarkets, digital tracking, food inspectors, and consumers. The same meal may include rice from one country, vegetables from another, fish from another, and seasoning from several more.

The modern world can produce and move large amounts of food, but serious problems remain. [SOFI 2025](https://www.fao.org/newsroom/detail/global-hunger-declines--but-rises-in-africa-and-western-asia--un-report/en) estimates that about 673 million people experienced hunger in 2024, and about 2.3 billion people experienced moderate or severe food insecurity. At the same time, [UNEP's Food Waste Index Report 2024](https://www.unep.org/resources/publication/food-waste-index-report-2024) estimates that 1.05 billion tonnes of food waste were generated in 2022 at retail, food service, and household levels.

Those two facts belong together. The problem is not only "grow more." It is also "grow the right foods," "move food safely," "keep food affordable," "protect nutrition," "reduce waste," and "make the system strong when shocks happen."

### Future
Future food systems may use more indoor farms, climate-controlled greenhouses, fish farms, robots, sensors, data platforms, alternative proteins, food waste recovery, disease monitoring, and climate-resilient crops. Some farms may look like fields. Some may look like buildings. Some future foods may be made with fermentation, plant proteins, algae, insects, or cultivated animal cells.

But technology will not automatically solve everything. A tool can be clever but too expensive. A robot can be fast but unsafe near people. An indoor farm can save land but use a lot of electricity. A data system can be powerful but wrong if the sensors are poorly placed. A new food can be promising but must be tested for safety and accepted by people.

So the future question is not "Can we invent something cool?" The better question is: "Can we design a food system that is safe, nutritious, affordable, resilient, and fair?" Mission Meals is a small robotics version of that big design question.

## Deep Explanation

### 1. Food Is A System, Not A Single Object
Think about a bowl of noodles. The noodles may come from wheat or rice. The vegetables need seeds, water, nutrients, light, labour, and pest control. The eggs may come from a farm that needs feed, temperature control, animal health care, and food safety rules. The meal also needs packaging, transport, cooking, refrigeration, washing, and waste handling.

A food system includes living things and non-living things. Living things include plants, animals, fungi, microbes, farmers, workers, drivers, cooks, sellers, and families. Non-living things include soil, water, fertilizer, machines, roads, ships, sensors, packaging, electricity, cold rooms, money, and data.

Think of it this way: a food system is like a giant team. Some team members grow food. Some protect food. Some carry food. Some check food. Some cook food. Some clean up after food. If one team member stops doing the job, the meal can be late, unsafe, too expensive, or wasted.

### 2. A Food Chain Is Too Simple; A Food Web Is Closer
People often say "farm to table," which sounds like a straight line. Real food systems are more like a web. A farm needs seeds from somewhere, fertilizer or nutrients from somewhere, water from somewhere, energy from somewhere, and workers or machines. A supermarket needs suppliers, transport, cooling, shelves, payment systems, and customers. A family needs money, time, cooking skills, and safe storage.

Here is a simple chain:

```text
farm -> truck -> warehouse -> shop -> home -> meal
```

Here is a more realistic system map:

```text
sunlight + water + seeds + nutrients + labour + machines
-> production
-> harvest
-> processing and packing
-> storage and cold chain
-> transport and ports
-> retail or food service
-> cooking and eating
-> leftovers, rescue, compost, or waste
```

A robot mission usually models one tiny part of this bigger map. If your robot moves a crate, it may represent logistics. If it sorts a food piece, it may represent quality control or waste recovery. If it lifts a tray, it may represent production infrastructure.

### 3. Food Security Has Four Main Dimensions
Food security means people can reliably get enough safe and nutritious food for a healthy life. The classic food security dimensions are explained by FAO and the World Bank: availability, access, utilization, and stability.

Availability asks: Is there enough food? This depends on production, imports, storage, and stocks. A farm robot can help availability if it improves harvesting, planting, watering, monitoring, or sorting.

Access asks: Can people actually get the food? Food can exist in a warehouse, but a family may still not be able to buy it or reach it. Access depends on income, prices, roads, shops, transport, safety, and fairness.

Utilization asks: Is the food safe and nutritious, and can the body use it well? This includes food safety, clean water, cooking, balanced diets, vitamins, minerals, protein, fibre, and health.

Stability asks: Can people keep getting food over time, even during shocks? A system can look fine on a normal day but fail during a flood, heat wave, disease outbreak, shipping delay, conflict, or price spike.

In simple words: food security means food must be there, people must be able to get it, it must be good for the body, and it must keep coming even when things go wrong.

### 4. Modern Food Problems Often Have More Than One Cause
A food problem is rarely caused by only one thing. Hunger can happen because crops failed, but also because people lost income, food prices rose, roads were blocked, conflict made farming dangerous, or food was not shared fairly. Food waste can happen because people bought too much, labels were confusing, storage failed, shops rejected imperfect food, or transport was delayed.

This matters for robotics because a robot usually helps with a specific cause. A robot can help move crates, but it cannot by itself change food prices. A robot can sort ripe fruit, but it cannot by itself make healthy diets affordable. A robot can inspect plants, but it cannot by itself solve drought. Good engineers understand both what their tool can do and what it cannot do.

A useful question is: "Where is the bottleneck?" A bottleneck is the part that slows or limits the whole system. If crops are growing well but transport is broken, then production is not the bottleneck. If transport is fast but food is unsafe, then safety control may be the bottleneck. If food is safe and available but too expensive, then access is the bottleneck.

### 5. Mission Meals Maps To Four Robot Ideas
The reference research for this project maps Mission Meals into four useful challenge areas.

Food Production Infrastructure is about systems that help food grow. Examples include greenhouses, hydroponics, farm trays, irrigation, lights, pumps, sensors, and controlled environments. A competition mission might model moving a plant tray, placing a resource, checking a marker, or activating a production station.

Labour-Intensive Farming is about tasks that require repeated human effort. Examples include planting, weeding, harvesting, sorting, carrying, washing, or inspecting. A competition mission might model reducing tiring or repetitive work.

Food Logistics is about storage, routing, cooling, delivery, traceability, and movement. A competition mission might model delivering a crate, docking at a warehouse, moving food to a correct zone, or keeping products separated.

End-Effector Design is about the robot's tool. The end-effector might be a gripper, hook, scoop, pusher, lifter, sweeper, clamp, fork, or modular attachment. In a food system, the tool must match the object. A strawberry needs a gentle tool. A crate may need a strong tool. A tray may need a wide support.

### 6. A System Has Inputs, Outputs, Feedback, And Tradeoffs
An input is something the system uses. A farm uses seeds, water, nutrients, energy, labour, knowledge, and money. A logistics system uses vehicles, fuel, time, cold storage, route plans, workers, and information.

An output is what the system produces. A farm produces food, but also plant waste, used water, emissions, and data. A warehouse delivers food, but also uses energy and packaging.

Feedback is information that changes what the system does next. A soil moisture sensor can tell a pump to turn on. A temperature sensor can warn that the cold chain is too warm. A sales record can tell a shop to order fewer bananas tomorrow.

A tradeoff is a choice where improving one thing can make another thing harder. Indoor farms can save land, but they may use more electricity. Buying food from many countries can improve resilience, but it can make tracking more complicated. Automation can reduce tiring work, but it can be expensive and require repair skills.

### 7. Past, Present, And Future All Help You Think Clearly
A strong Mission Meals explanation should not only describe today's technology. It should include time.

Past thinking asks: How did people solve this problem before? For example, before refrigeration, people dried, salted, fermented, or smoked food. Before sensors, farmers used sight, touch, smell, and experience.

Present thinking asks: What are people doing now, and what data shows the problem? For example, current reports show hunger, food insecurity, waste, and climate risks at global scale.

Future thinking asks: What might change, and what are people still researching? For example, researchers are working on better plant lighting recipes, lower-energy vertical farms, robotic harvesting, climate-resilient crops, traceability systems, and alternative proteins.

When you include all three, your robot story becomes deeper. You can say: "People used to solve this with human labour. Today the problem is still hard because of speed, safety, or cost. In the future, robots and sensors may help if they are reliable and affordable."

### 8. Four Mini Food-System Stories
Story 1: A lettuce tray in a vertical farm. The plant needs light, water, nutrients, air, space, and temperature control. A robot might move trays, read color markers, or deliver supplies. The real science is plant growth and controlled environment agriculture.

Story 2: A fish product in a cold chain. The fish must be kept at a safe temperature, tracked, transported, and sold before it spoils. A robot might move cold boxes or sort packages. The real science is food safety, temperature, microbes, and logistics.

Story 3: A crate of mixed produce after harvest. Some items are ripe, some damaged, and some still usable for rescue or processing. A robot might sort by color or location. The real science is quality control, food loss, and waste prevention.

Story 4: A future protein product. It may be plant-based, fermented, insect-based, algae-based, or cultivated. A robot might model safe handling or production steps. The real science is nutrition, safety, regulation, and public acceptance.

### 9. What A Robot Can And Cannot Represent
A small competition robot is not a real farm robot, warehouse robot, or food safety laboratory. But it can represent important ideas.

It can represent sensing: detecting color, position, distance, touch, angle, or time. It can represent movement: carrying, pushing, lifting, turning, docking, or following a path. It can represent decision-making: if the object is red, sort it one way; if it is blue, sort it another way. It can represent reliability: doing the same action correctly many times.

It cannot represent everything. It cannot show the full economics of food prices, the real biology of a plant disease, or the full safety testing of novel foods. That is okay. The goal is to model one meaningful part clearly and honestly.

### 10. How To Read A Food Problem Like An Engineer
When you read a food-system problem, use this checklist:

1. What food or resource is involved?
2. Where is it in the system: production, processing, logistics, eating, or waste recovery?
3. What is the problem: not enough, too expensive, unsafe, too slow, too much waste, too much labour, or too fragile?
4. What science explains the problem?
5. What object, marker, or model could represent it on a robotics field?
6. What robot action could help: sense, move, sort, lift, push, deliver, activate, or record?
7. What evidence would show the robot is reliable?

This checklist will appear in different forms across the course. By Week 16, you should be able to use it almost automatically.


## Expanded Knowledge Notes

### Food-System Layer 1: Production
Production is the part of the system where food is grown, raised, caught, or made. It includes crop farming, livestock farming, aquaculture, fishing, mushroom growing, and some newer production methods such as fermentation and cultivated foods.

Crop production depends on plant biology. A crop needs light, water, carbon dioxide, nutrients, a suitable temperature, and protection from pests and disease. Livestock production depends on animal health, feed, water, shelter, space, disease control, and safe handling. Aquaculture depends on water quality, oxygen, feed, stocking density, and disease management.

Production is not only a farm problem. It connects to land use, climate, energy, water, labour, money, equipment, seeds, feed, fertilizer, and markets. A farmer may know how to grow a crop, but still face high electricity prices, worker shortages, pest outbreaks, or low selling prices.

In Mission Meals, production can be represented by a plant tray, farm station, water station, nutrient station, greenhouse, fish tank, egg collection point, or inspection marker. A robot production mission should ask: What living process are we helping? Are we moving a resource, checking a condition, or reducing repetitive labour?

### Food-System Layer 2: Processing And Food Safety
Processing means changing raw food into a form that is easier to store, transport, cook, or eat. Wheat becomes flour. Milk becomes cheese or yoghurt. Fish may be cleaned, chilled, packed, and labelled. Vegetables may be washed, cut, frozen, or packed.

Processing can make food safer and more useful, but it must be controlled. Food safety includes preventing harmful microbes, chemical hazards, allergens, and physical hazards such as metal or glass. A food safety system often uses cleaning, temperature control, separation of raw and cooked foods, testing, labels, and traceability.

Food safety is part of food security because unsafe food cannot truly nourish people. If a food causes illness, the system failed even if the food was available and affordable.

For a robotics model, processing might become sorting, washing, scanning, separating, or moving products through stations. The robot should act accurately because a wrong item in the wrong place can represent a real safety problem.

### Food-System Layer 3: Logistics And Cold Chain
Logistics is the planned movement of goods, information, and resources. Food logistics includes trucks, ships, planes, ports, warehouses, delivery workers, route planning, storage, packaging, inventory, and records.

Some foods need a cold chain. A cold chain is a temperature-controlled system from production to consumption. Meat, seafood, dairy, many fresh foods, and frozen foods can spoil or become unsafe if temperature is not controlled. A broken cold chain can waste food and create health risks.

[FAO's traceability and recalls page](https://www.fao.org/food-safety/food-control-systems/supply-chains-and-consumers/traceability-and-recalls/en/) explains traceability as following food through production, processing, and distribution stages. Traceability matters because if something goes wrong, people need to know which batch is affected and where it went.

In a competition robot, logistics can become path planning, loading, unloading, docking, route choice, sorting by destination, or carrying items without dropping them. The robot does not need to be fast only. It needs to be accurate and reliable.

### Food-System Layer 4: Markets, Homes, And Eating
Food does not finish its journey when it reaches a shop. People must choose, buy, store, cook, share, and eat it. This part includes culture, price, taste, family habits, cooking equipment, time, nutrition knowledge, and food safety at home.

A healthy meal is not only a full meal. It should include useful nutrients and be safe to eat. For example, a meal with only sugary drinks and snacks may provide energy but not enough protein, fibre, vitamins, or minerals.

This matters for Mission Meals because the word "meals" points to people, not only products. A robot can model movement and sorting, but the reason behind the mission is that real people need meals that support life and health.

### Food-System Layer 5: Loss, Waste, And Recovery
Food loss often means food that leaves the human food supply before retail or consumer stages, such as loss during harvest, storage, or transport. Food waste often means food wasted by retailers, restaurants, and households. The exact definitions can vary by organization, but the idea is that edible resources are lost at different points.

[UNEP's Food Waste Index Report 2024](https://www.unep.org/resources/publication/food-waste-index-report-2024) focuses on waste at retail, food service, and household levels. It reminds us that food waste is not only wasted food. It is also wasted land, water, labour, energy, packaging, money, and emissions.

Recovery can include prevention, donation of safe edible surplus, upcycling, animal feed where safe and allowed, composting, and anaerobic digestion. Prevention usually comes first because it avoids using resources for food that nobody eats.

A robot model could sort edible and inedible items, deliver rescued food, move compost resources, or track waste amounts. The science idea is resource efficiency: use what we already produce more wisely.

### System Thinking Tool: Cause, Effect, And Feedback
A cause makes something happen. An effect is what happens because of a cause. In food systems, one cause can have many effects.

Example:

```text
heat wave
-> lower crop yield
-> less supply
-> higher prices
-> families buy cheaper food
-> diet quality may drop
```

Feedback happens when the result changes the next action. If a store sees many vegetables going unsold, it may order fewer next time. If a farm sensor detects dry soil, it may start irrigation. If prices rise, consumers may change what they buy.

Feedback can be helpful or harmful. Helpful feedback corrects a problem early. Harmful feedback can make a problem worse, such as panic buying causing empty shelves, which causes more panic buying.

### System Thinking Tool: Scale
Scale means size or level. A food problem can happen at many scales:

- plant scale: a leaf lacks nutrients,
- farm scale: a pump fails,
- city scale: delivery routes are disrupted,
- country scale: import supply changes,
- global scale: grain prices rise.

A student robot works at a tiny model scale, but the idea it represents can belong to a much larger scale. A small blue block might represent a cold box. A short route on the mat might represent a supply chain. A color marker might represent a safety label.

Good explanations clearly say which scale is real and which scale is modelled.

### System Thinking Tool: Evidence
Evidence is information that supports a claim. In food systems, evidence can include sensor readings, crop yields, price data, nutrition surveys, safety test results, delivery times, and waste measurements. In robotics, evidence can include run results, timing, number of successful deliveries, number of dropped objects, and notes about failure modes.

A strong Mission Meals team should avoid saying "our robot helps food security" without proof. A better claim is: "Our model represents food logistics. The robot delivered the crate to the correct zone in 8 out of 10 trials. This shows how reliable handling matters in supply chains."

### Common Misunderstandings To Avoid
Misunderstanding 1: Food security only means growing more food. Better thinking: food security also includes access, utilization, and stability.

Misunderstanding 2: Technology always makes a system better. Better thinking: technology has costs, maintenance needs, energy needs, and tradeoffs.

Misunderstanding 3: Local food is always better. Better thinking: local production can improve resilience, but it must be safe, affordable, resource-efficient, and suitable for the place.

Misunderstanding 4: Waste is only a consumer problem. Better thinking: waste and loss can happen during production, storage, transport, retail, food service, and at home.

Misunderstanding 5: A robot has to solve the whole problem. Better thinking: a robot should solve or model one clear part of the problem well.


## Additional Guided Reading: How To Connect Every Later Week Back To This Map

### Week 2 Connection: Singapore Is A Local Example Of A Global System
When you study Singapore's food story, remember the four food-security dimensions from this week. Import diversification supports availability and stability. Stockpiling supports stability. Growing local supports availability and resilience for selected foods. Food safety supports utilization. Affordability and consumer trust affect access.

Singapore is not a separate topic from Mission Meals. It is a real-world example of a dense city designing a food system under constraints. When you later design a robot mission, you can ask whether the mission represents production, logistics, safety, waste recovery, or resilience.

### Week 3 Connection: Agriculture History Is A History Of System Upgrades
Domestication, irrigation, storage, crop rotation, mechanization, fertilizer, and improved seeds were all upgrades to food systems. Each one changed inputs, outputs, labour, and risk. Robots are another possible upgrade, but they should be judged the same way: What problem do they solve? What new dependency do they create? Who can use them? What happens when they fail?

### Week 4 Connection: Hunger Data Explains Why The Theme Matters
Global hunger and food insecurity data show why food-system design matters. The [SOFI 2025 summary](https://www.fao.org/newsroom/detail/global-hunger-declines--but-rises-in-africa-and-western-asia--un-report/en) is not just a list of numbers. It is evidence that food systems still fail many people. Your robot model is small, but the theme is serious.

### Week 5 And 6 Connection: Plants Are Living Systems Inside Food Systems
When you study photosynthesis, hydroponics, and controlled environment agriculture, connect the science back to food production infrastructure. A plant tray on a competition mat is not just a prop. It represents biology supported by engineering: light, water, nutrients, airflow, temperature, and monitoring.

### Week 7 And 8 Connection: Data And Labour Shape Modern Farming
Precision agriculture uses data to decide where to act. Agricultural robots use sensing, movement, and tools to reduce repetitive or difficult labour. Both are examples of feedback loops. The system observes, decides, acts, and observes again.

### Week 9 And 10 Connection: Tools And Logistics Turn Ideas Into Movement
An end-effector is the part of the robot that touches the world. Logistics is the part of the food system that moves the world. These two topics connect strongly. If food must move safely, the tool must hold it correctly, the route must be planned, and the release must be reliable.

### Week 11 And 12 Connection: Waste And Climate Show Why Efficiency Is Not Enough
A system can produce a lot and still waste too much. A system can be efficient on normal days and still fail during heat, floods, drought, or disease. Food-system thinking must include waste prevention and climate resilience, not only output.

### Week 13 Connection: Future Foods Need Safety And Trust
Alternative proteins, fermentation, cultivated foods, insects, and algae are possible future directions. They connect to food security because they may change land use, protein supply, and production systems. But new foods also need safety assessment, clear labels, affordability, and public acceptance.

### Week 14 And 15 Connection: Programs And Tests Create Reliable Action
A food system needs evidence, and a robot system needs evidence. In programming, a sequence, loop, condition, variable, or state is useful only if it makes the robot act more reliably. In testing, one lucky run is not enough. Reliability is part of responsible engineering.

### Week 16 Connection: Your Capstone Is A Translation
By the final week, you should be able to translate:

```text
food-system problem -> science idea -> mission model -> robot mechanism -> program logic -> test evidence -> future improvement
```

This translation is the heart of Mission Meals. If you can explain that chain clearly, you are not only building a robot. You are showing that you understand why the robot matters.


## Extra Framework Notes: Seven Questions For Any Food-System Robot

### 1. What Is The Real Object?
A competition object is usually a model. A block may represent a crate, a plant tray, a fish box, a waste item, a nutrient packet, or a food order. Before designing the robot, name the real object. Real objects have properties: mass, size, shape, fragility, temperature needs, safety rules, and labels.

If the real object is fragile, your model should inspire gentle handling. If the real object needs cooling, your model should inspire careful timing and correct destination. If the real object is waste, your model should inspire sorting and recovery.

### 2. What Is The Real Location?
Food changes meaning depending on where it is. A tomato on a plant is a crop. A tomato in a crate is a harvested product. A tomato in a kitchen is an ingredient. A spoiled tomato in a bin is waste or compost material.

Robot missions also use locations: farm zone, warehouse zone, market zone, rescue zone, compost zone, or inspection zone. Naming the location helps you explain the mission more clearly.

### 3. What Is The Real Risk?
A risk is something that could go wrong. Food-system risks include spoilage, contamination, delay, breakage, shortage, high price, wrong label, pest damage, heat stress, water shortage, or waste.

A robot mission becomes stronger when it models a risk. For example, sorting unsafe food away from safe food is clearer than simply moving a random object.

### 4. What Is The Real Constraint?
A constraint is a limit. Food systems have constraints such as land, water, labour, energy, money, safety, time, weather, and public trust. Robots have constraints such as motors, sensors, size, battery, field rules, and time.

Good design respects constraints. If your robot has only one motor left for an attachment, design a simple tool. If a real farm has limited labour, design an action that reduces repetitive work.

### 5. What Is The Real Feedback?
Feedback tells the system what happened. A farmer may use a soil sensor. A warehouse may use an inventory scan. A family may check a use-by date. Your robot may use a color sensor, motor rotation, distance reading, or test table.

A mission without feedback can still work, but feedback helps reliability. It helps the system notice errors.

### 6. What Is The Real Tradeoff?
Every serious solution has tradeoffs. More speed can reduce accuracy. Stronger grip can damage fragile items. More sensors can improve decisions but make coding harder. More local production can improve resilience but use land, energy, or money.

When you mention tradeoffs, your explanation becomes more mature.

### 7. What Is The Evidence?
Evidence turns an idea into an engineering claim. If your robot says it delivers food reliably, test it. Count successful runs. Record failures. Change one variable at a time. Use evidence to decide what to improve.

Food-system experts also need evidence. They use reports, surveys, sensor readings, lab tests, maps, and price data. Mission Meals teaches the same habit at a smaller scale.

### A Simple Full Example
Real problem: Fresh vegetables can be damaged or delayed before reaching people.

System part: Local production and food logistics.

Robot model: A robot moves a plant tray from a farm zone to a market zone without dropping it.

Science idea: Fresh produce is fragile and needs careful handling.

Robot mechanism: A wide tray support spreads force and reduces tipping.

Program idea: Move slowly during carrying, turn gently, and align before release.

Evidence: The robot completes 9 out of 10 deliveries without dropping the tray.

Future improvement: Add a guide rail or sensor check to reduce the one failed run.

This example is simple, but it contains the whole Mission Meals thinking chain.


## Final Framework Reminder: The Small Model And The Big World

A robotics field is small on purpose. It lets you practise a big idea safely. The mat is not a real farm, port, warehouse, or kitchen. The mission models are not real food. But the thinking can still be real.

When you look at a mission model, train yourself to ask two questions at the same time. First: What does the robot physically need to do on this field? Second: What real food-system idea does this action represent? If you only answer the first question, you may build a working robot but give a weak explanation. If you only answer the second question, you may understand the theme but fail the mission. NRC needs both.

A strong student explanation can be short but complete: "This mission represents food logistics. The robot moves a crate from storage to delivery. In real food systems, accurate delivery helps access and reduces waste. Our test evidence shows the robot completed the delivery 9 out of 10 times."

That kind of explanation is the goal of the whole course.


One last way to test your thinking is to remove the robot for a moment. If the mission still describes a meaningful food-system action, your idea is strong. If the mission only sounds like "move the red block because the rule says so," your explanation needs more work. The robot should perform the rule, but your mind should understand the reason behind the rule.


A useful notebook sentence is: "My robot action is small, but it represents a real system function." Then name the function: production, inspection, storage, cold-chain delivery, traceability, rescue, composting, or emergency supply. This one sentence keeps your robot work connected to the science.


If you can name both the system function and the evidence, your explanation is already much stronger than saying only that the robot scores points.


Keep this habit all season during every practice.

## Core Terms

### Food System
All the people, living things, tools, places, energy, data, and rules that move food from production to eating and waste handling.

Simple version: the food system is the whole journey of food.

### Food Security
The condition where people can reliably get enough safe and nutritious food.

Simple version: people have the food they need, not just once, but again and again.

### Availability
The amount of food that exists in a place. Availability depends on farms, imports, stocks, and storage.

### Access
Whether people can actually get the food. Money, distance, transport, safety, and fairness matter here.

### Utilization
Whether the food is safe, nutritious, and useful for the body.

### Stability
Whether the system keeps working during shocks such as heat waves, disease outbreaks, wars, floods, or shipping delays.

### Food Supply Chain
The movement of food and information from producers to consumers. It includes production, processing, storage, transport, retail, and sometimes waste recovery.

### Resilience
The ability to keep working, recover, or adapt when something goes wrong.

### Bottleneck
The slow or weak part that limits the whole system. If one narrow door slows a whole class, the door is the bottleneck.

### Feedback Loop
Information that changes what happens next. A sensor reading can become a feedback loop if it tells a machine to turn on, slow down, stop, or warn people.

### Shock
A sudden event that stresses the system, such as a drought, flood, disease outbreak, conflict, price spike, or shipping delay.

### Tradeoff
A choice where improving one thing may make another thing harder.

### Mission Abstraction
Changing a real-world problem into a smaller task a robot can do.

Example: "food must stay cold" becomes "robot carries a cold box to the correct station."

## Student Thinking Tasks

1. Choose one food you ate this week. Draw its possible food-system journey with at least six steps.
2. Mark each step as production, logistics, safety, eating, or waste handling.
3. Choose one weak point in the journey. Explain whether it is about availability, access, utilization, or stability.
4. Design one tiny robot mission that represents that weak point.
5. Write one sentence that connects the robot action back to the food-system problem.

## Sources For Further Reading
- Science Centre Singapore NRC page: https://www.science.edu.sg/for-schools/competitions/national-robotics-competition
- UN Sustainable Development Goal 2: https://sdgs.un.org/goals/goal2
- FAO food security concept note: https://www.fao.org/docrep/013/al936e/al936e00.pdf
- World Bank food security explainer: https://www.worldbank.org/en/topic/agriculture/brief/food-security-update/what-is-food-security
- FAO SOFI 2025 newsroom summary: https://www.fao.org/newsroom/detail/global-hunger-declines--but-rises-in-africa-and-western-asia--un-report/en
- UNEP Food Waste Index Report 2024: https://www.unep.org/resources/publication/food-waste-index-report-2024
- FAO food systems resources: https://www.fao.org/food-systems/en/
