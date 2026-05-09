# W07 Science Brief - Precision Agriculture, Sensors, Drones, And Data

This brief keeps the main ideas from `science.md` for shorter review.

## Big Idea
**Precision Agriculture** means using observations and data to treat different places differently. A field is not the same everywhere. One zone may be dry, another may have weeds, and another may need nutrients.

The main rule is simple: measure, compare, decide, act, and check the result. This is also how a good robot works.

## Past, Present, And Future
In the past, farmers used their senses and memory. They walked fields, touched soil, watched leaves, smelled soil, noticed insects, and remembered which areas stayed wet or dry. Precision agriculture did not invent observation. It added tools, maps, sensors, and automation.

Today, farms can use soil sensors, weather stations, GPS tractors, drones, satellites, cameras, yield monitors, crop maps, and computer vision. These tools can help save water, reduce wasted fertilizer, target weeds, detect stress earlier, and improve timing.

In the future, farms may use more robots, AI, plant-level sensing, autonomous tractors, digital twins, and early disease detection. The challenge is making these tools accurate, affordable, repairable, fair, and useful.

## Fields Are Variable
A field may look like one big area, but it contains many small differences: soil type, slope, shade, moisture, nutrients, pests, weeds, disease, compaction, and drainage.

If the whole field gets the same treatment, some places may get too much and others too little. Too much fertilizer can pollute water. Too little can reduce yield. Too much irrigation can harm roots. Too little can stress plants.

Precision agriculture begins by respecting variation.

## Sensors Turn Conditions Into Data
A **sensor** measures something. A soil moisture sensor measures water. A pH sensor measures acidity. A camera measures reflected light. A weather station measures temperature, rain, wind, and humidity.

But data is useful only if it changes a decision.

```text
measure -> compare -> decide -> act -> check
```

For a farm: soil is dry, compare with a threshold, irrigate the dry zone, then measure again. For a robot: colour sensor sees green, program chooses route A, robot moves the object, team checks the result.

## Location Matters
If a sensor says soil is dry, the farmer must know where. **GPS** is one satellite system that gives position. **GNSS** is the wider term for global navigation satellite systems.

A tractor can use position to follow rows, apply fertilizer in mapped zones, or record harvest results. A LEGO robot does not use GPS on the mat, but it still needs location thinking: start position, routes, turns, mission zones, docking points, and alignment.

## Remote Sensing Sees From Above
**Remote sensing** collects information without touching the target. Satellites, planes, and drones can see crop patterns from above. A drone is not a magic farm fixer; it is a flying sensor.

Some cameras see visible light. **Multispectral imaging** sees several bands of light, including near-infrared light that humans cannot see. Healthy plants reflect light differently from stressed plants.

A **vegetation index**, such as **NDVI**, uses reflected light to estimate plant greenness or vigour. But an index is not a diagnosis. Low NDVI might mean drought, disease, nutrient shortage, bare soil, or another problem. It says, "Look here," not always "This is the cause."

## Targeted Action
**Variable rate application** means applying different amounts of water, fertilizer, seed, or pesticide in different places. A smart sprayer may spray only weeds. An irrigation system may water only dry zones.

The science idea is **targeted action**: do the right thing, in the right place, at the right time. The robotics idea is the same: sense the right marker, choose the right action, and check that the action worked.

## Data Quality Matters
Bad data can cause bad decisions. Sensors can fail, drift, get dirty, or be placed badly. Cameras can be confused by shadows. GPS can have errors. A map can be out of date.

**Data quality** includes accuracy, precision, completeness, timeliness, and relevance. **Calibration** means checking a sensor against a known example so the reading can be trusted.

Before using a sensor, ask what it measures, what decision will change, how it could be wrong, and how you will test it.

## People Still Matter
Data needs interpretation. A soil sensor may say "dry," but the farmer still asks: What crop stage is this? Is rain coming? Is this sandy soil? Is water available? Is the sensor correct?

Precision agriculture should support farmers, not pretend farmers are unimportant. It also raises fairness questions because some tools are expensive or need internet, training, and repair services.

## Mission Meals Connections
A precision agriculture mission can use a colour marker before choosing a route, deliver water only to a dry zone, remove a weed marker without touching crop markers, sort stressed plants, or record which zones were completed.

The strongest explanation names the decision rule. Example: "If the plant marker is yellow, move it to inspection; if it is green, move it to harvest."

## Extra Details To Remember
A data pipeline is the path from measurement to action:

```text
sensor -> data storage -> cleaning -> analysis -> decision -> action -> result check
```

Each step can fail. A sensor can be dirty. A file can be labelled wrong. A model can make a bad prediction. A farmer may not receive the alert. A machine may apply the wrong amount. The result may not be checked.

Accuracy and precision are different. Accuracy means close to the true value. Precision means repeated readings are close to each other. A sensor can be precise but wrong, like a scale that always adds 2 kg. Calibration helps find and fix this.

Spatial resolution means how much detail you can see in space. A satellite may cover a huge area but with less detail. A drone may see more detail but cover less area. Temporal resolution means how often data is collected. A greenhouse sensor may record every minute; a satellite may pass every few days.

**Ground truth** means checking data against real observations. If a drone map shows a weak patch, a farmer may walk there to inspect soil and plants. If a robot program says it turned correctly, the team should check the actual robot.

Sensor fusion means combining more than one sensor. A robot may use motor degrees, a colour sensor, and wall alignment. Combining sensors can help, but it also adds decisions about which reading to trust.

## Review Example: Sensor To Action
A dry-zone marker is useful only if the robot changes behaviour after reading it. If the robot ignores the marker, the sensor is decoration.

## Key Takeaways
Precision agriculture is not "more data." It is useful data connected to action. Sensors, maps, drones, satellites, and AI are helpful only when they are tested, interpreted, and used for better decisions.

Final check: name one measurement, the decision it supports, one possible error, and the action that follows.
