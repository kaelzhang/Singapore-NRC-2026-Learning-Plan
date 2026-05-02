# W07 Science - Precision Agriculture, Sensors, Drones, And Data

This student document contains the science and food-system knowledge for the week. For robot building and programming work, see `robotics.md`.

## Big Question
How can farmers know exactly where a crop needs water, nutrients, or protection?

## Why This Week Matters
Precision agriculture is about making better decisions by observing differences. A field is not the same everywhere. One area may be dry, another may have weeds, and another may need nutrients. A greenhouse tray is not the same everywhere either. One plant may be healthy, another may be stressed.

Robots also need this idea. A good robot does not act blindly. It senses, decides, then acts. Precision agriculture is the farm version of that loop.

This week helps you connect sensors, data quality, mapping, computer vision, drones, satellites, and robot decisions.

## Key Reference Links For This Week
Use these links for reliable background:

- [GPS.gov precision agriculture](https://www.gps.gov/index.php/precision-agriculture-gps) - explains how GPS supports location-aware farming.
- [USDA ARS benefits and evolution of precision agriculture](https://www.ars.usda.gov/oc/utm/benefits-and-evolution-of-precision-agriculture/) - USDA overview of precision agriculture development.
- [USDA AgLab precision agriculture](https://aglab.ars.usda.gov/fuel-your-curiosity/sustainability/precision-agriculture) - clear USDA explanation.
- [FAO SOFA 2022 automation report](https://www.fao.org/agrifood-economics/publications/detail/en/c/1613500/) - global view of automation and digital technologies in agriculture.
- [NASA photosynthesis from space](https://www.nasa.gov/earth-and-climate/seeing-photosynthesis-from-space-nasa-scientists-use-satellites-to-measure-plant-health/) - example of remote sensing for plant health.
- [USDA agriculture technology topics](https://www.nifa.usda.gov/topics/agriculture-technology) - broad technology context.

## The One-Minute Idea
Precision agriculture uses sensors, maps, GPS, drones, cameras, satellites, and data to treat different places differently. The goal is to use the right input, in the right place, at the right time.

Instead of giving every plant the same help, precision agriculture asks, "What does this plant or place need?" Then it tries to help only where help is needed.

## Past, Present, Future

### Past
Farmers have always observed differences by walking fields, touching soil, watching leaves, smelling soil, noticing insects, remembering seasons, and comparing harvests. The old tool was human experience.

Farmers also made mental maps. They knew which corner stayed wet, which slope dried first, which patch had weeds, and which area produced better grain. Precision agriculture did not invent observation. It added instruments, maps, and automation to an old habit.

### Present
Modern farms can collect data using soil sensors, weather stations, GPS tractors, drones, satellite images, cameras, yield monitors, and crop models. Machines such as smart sprayers can use computer vision to target weeds instead of spraying everything.

Data can help farmers save water, reduce fertilizer waste, reduce pesticide use, detect stress earlier, and improve timing. But data must be accurate and useful. A beautiful map is not helpful if it leads to the wrong action.

### Future
Future precision agriculture may combine robots, AI, plant-level sensing, autonomous tractors, early disease detection, swarm robots, digital twins, and data platforms. The challenge is to make these systems accurate, affordable, repairable, explainable, and fair for farms of different sizes.

A future farm may use many small observations instead of one big guess. But farmers will still need judgement. Data supports decisions; it should not replace thinking.

## Deep Explanation

### 1. Fields Are Variable
A field may look like one big rectangle, but it contains many micro-conditions. Soil type, slope, shade, pests, moisture, compaction, drainage, nutrients, weeds, and disease can vary from one spot to another.

If farmers treat the whole field the same, some areas may get too much input while others get too little. Too much fertilizer can waste money and pollute water. Too little fertilizer can reduce yield. Too much irrigation can waste water and harm roots. Too little irrigation can stress plants.

Precision agriculture begins with the idea that variation is real and should be measured.

### 2. Sensors Turn Conditions Into Data
A sensor measures something. A soil moisture sensor measures water level. A pH sensor measures acidity. A weather station measures temperature, rain, wind, and humidity. A camera measures reflected light. A scale measures mass. A flow meter measures water movement.

Data is useful only if it leads to a decision:

```text
measure -> compare -> decide -> act -> check result
```

For example:

```text
soil is dry -> compare with threshold -> irrigate this zone -> measure again
```

This is the same logic a robot uses:

```text
color sensor sees red -> program chooses route A -> robot moves object -> team checks result
```

### 3. GPS And GNSS Give Location
Precision agriculture often needs location. If a sensor says soil is dry, the farmer must know where. GPS is one satellite-based navigation system. GNSS is a wider term for global navigation satellite systems.

[GPS.gov's precision agriculture page](https://www.gps.gov/index.php/precision-agriculture-gps) explains how position information supports mapping, guidance, and site-specific farming. A tractor can follow rows more accurately. A sprayer can apply inputs in mapped zones. A yield monitor can record where harvest was strong or weak.

In NRC, your robot does not use GPS on the mat. But it still needs location thinking: start position, route, turns, alignment, mission zones, and docking points.

### 4. Remote Sensing Looks From Above
Remote sensing means collecting information without touching the target. Satellites, planes, and drones can see crop patterns from above. This helps farmers see large areas faster than walking every row.

A normal camera sees visible light. Multispectral cameras see several bands of light, including near-infrared light that humans cannot see. Healthy plants reflect near-infrared light differently from stressed plants. This can reveal patterns before humans notice them from the ground.

Remote sensing can show crop vigour, water stress, disease patterns, storm damage, or uneven growth. But it does not explain everything by itself. A farmer may still need to inspect the field to find the cause.

### 5. Vegetation Indices Are Plant Clues
A vegetation index is a number calculated from reflected light. One well-known index is NDVI, the Normalized Difference Vegetation Index. You do not need to memorize the formula, but you should understand the idea: compare different light bands to estimate plant greenness or vigour.

An index is not a diagnosis. Low NDVI might mean drought, disease, nutrient shortage, soil problem, pest damage, or simply bare soil. The index says, "Look here." It does not always say, "This is the exact cause."

This is a good lesson for robot sensors too. A colour reading may tell you which object you see, but it can be affected by lighting, angle, shadows, or calibration.

### 6. Variable Rate Application Changes The Amount
Variable rate application means using different amounts of water, fertilizer, seed, or pesticide in different places. This can reduce waste and pollution, but only if the data and equipment are accurate.

Example: A field map shows one zone has enough nitrogen and another zone is low. The farmer applies more nitrogen only where needed.

Example: A smart irrigation system gives more water to a dry zone and less to a wet zone.

Example: A smart sprayer detects weeds and sprays only the weeds, not the whole field.

The science idea is targeted action. The robotics idea is also targeted action: do the right move in the right place for the right object.

### 7. Computer Vision Helps Machines Interpret Images
Computer vision is a technology that helps computers interpret images. In agriculture, computer vision can detect weeds, count plants, estimate fruit size, identify disease spots, guide harvesters, or sort produce.

Machine learning can help computer vision by learning patterns from many examples. But it needs good training data. A model trained on one crop variety, lighting condition, or farm may fail in another.

Computer vision also faces farm problems: moving leaves, shadows, dust, mud, overlapping plants, hidden fruit, changing sunlight, and similar-looking weeds and crops.

For students, the lesson is not "AI is magic." The lesson is: image-based decisions need examples, testing, and error checking.

### 8. Drones Are Flying Sensors, Not Magic Farm Fixers
Drones can collect images quickly, especially over fields that are hard to inspect on foot. They can carry visible, multispectral, thermal, or other sensors. Some drones can spray, but spraying drones need safety rules and careful operation.

Drones are useful when the information they collect leads to action. A drone map that nobody uses is just a picture. A drone map that helps a farmer inspect a problem zone can save time.

Limitations include battery life, weather, regulations, cost, image processing, and data interpretation. Wind, rain, and poor lighting can reduce usefulness.

### 9. Data Quality Matters
Bad data can lead to bad decisions. Sensors can fail. Cameras can be confused by shadows. GPS can have errors. A sensor can drift over time. A data file can be incomplete. A map can be out of date.

Data quality includes accuracy, precision, completeness, timeliness, and relevance. Accuracy means close to the true value. Precision means repeated measurements are close to each other. Timeliness means the data is recent enough to use. Relevance means the data actually helps the decision.

A robot team should learn the same habit. If your colour sensor reads differently under different lighting, collect data and adjust. If your run results change when the battery is low, record it.

### 10. Data Needs Interpretation And Action
A sensor reading is not the same as understanding. Imagine a soil sensor says "low moisture." The farmer still asks: Is the sensor correct? What crop stage is this? Is rain coming? Is this soil type sandy? Is irrigation available? Is water expensive?

Data becomes useful when combined with context. Farmers understand their fields. Technicians understand equipment. Scientists understand measurements. Good decisions often combine human knowledge and machine data.

This is why precision agriculture should support farmers, not treat them as unimportant.

### 11. Fairness And Access Matter
Precision tools can be expensive. Large farms may adopt them more easily than small farms. Some farmers may lack internet access, repair services, training, or money for sensors and software.

A technology can widen inequality if only some people can use it. It can also help smaller farms if it becomes affordable, shared, open, repairable, and locally useful.

This is why [FAO's automation work](https://www.fao.org/agrifood-economics/publications/detail/en/c/1613500/) discusses technology in relation to farm size, labour, and development. The social side matters.

### 12. Precision Agriculture Mission Ideas
Precision agriculture can become an NRC mission through:

- sensing a colour marker before choosing a route,
- sorting healthy and stressed plants,
- delivering water only to a dry zone,
- delivering nutrients only to a low-nutrient zone,
- avoiding a protected area,
- mapping which mission objects were completed,
- using test data to improve reliability.

The key idea is not the sensor itself. The key idea is data-driven action.


## Expanded Knowledge Notes

### Precision Starts With A Question
A sensor should answer a question. If you do not know the question, you may collect data that is interesting but useless.

Weak question: Can we collect drone images?

Stronger question: Which part of the field may be water-stressed this week?

Weak question: Can our robot read a colour?

Stronger question: Can our robot use the colour to choose the correct delivery zone?

Precision agriculture is not "use more data." It is "use the right data to make a better decision."

### The Data Pipeline
A data pipeline is the path from measurement to action:

```text
sensor -> data storage -> cleaning -> analysis -> decision -> action -> result check
```

Each step can fail. A sensor can be dirty. A file can be labelled wrong. A model can make a bad prediction. A farmer may not receive the alert. A machine may apply the wrong amount. The result may not be checked.

This is why precision agriculture needs system design, not only sensors.

### Accuracy And Precision Are Different
Accuracy means a measurement is close to the true value. Precision means repeated measurements are close to each other.

A sensor can be precise but inaccurate. Imagine a scale that always says your bag is 2 kg heavier than it really is. It gives repeatable readings, but they are wrong.

A sensor can be accurate on average but not precise. Imagine a reading that jumps above and below the true value.

Calibration helps improve trust. Calibration means checking and adjusting a sensor using a known standard.

### Spatial Resolution And Temporal Resolution
Spatial resolution means how much detail you can see in space. A satellite image may cover a huge area but with less detail than a drone image. A close camera may see one plant with high detail.

Temporal resolution means how often data is collected. A satellite may pass every few days. A greenhouse sensor may record every minute. A farmer may scout a field once a week.

A decision needs the right resolution. A fast-spreading disease may need frequent monitoring. A long-term soil map may not need daily updates.

### Ground Truth
Ground truth means checking data against real observations on the ground. If a drone image shows a weak patch, a farmer may walk there to inspect plants and soil. The image says where to look; ground truth helps explain why.

Machine learning also needs ground truth. If an image is labelled "weed," someone must know it is actually a weed. Bad labels teach bad models.

For an NRC robot, ground truth is your test observation. If the program says it turned 90 degrees, check whether the robot actually turned correctly.

### Sensor Fusion
Sensor fusion means combining data from more than one sensor. A farm robot might combine camera images, GPS, wheel odometry, and lidar. A greenhouse might combine temperature, humidity, light, and CO2 data.

Combining sensors can improve decisions, but it can also add complexity. If sensors disagree, the system must decide which one to trust.

In a LEGO robot, sensor fusion might be simple: use motor degrees for distance, a colour sensor for line detection, and physical alignment for position.

### Maps Are Models
A map is not the real field. It is a model of the field. A soil map, weed map, yield map, or irrigation map shows selected information. It leaves out other information.

Maps can be powerful because they help people see patterns. But maps can also hide uncertainty. A map with bright colours may look certain even when the data is weak.

Good map reading asks: When was this made? What data was used? What does the colour mean? What uncertainty exists? What action should follow?

### AI Needs Testing In The Real World
An AI model may perform well in a test dataset but fail in a different farm. Lighting, crop variety, camera angle, soil colour, weeds, and growth stage can change.

This is called generalization: can the model work beyond the examples it learned from? Generalization is hard in agriculture because living systems vary.

Responsible use of AI includes testing, monitoring, updating, and human oversight. A farmer should be able to question the system.

### Data Ownership And Privacy
Farm data can be valuable. It may include yield, soil fertility, input use, machinery paths, financial information, and production plans. Farmers may worry about who owns the data and how companies use it.

This is an advanced topic, but it matters. Data is not only technical; it is also social and economic.

For students, the simple version is: when data affects people, we should ask who controls it and who benefits.

### Precision Agriculture Mission Examples
Dry-zone mission: The robot reads a marker and delivers water only to the dry zone.

Weed mission: The robot detects a weed marker and removes it without touching crop markers.

Nutrient mission: The robot sorts low-nutrient and healthy plant markers.

Mapping mission: The team records which zones were completed and uses the data to improve strategy.

Calibration mission: The robot tests a sensor reading before starting the main task.

Each example follows the same loop: observe, decide, act, verify.


## Additional Guided Reading: From Sensor Reading To Decision

### Example: Soil Moisture
Sensor reading: this zone is dry.

Possible decisions: irrigate now, wait because rain is coming, inspect the sensor, or check whether the crop is drought-tolerant.

Why context matters: dry soil may be normal for one crop stage but dangerous for another. Sandy soil dries quickly. Clay soil holds water longer.

### Example: Leaf Colour
Sensor reading: leaves look less green.

Possible causes: nitrogen deficiency, old leaves, disease, water stress, root damage, shade, or camera lighting.

Possible decisions: inspect the plant, test soil or nutrient solution, compare with other data, or mark the zone for treatment.

### Example: Weed Detection
Sensor reading: camera identifies a weed.

Possible decisions: mechanically remove it, spray only that spot, ignore it if too small, or confirm with a human.

Why precision matters: removing a weed is useful only if the crop is not damaged.

### Example: Yield Map
Sensor reading: one area produced less crop.

Possible causes: poor soil, drainage problem, pest damage, shade, compaction, disease, or previous management.

Possible decisions: test soil, change irrigation, adjust planting density, or study the area next season.

### How To Use This In NRC
When your robot uses a sensor, write down the decision rule:

```text
If the marker is green, deliver to the healthy crop zone.
If the marker is yellow, deliver to the inspection zone.
If the marker is blue, deliver water.
```

Then test whether the sensor reads reliably. If lighting changes the reading, build a shield, slow down, calibrate, or use a simpler marker.

### Common Precision Agriculture Misunderstandings
Misunderstanding 1: More data always means better farming. Better thinking: useful data must answer a decision question.

Misunderstanding 2: A drone map automatically explains the problem. Better thinking: remote sensing often shows where to inspect, not the full cause.

Misunderstanding 3: AI removes the farmer. Better thinking: AI can support decisions, but farmers still provide context, ethics, and judgement.

Misunderstanding 4: Precision agriculture is only for big farms. Better thinking: some tools are expensive, but the principle of observing differences can help any farm.

Misunderstanding 5: Sensors are always objective. Better thinking: sensors need calibration, maintenance, and interpretation.


## Final Data Reminder: Data Must Change Action

Precision agriculture can be summarized in one sentence: data should change action. If data does not change a decision, it may not be useful yet.

A farmer does not need a moisture sensor because sensors are interesting. The farmer needs it because water decisions affect plant health, cost, and water conservation. A robot does not need a colour sensor because sensors are exciting. The robot needs it if colour changes the route, sorting choice, or safety response.

Before adding a sensor, ask:

1. What exactly will it measure?
2. What decision will change because of the measurement?
3. How could the measurement be wrong?
4. How will we test that it works?
5. What will the system do if the sensor fails?

These five questions turn a gadget into an engineering tool.

### Data And Food Security
Precision agriculture links back to food security because better information can improve availability, stability, and sustainability. Detecting drought stress early can protect yield. Applying fertilizer precisely can reduce waste and pollution. Mapping disease can support faster response. Recording yields can guide next season's planning.

But data does not automatically improve access or fairness. If only wealthy farms can use the tools, benefits may be uneven. That is why future precision agriculture must become more affordable, understandable, and useful in many contexts.


## Tiny Data Exercise

Make a three-column table: measurement, decision, possible error. Fill it with five examples from farming or robotics. For example: colour sensor reading, choose sorting zone, error from shadows. Or soil moisture, decide irrigation, error from bad sensor placement.

This exercise teaches the most important precision-agriculture habit: never collect data without knowing how it will guide action and how it might mislead you.


A final notebook sentence for this week: "Precision agriculture is useful when measurement changes action." Add your own example after it. For instance, "The sensor measured a dry zone, so the system watered that zone instead of watering every zone."

This is also how autonomous robots become smarter: they stop following only fixed motion and start responding to evidence from the field.

If the robot ignores the sensor result, the sensor is decoration, not intelligence. If the farm ignores the map, the map is decoration, not precision. Useful data changes what happens next and is checked after action. In practice, a good precision system also records the result after action. Did the dry zone improve? Did the weed return? Did the robot sort correctly? Feedback after action is what turns one decision into learning over time. Check, record, compare, and improve the next action carefully. Keep improving the evidence, not only the hardware.

## Core Terms

### Precision Agriculture
Farm management that uses data to observe, measure, and respond to differences in fields, crops, or animals.

### Sensor
A device that measures something in the world.

### GPS
A satellite-based system that helps locate a position on Earth.

### GNSS
A broader term for global navigation satellite systems, including GPS and other systems.

### Remote Sensing
Collecting information from a distance, often using satellites, drones, or cameras.

### Multispectral Imaging
Using cameras that see several bands of light, including light humans cannot see.

### Vegetation Index
A number calculated from reflected light to estimate plant condition.

### NDVI
A common vegetation index that compares red and near-infrared light to estimate plant greenness or vigour.

### Variable Rate Application
Applying different amounts of input in different places.

### Computer Vision
A technology that helps computers interpret images.

### Machine Learning
A way for computers to learn patterns from examples.

### Data Quality
How accurate, reliable, complete, recent, and useful data is for making decisions.

### Calibration
Adjusting or checking a sensor so its measurements are trustworthy.

### Targeted Action
Doing the right action in the right place instead of treating everything the same.

## Student Thinking Tasks

1. Choose one thing a farmer might measure: water, temperature, plant colour, location, weeds, or yield.
2. Explain what decision that measurement could support.
3. Describe one way the data could be wrong.
4. Design a robot mission that uses a sensor or marker before acting.
5. Write the mission as a loop: measure, compare, decide, act, check.

## Sources For Further Reading
- GPS.gov precision agriculture: https://www.gps.gov/index.php/precision-agriculture-gps
- USDA ARS - Benefits and Evolution of Precision Agriculture: https://www.ars.usda.gov/oc/utm/benefits-and-evolution-of-precision-agriculture/
- USDA AgLab - Precision Agriculture: https://aglab.ars.usda.gov/fuel-your-curiosity/sustainability/precision-agriculture
- FAO SOFA 2022 automation report: https://www.fao.org/agrifood-economics/publications/detail/en/c/1613500/
- NASA photosynthesis from space: https://www.nasa.gov/earth-and-climate/seeing-photosynthesis-from-space-nasa-scientists-use-satellites-to-measure-plant-health/
- USDA agriculture technology: https://www.nifa.usda.gov/topics/agriculture-technology
