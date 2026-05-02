# W05 Science - Plant Growth Science: Light, Water, Soil, And Nutrients

This student document contains the science and food-system knowledge for the week. For robot building and programming work, see `robotics.md`.

## Big Question
What does a plant need to grow food, and why do farmers care so much about light, water, and nutrients?

## Why This Week Matters
Food Production Infrastructure missions are about helping food grow. To understand those missions, you need to understand the living system inside a plant.

A robot that checks a farm, moves a plant tray, turns on a light, or delivers water is supporting a biological process. The robot is not growing the plant by magic. It is helping control the conditions that let the plant grow.

This week is the biology foundation for later weeks on controlled environment agriculture, vertical farms, precision sensors, and farm robots. If you know what a plant needs, you can design better robot missions around production, inspection, watering, sorting, and tray movement.

## Key Reference Links For This Week
Use these links when you want stronger background:

- [NASA Growing Plants in Space](https://www.nasa.gov/exploration-research-and-technology/growing-plants-in-space/) - explains plant growth systems using LED lights, water, nutrients, and root support.
- [NASA Plant Biology Program](https://science.nasa.gov/biological-physical/focus-areas/plant-biology/focus-areas/) - shows why controlled plant growth matters in space and on Earth.
- [NASA plant hardware](https://science.nasa.gov/biological-physical/focus-areas/plant-biology/hardware/) - reference for growth chambers, LED spectra, and plant research hardware.
- [USDA National Agricultural Library hydroponics](https://www.nal.usda.gov/farms-and-agricultural-production-systems/hydroponics) - background on growing plants without soil.
- [NASA photosynthesis from space](https://www.nasa.gov/earth-and-climate/seeing-photosynthesis-from-space-nasa-scientists-use-satellites-to-measure-plant-health/) - explains how scientists can detect plant photosynthesis signals remotely.
- [USDA agriculture technology topics](https://www.nifa.usda.gov/topics/agriculture-technology) - wider context for technology in agriculture.

## The One-Minute Idea
Plants make sugar through photosynthesis. They need light energy, carbon dioxide, water, and nutrients. They also need the right temperature, enough space, oxygen around roots, and protection from stress. Different farming systems control these needs in different ways.

Think of a plant as a tiny food factory. Light is energy, water is a material, air gives carbon dioxide, and nutrients are building blocks. Farmers and robots help by keeping the factory supplied and safe day by day.

## Past, Present, Future

### Past
Early farmers learned from observation. They noticed that crops grew better in certain soils, seasons, and watering patterns. They did not know the chemistry of photosynthesis, but they knew that sun, water, soil, and timing mattered.

Farmers also learned that plants could be stressed. A crop might fail if rain did not come, if soil was poor, if insects attacked, or if the season was wrong. Before modern instruments, people used their senses: leaf colour, plant height, soil feel, smell, weather signs, and memory.

### Present
Today, scientists can measure light intensity, light spectrum, soil moisture, nutrient levels, pH, electrical conductivity, temperature, humidity, carbon dioxide, plant colour, and plant stress. Farmers can use soil tests, hydroponic nutrient solutions, greenhouse sensors, LED lights, irrigation controllers, and cameras to control plant growth more precisely.

Modern plant science also looks at the inside of plants: cells, chloroplasts, stomata, hormones, roots, microbes, genes, and stress responses. A farm can now be partly a biology lab, partly an engineering system, and partly a business.

### Future
Future plant production may use smarter lighting recipes, water recycling, plant stress sensors, AI crop models, climate-resilient varieties, biological pest control, nutrient recovery, and robots that inspect individual plants. Space research also pushes plant science forward because astronauts need fresh food in controlled environments.

The challenge is to grow more nutritious food while using less land, water, energy, and chemicals. A future farm will need good biology and good engineering at the same time.

## Deep Explanation

### 1. Photosynthesis Is The Plant's Food-Making Process
Photosynthesis happens mainly in leaves. Inside many leaf cells are chloroplasts. Chloroplasts contain chlorophyll, a green pigment that captures light energy. The plant uses that energy to combine carbon dioxide from air and water from roots into sugars.

The simple classroom idea is:

```text
light + carbon dioxide + water -> sugar + oxygen
```

The more scientific version is:

```text
6 CO2 + 6 H2O + light energy -> C6H12O6 + 6 O2
```

You do not need to memorize the chemical formula, but it shows that photosynthesis rearranges atoms. Carbon dioxide and water become sugar and oxygen. The sugar becomes energy and building material for the plant. It helps make stems, roots, leaves, flowers, fruits, and seeds.

Photosynthesis is why plant production is connected to light, air, water, nutrients, and temperature. If any important condition is too low or too high, growth can slow.

### 2. Leaves Are Solar Panels, Factories, And Breathing Surfaces
A leaf is not just a flat green shape. It has jobs.

A leaf captures light like a solar panel. It makes sugars like a factory. It exchanges gases through tiny openings called stomata. Carbon dioxide enters through stomata. Oxygen and water vapour leave.

Stomata can open and close. When stomata open, the plant can take in carbon dioxide, but it can also lose water. When stomata close, the plant saves water, but photosynthesis can slow because less carbon dioxide enters.

This creates a tradeoff: plants need gas exchange, but they must avoid drying out. Hot, dry weather makes this tradeoff harder. This is why farmers care about humidity, temperature, irrigation, and shade.

### 3. Light Has Colour, Intensity, And Time
Light is made of different wavelengths. Humans see many wavelengths as colours. Plants use some wavelengths strongly for photosynthesis, especially red and blue light, but plants also respond to green, far-red, and other wavelengths for shape, timing, and stress signals.

Intensity means how much light reaches the plant. Too little light can slow growth. Too much light can stress plants, especially if water or temperature is not right.

Time matters too. Photoperiod means the length of light and dark periods. Some plants use day length as a signal for flowering. Daily light integral, often called DLI, means the total useful light a plant receives in a day. Indoor farms care about DLI because lights cost energy.

This is why vertical farms and greenhouses may use LED lights. LEDs can be tuned so plants receive useful light. But lights need electricity, so energy cost is a serious tradeoff.

### 4. Water Is A Material, A Transport System, And A Cooling Tool
Water does not only stop plants from drying out. It is one of the raw materials for photosynthesis. It also carries dissolved nutrients from roots into the plant. Water helps cells stay firm. It helps cool leaves when water evaporates through transpiration.

Transpiration is the movement of water through a plant and out through leaves as water vapour. It helps pull water upward from roots through xylem, which is plant tissue that transports water and minerals.

If a plant lacks water, leaves may wilt, stomata may close, photosynthesis may slow, and growth may stop. If a plant has too much water around roots, roots may lack oxygen and become unhealthy. Good watering means the right amount at the right time, not just "more water."

### 5. Roots Need Water, Nutrients, Oxygen, And Space
Roots anchor the plant and absorb water and nutrients. They also need oxygen for respiration. Respiration is how living cells release energy from sugars. Plant roots are alive, so they need oxygen even though they are underground or in water systems.

This is why soil structure matters. Soil must hold water but also have air spaces. In hydroponics, water must often be aerated or circulated so roots get oxygen.

Root hairs increase surface area. Surface area is how much outside contact a shape has. More surface area helps roots absorb more water and nutrients.

A robot that moves plant trays should remember that the visible leaves are only part of the plant. The root zone is also critical.

### 6. Nutrients Are Plant Building Blocks
Plants need many nutrients. The big macronutrients include nitrogen, phosphorus, and potassium. Farmers often call them N, P, and K.

Nitrogen helps plants make proteins and chlorophyll. A nitrogen shortage can make leaves pale or yellow.

Phosphorus helps with energy transfer, roots, and flowering.

Potassium helps water regulation, enzymes, and stress tolerance.

Plants also need calcium, magnesium, sulfur, iron, manganese, zinc, copper, boron, molybdenum, chlorine, and nickel in smaller amounts. Small amount does not mean unimportant. A tiny missing nutrient can still limit growth.

This connects to Liebig's law of the minimum: plant growth can be limited by the scarcest necessary resource. If a plant has enough light and water but lacks one key nutrient, growth can still be limited.

### 7. Soil Is More Than Dirt
Soil can hold water, air, minerals, organic matter, microbes, and roots. Healthy soil is a living system. It includes bacteria, fungi, insects, worms, and other organisms that help break down organic matter and cycle nutrients.

Soil texture describes the mix of sand, silt, and clay. Sandy soil drains quickly but may hold fewer nutrients. Clay soil can hold nutrients and water but may drain poorly. Loam is a balanced mixture often good for many crops.

Soil organic matter improves structure, water holding, nutrient cycling, and microbial life. Soil pH affects which nutrients are available to plants.

Some modern farms grow plants without soil, but they must still provide the jobs soil usually does: water, nutrients, oxygen, root support, and microbial balance where relevant.

### 8. Hydroponics Replaces Soil With A Nutrient Solution
Hydroponics means growing plants with roots in water or another support material while nutrients are dissolved in the water. [USDA's hydroponics reference](https://www.nal.usda.gov/farms-and-agricultural-production-systems/hydroponics) gives historical and practical background on soil-less plant growth.

Hydroponics can save space and water, and it can be used indoors. It lets farmers control nutrient concentration and pH carefully. But it needs monitoring. If pumps fail, roots can dry or lose oxygen. If nutrient balance is wrong, plants can suffer quickly. If disease enters the water system, it can spread.

Important hydroponic measurements include pH and electrical conductivity. pH measures acidity or alkalinity. Electrical conductivity, often called EC, estimates how many dissolved ions are in the nutrient solution. Too low EC may mean too few nutrients. Too high EC can stress roots.

### 9. Plant Stress Has Signals
Plants cannot speak, but they show stress. Leaves may yellow, curl, wilt, develop spots, become purple, grow slowly, or drop. Roots may become brown or slimy. Stems may stretch if light is weak. Flowers or fruit may fail if temperature, water, or nutrients are wrong.

Some plant stress is visible to human eyes. Some can be detected earlier with sensors. Cameras can measure colour. Multispectral sensors can see wavelengths beyond human vision. Thermal cameras can detect leaf temperature. Scientists can even study plant fluorescence, as described by [NASA's photosynthesis-from-space article](https://www.nasa.gov/earth-and-climate/seeing-photosynthesis-from-space-nasa-scientists-use-satellites-to-measure-plant-health/).

For Mission Meals, a colour sensor or marker can model plant health information. The key idea is that sensing helps people act before the problem becomes severe.

### 10. The Limiting Factor Idea Helps Robot Design
A limiting factor is the resource or condition that most limits growth. Imagine a plant has enough light, water, and nitrogen, but the pH is wrong. The plant may still fail to absorb nutrients well. The pH becomes the limiting factor.

Farmers and scientists try to identify the limiting factor before acting. Otherwise they may waste effort. Adding more water does not fix a light problem. Adding more light does not fix a root oxygen problem. Adding more fertilizer does not fix a pest problem.

Robotics has limiting factors too. If your robot misses because its attachment is wobbly, changing the program may not fix it. If the program is wrong, adding a bigger attachment may not fix it. Good engineers find the real limit.

### 11. Plant Science Connects Directly To Food Quality
Plant growth is not only about size. Food quality matters. A fast-growing plant may not always have the best flavour, texture, or nutrient profile. Light, nutrients, water, harvest time, and stress can affect quality.

For leafy vegetables, colour, crispness, taste, safety, and shelf life matter. For fruit, sugar, acidity, firmness, aroma, and ripeness matter. For grains, protein and moisture matter. A food system wants useful food, not just plant mass.

This connects to Mission Meals because a robot that handles food should protect quality. Rough handling can bruise produce. Delays can reduce freshness. Wrong sorting can waste edible food.

### 12. Future Plant Research Questions
Scientists and farmers are still working on many questions:

- How can indoor farms use less energy?
- Which light recipes grow nutritious food efficiently?
- How can farms recycle water safely?
- How can sensors detect disease earlier?
- How can crops tolerate heat, drought, flooding, or salt?
- How can soil health be protected while producing enough food?
- How can robots inspect plants without damaging them?

These future questions show that plant science is not finished. Mission Meals is a doorway into real research.


## Expanded Knowledge Notes

### Plant Growth Is A Balance, Not A Checklist
It is easy to make a list of plant needs: light, water, air, nutrients, temperature, and space. But real plant growth is a balance. A plant with strong light but too little water may close stomata and slow photosynthesis. A plant with enough water but too little oxygen around roots may become unhealthy. A plant with many nutrients but wrong pH may not absorb them well.

Think of plant growth like a team project. If one team member cannot do the job, the whole project slows. That is why farmers search for the limiting factor instead of adding everything at once.

### The Source-Sink Idea
Plant scientists sometimes use the words source and sink. A source is a plant part that makes or releases sugars, such as a mature leaf doing photosynthesis. A sink is a plant part that uses or stores sugars, such as growing roots, fruits, seeds, or young leaves.

This helps explain why plants change during growth. A young plant may send resources to roots and leaves. A fruiting plant sends many resources to fruit. If light is weak, the source is weak. If roots are damaged, sinks and water uptake suffer.

A Mission Meals plant tray can represent this invisible resource flow. The visible plant is only the surface of a deeper sugar, water, and nutrient system.

### Xylem And Phloem: Two Transport Highways
Xylem carries water and dissolved minerals mostly upward from roots to leaves. Transpiration helps pull water through xylem.

Phloem carries sugars and other substances from sources to sinks. If leaves make sugar, phloem can move it to roots, fruits, or growing tips.

Xylem is like the water elevator, and phloem is like the sugar delivery road inside the plant.

These transport systems are why root health and leaf health are connected. A damaged root can affect leaves. Damaged leaves can affect fruit.

### Why Leaves Are Often Green
Leaves look green because chlorophyll absorbs red and blue light strongly and reflects more green light. This does not mean green light is useless. Plant responses are more complex than that. But the green colour gives us a clue that chlorophyll is present.

Yellow leaves can mean many things: nitrogen shortage, old leaves aging, water stress, root problems, disease, or other issues. A colour sensor can detect a colour difference, but diagnosis needs context.

This is why sensing and science must work together. The sensor tells you something changed. Science helps you ask why.

### Nutrient Deficiency Is A Detective Problem
A nutrient deficiency means a plant lacks enough of a nutrient. But symptoms can be confusing. Yellow leaves may point to nitrogen, iron, water stress, root damage, or disease. Purple colour may connect to phosphorus stress in some situations, but temperature and variety can also matter.

Farmers use observation, soil tests, water tests, tissue tests, and experience. In hydroponics, they can adjust the nutrient solution more directly. In soil, nutrients interact with organic matter, microbes, moisture, pH, and texture.

A good plant scientist does not jump to the first answer. They collect clues.

### pH Changes Nutrient Availability
pH measures how acidic or alkaline something is. A pH of 7 is neutral. Below 7 is acidic. Above 7 is alkaline. Plants often have a preferred pH range depending on crop and system.

pH matters because it changes whether nutrients are available to roots. A nutrient can be present but hard for the plant to absorb if pH is outside a good range. This is like having food locked in a cupboard.

Hydroponic systems monitor pH closely because the nutrient solution is the root environment. Soil farmers also care about pH, but soil changes more slowly and has buffering capacity.

### Electrical Conductivity Is Useful But Not Complete
Electrical conductivity, or EC, measures how well a solution conducts electricity. In hydroponics, EC gives a clue about dissolved ions, which often means nutrient concentration.

But EC does not tell exactly which nutrient is present. Two solutions can have the same EC but different nutrient balance. EC is like knowing the total number of students in a classroom without knowing who is there.

This is an important data lesson: one measurement rarely tells the whole story.

### Temperature Affects Plant Speed
Temperature affects enzyme activity, respiration, water movement, flowering, fruit set, disease risk, and stress. A plant has a temperature range where it grows well. Below that range, growth may slow. Above that range, stress can increase.

Heat can be especially dangerous when combined with water stress. If leaves lose water quickly and roots cannot replace it, the plant wilts. If stomata close to save water, carbon dioxide entry drops and photosynthesis slows.

This connects W05 to W12, where you will study climate risk and extreme heat.

### Microbes Can Help Or Harm
Microbes are tiny living things such as bacteria and fungi. Some microbes cause disease. Others help plants by cycling nutrients, supporting roots, or protecting against pathogens. Soil is full of microbial life.

Hydroponic and indoor systems also have microbes, even if they look clean. Farmers must manage microbial balance and prevent harmful organisms from spreading.

This is why cleanliness and monitoring matter in CEA. A controlled environment is not automatically a sterile environment.

### Plant Science Mission Examples
Water mission: The robot delivers a blue water resource to a dry plant zone. Science explanation: plants need water for photosynthesis, nutrient transport, and cell firmness.

Light mission: The robot activates a light station for a plant tray. Science explanation: light provides energy for photosynthesis, but energy use is a tradeoff.

Nutrient mission: The robot moves a nutrient marker to a hydroponic station. Science explanation: nutrients are dissolved in water and roots absorb them, but pH and EC must be controlled.

Stress mission: The robot sorts yellow plant markers from green plant markers. Science explanation: leaf colour can be a clue for stress, but diagnosis needs more evidence.

Root mission: The robot moves a tray gently without tipping. Science explanation: roots need water, oxygen, and support; rough handling can damage the plant system.


## Additional Guided Reading: Plant Problems You Can Diagnose

### Problem 1: A Plant Is Tall, Thin, And Pale
This may happen when light is too weak or too far away. The plant stretches to find light, making a long weak stem. In an indoor farm, this could mean the light intensity, light distance, or light timing needs adjustment.

Robot connection: a robot might move a tray closer to a light zone or mark the tray for inspection.

### Problem 2: Leaves Wilt During A Hot Afternoon
Wilting can happen when the plant loses water faster than roots can replace it. Heat, dry air, weak roots, low water, or damaged xylem can contribute.

Robot connection: a robot might deliver water to a dry zone, but the explanation should mention that water is only one possible cause. Heat and root health also matter.

### Problem 3: Hydroponic Plants Suddenly Decline
In hydroponics, roots depend on pumps, oxygen, pH, nutrient concentration, and water flow. A pump failure can harm plants quickly because roots may lose oxygen or water contact.

Robot connection: a robot could represent emergency delivery, pump activation, or sensor warning.

### Problem 4: Leaves Are Yellow But Soil Is Wet
The simple answer might be "add fertilizer," but wet soil can reduce root oxygen and damage roots. Damaged roots cannot absorb nutrients well, so the leaf colour can look like nutrient deficiency even when nutrients exist.

Robot connection: a sensor mission should avoid one-clue thinking. The robot can model detection, but humans still interpret the cause.

### Problem 5: Plants Grow Well But Taste Poor
Food production is not only about size. Too much or too little water, light, nutrient balance, harvest timing, and plant stress can affect flavour and texture.

Robot connection: gentle handling and correct timing protect quality, not only quantity.

### How This Week Prepares You For Robot Building
A plant-growth robot mission should name the plant process it supports. Use precise sentences:

- "This mission models irrigation because plants need water for photosynthesis and nutrient transport."
- "This mission models nutrient delivery because roots absorb dissolved minerals."
- "This mission models plant inspection because leaf colour can show stress."
- "This mission models controlled lighting because light spectrum, intensity, and timing affect growth."

These sentences are stronger than saying only "the robot helps plants." Science gives your robot action meaning.

### Mini Glossary Bridge To Later Weeks
CEA uses the plant needs from this week and puts them into a controlled room.

Precision agriculture uses sensors to measure plant needs and stress.

Agricultural robots act on plant needs by moving trays, removing weeds, inspecting leaves, or harvesting.

End-effectors must protect plant tissues because living food can be fragile.

Climate resilience matters because heat and water stress directly affect photosynthesis, transpiration, and roots.


## Final Plant Science Reminder: A Plant Is Alive While You Handle It

In a robotics competition, a plant model may be plastic, LEGO, or cardboard. In real food systems, plants are living organisms. Even after harvest, many plant foods are still biologically active for some time. They can lose water, respire, bruise, ripen, wilt, or spoil.

This changes how engineers think. A crate of metal screws can be handled roughly. A crate of lettuce cannot. A box of ripe tomatoes needs different handling from a bag of dry rice. Plant science therefore affects logistics and end-effector design.

A useful food-system sentence is: "The object property comes from biology." Lettuce is fragile because leaves are thin and full of water. Roots need oxygen because root cells respire. Fruit ripens because living tissues continue chemical changes. Seeds can be stored because they are adapted for waiting, but they still need protection from moisture and pests.

When you build a robot attachment, ask whether the real food would bruise, dry out, overheat, or be contaminated. Even if your model object is strong, your explanation should remember the living food behind it.

### Plant Science Links To Current World Challenges
Plant science connects to many current problems. Water scarcity makes irrigation efficiency important. Heat waves make transpiration and temperature stress important. Fertilizer cost makes nutrient management important. Urban farming makes artificial light and energy efficiency important. Food waste makes harvest timing and shelf life important.

Future research is trying to grow crops that tolerate heat and drought, use nutrients efficiently, resist disease, and grow well in controlled environments. Robots and sensors can help, but they need plant science to know what to measure and how to act.


## Tiny Home Experiment Ideas

You can understand plant needs without expensive equipment. Grow two bean seeds with the same water but different light. Compare leaf colour and stem shape. Place two similar plants in different watering schedules and observe wilting carefully, without harming them. Look at soil after watering and ask whether it drains or stays soggy.

These are not perfect scientific experiments unless you control variables, but they build observation skill. Observation is the beginning of both farming and robotics.

When recording plant observations, write date, condition, what changed, and what stayed the same. That habit prepares you for robot testing because both biology and engineering need careful records.


A final notebook sentence for this week: "Plants are living systems, so a robot that supports plant production must protect conditions for photosynthesis, roots, water movement, nutrients, and stress control." If your robot mission can connect to one of those conditions, it has a clear science reason.

Do not worry if the plant science feels detailed. You are not expected to become a botanist in one week. You are learning enough biology to explain why production infrastructure matters.

In your sketch, always include both leaves and roots, because food production depends on what happens above and below the growing surface. A tray is not only a platform; it is a life-support space for roots, water, air, and nutrients. That is why careful handling matters from seedling to harvest every day.

## Core Terms

### Photosynthesis
The process plants use to turn light energy, carbon dioxide, and water into sugar.

### Chlorophyll
The green pigment that helps plants capture light energy.

### Chloroplast
A structure inside plant cells where photosynthesis happens.

### Spectrum
The range of colours or wavelengths in light.

### Photon
A tiny packet of light energy.

### Photoperiod
The length of light and dark periods a plant experiences.

### Daily Light Integral
The total useful light a plant receives in one day.

### Stomata
Tiny openings on leaves that allow gas exchange.

### Transpiration
The movement of water through a plant and out through leaves as water vapour.

### Xylem
Plant tissue that transports water and dissolved minerals upward.

### Nutrient
A substance a plant needs to grow, such as nitrogen, phosphorus, potassium, calcium, or magnesium.

### Macronutrient
A nutrient plants need in larger amounts, such as nitrogen, phosphorus, and potassium.

### Micronutrient
A nutrient plants need in very small amounts, such as iron or zinc.

### Hydroponics
Growing plants without soil by giving roots water with dissolved nutrients.

### pH
A measure of how acidic or alkaline a liquid is. Nutrient solutions need the right pH so roots can take up nutrients.

### Electrical Conductivity
A measurement that helps estimate the amount of dissolved nutrients in a hydroponic solution.

### Limiting Factor
The condition or resource that most limits growth at a given time.

## Student Thinking Tasks

1. Choose one plant need: light, water, carbon dioxide, nutrients, oxygen, temperature, or space. Explain what happens if it is too low or too high.
2. Draw a plant as a system. Label leaves, roots, water, light, carbon dioxide, nutrients, sugar, and oxygen.
3. Choose one sensor that could help a farmer. What does it measure, and what decision could it support?
4. Design a small robot mission that helps plant production infrastructure.
5. Write one sentence explaining the biology behind your robot action.

## Sources For Further Reading
- NASA Growing Plants in Space: https://www.nasa.gov/exploration-research-and-technology/growing-plants-in-space/
- NASA Plant Biology Program: https://science.nasa.gov/biological-physical/focus-areas/plant-biology/focus-areas/
- NASA plant biology hardware: https://science.nasa.gov/biological-physical/focus-areas/plant-biology/hardware/
- USDA National Agricultural Library hydroponics: https://www.nal.usda.gov/farms-and-agricultural-production-systems/hydroponics
- NASA photosynthesis from space: https://www.nasa.gov/earth-and-climate/seeing-photosynthesis-from-space-nasa-scientists-use-satellites-to-measure-plant-health/
- USDA agriculture technology: https://www.nifa.usda.gov/topics/agriculture-technology
