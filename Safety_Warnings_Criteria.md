# Safety Warnings Criteria Guide
## Predictive Weather Route Planner

Based on the core logic in `script.js` (specifically the `generateWarnings()` function), the application dynamically scans the data returned by the OpenWeather API and looks for **4 specific criteria** to trigger the safety warnings.

### 1. Thunderstorms
* **Criteria:** OpenWeather API returns a `weather.id` between **200 and 299**.
* **What happens:** The system detects active thunderstorms (with or without rain/drizzle) and injects the warning:
  > *"⛈️ Thunderstorm conditions detected on route. Drive with extreme caution."*

### 2. Rain & Slippery Roads
* **Criteria:** OpenWeather API returns a `weather.id` between **500 and 599**, OR the main weather condition (`weather.main`) explicitly says **"Rain"**.
* **What happens:** The system flags wet conditions ranging from light drizzle to extreme rain and injects the warning:
  > *"🌧️ Rain expected on this part of the route. Roads may be slippery."*

### 3. Fog & Reduced Visibility
* **Criteria:** OpenWeather API returns a `weather.id` between **700 and 799**.
* **What happens:** These specific IDs belong to the "Atmosphere" group in OpenWeather. It detects things like Mist, Smoke, Haze, Dust, Fog, or Ash. If any of these are present, the system injects the warning:
  > *"🌫️ Reduced visibility due to fog, mist, or haze. Use headlights."*

### 4. High Winds
* **Criteria:** OpenWeather API returns a `wind.speed` that is **greater than 10 meters per second** (which is roughly 36 km/h).
* **What happens:** Regardless of the sky conditions, if the mathematical wind speed crosses this threshold, the system injects the warning:
  > *"💨 Strong wind conditions detected. Maintain safe speeds."*

---

### 💡 Presentation Tip: The Duplicate Warning Optimization
If the panelists ask how you manage these warnings—especially on a long route where it might be raining at the Start, Midpoint, and Destination simultaneously—you should explain that the warnings are processed using a **JavaScript `Set()` data structure**.

A `Set` mathematically prevents duplicate values. Therefore, instead of spamming the user interface with three identical rain warnings, the system intelligently collapses them into a single, clean warning banner. This is a deliberate, highly efficient UI design choice.
