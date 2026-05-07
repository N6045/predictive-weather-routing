#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors

pdf_file = "Pseudocode_Implementation_Guide.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch, leftMargin=0.75*inch, rightMargin=0.75*inch)

elements = []
styles = getSampleStyleSheet()

title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#1e40af'), spaceAfter=12, alignment=TA_CENTER, fontName='Helvetica-Bold')
slide_heading_style = ParagraphStyle('SlideHeading', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#dc2626'), spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold')
section_heading_style = ParagraphStyle('SectionHeading', parent=styles['Heading3'], fontSize=12, textColor=colors.HexColor('#2563eb'), spaceAfter=4, spaceBefore=4, fontName='Helvetica-Bold')
body_style = ParagraphStyle('CustomBody', parent=styles['BodyText'], fontSize=10, alignment=TA_LEFT, spaceAfter=8, leading=14)
code_style = ParagraphStyle('CodeStyle', parent=styles['BodyText'], fontSize=8.5, fontName='Courier', textColor=colors.HexColor('#374151'), backColor=colors.HexColor('#f3f4f6'), leftIndent=10, rightIndent=10, spaceAfter=8, leading=12, borderPadding=5)

def add_title(text):
    elements.append(Paragraph(text, title_style))
    elements.append(Spacer(1, 0.2*inch))

def add_algo_section(title, pseudocode, implementation, code_block):
    elements.append(Paragraph(title, slide_heading_style))
    
    elements.append(Paragraph("1. Original Pseudocode:", section_heading_style))
    elements.append(Paragraph(pseudocode, body_style))
    
    elements.append(Paragraph("2. Actual Implementation & Technical Details:", section_heading_style))
    elements.append(Paragraph(implementation, body_style))
    
    elements.append(Paragraph("3. Syntax & Code Block (script.js):", section_heading_style))
    elements.append(Paragraph(code_block.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))
    
    elements.append(Spacer(1, 0.2*inch))
    elements.append(PageBreak())

# --- Document Content ---
add_title("Algorithm Implementation & Technical Guide")
elements.append(Paragraph("This document explains the 5 core pseudocodes presented in the slides and details exactly how they are implemented in the actual JavaScript codebase. It maps the theoretical algorithms to their technical execution, including the specific syntax and code blocks used.", body_style))
elements.append(Spacer(1, 0.2*inch))

# 1. Road Mapping & Path Computation Algorithm
add_algo_section(
    "Algorithm 1: Road Mapping & Path Computation",
    "Read locations → Geocode → Request OSRM route → Extract path/distance/time → Compute midpoint index/coordinate → Draw route on map.",
    "<b>How it works in the code:</b><br/>"
    "The application relies on <b>Leaflet Routing Machine</b> which automatically handles the OSRM network requests. When the user hits 'Calculate', we first use the <b>Nominatim API</b> via the <code>geocode()</code> function to convert city names to latitude/longitude. <br/><br/>"
    "Once we have the coordinates, <code>L.Routing.control()</code> generates the route. We listen to the asynchronous <code>'routesfound'</code> event. The technical challenge was finding the <b>exact midpoint</b>. Rather than just taking the middle array index (which might be skewed on curved roads), the implementation calculates the <b>cumulative geographical distance</b> of the entire polyline using Leaflet's <code>p1.distanceTo(p2)</code>. It then iterates through the polyline array until it finds the coordinate that is exactly equal to <code>totalPathDistance / 2</code>.",
    "function calculateRoute(startLoc, destLoc) {\n"
    "  routingControl = L.Routing.control({\n"
    "    waypoints: [\n"
    "      L.latLng(startLoc.lat, startLoc.lng),\n"
    "      L.latLng(destLoc.lat, destLoc.lng)\n"
    "    ]\n"
    "  }).addTo(map);\n\n"
    "  routingControl.on('routesfound', async function (e) {\n"
    "    const coordinates = e.routes[0].coordinates;\n"
    "    let totalPathDistance = 0;\n"
    "    const distances = [0];\n"
    "    for (let i = 1; i < coordinates.length; i++) {\n"
    "      const p1 = L.latLng(coordinates[i - 1]);\n"
    "      const p2 = L.latLng(coordinates[i]);\n"
    "      totalPathDistance += p1.distanceTo(p2);\n"
    "      distances.push(totalPathDistance);\n"
    "    }\n"
    "    const targetMidDistance = totalPathDistance / 2;\n"
    "    // Loop to find coordinate matching targetMidDistance\n"
    "  });\n"
    "}"
)

# 2. Weather Forecast Extraction & API Integration
add_algo_section(
    "Algorithm 2: Weather Forecast Extraction",
    "Read coordinates → Construct API URLs → Fetch OpenWeather data → Check empty response → Store forecasts for start, mid, dest.",
    "<b>How it works in the code:</b><br/>"
    "We extract the forecast using the <b>OpenWeather 5-day/3-hour API</b>. The function <code>fetchForecast(lat, lng)</code> uses the native JavaScript <code>fetch()</code> API to make HTTP GET requests.<br/><br/>"
    "<b>Technical Optimization:</b> Instead of fetching the weather sequentially (which would block the thread and take 3x longer), the system implements <code>Promise.all()</code>. This allows the JavaScript engine to make all three network requests (start, mid, dest) <b>simultaneously</b>. The code waits until all three asynchronous promises resolve before moving to the next step. If the API key is missing or fails, a <code>try...catch</code> block catches the network error and prevents the app from crashing.",
    "async function fetchForecast(lat, lng) {\n"
    "  const url = `https://api.openweathermap.org/data/2.5/forecast...`;\n"
    "  const response = await fetch(url);\n"
    "  return await response.json();\n"
    "}\n\n"
    "// Parallel API Fetching\n"
    "try {\n"
    "  const [startData, midData, destData] = await Promise.all([\n"
    "    fetchForecast(routePoints.start.lat, routePoints.start.lng),\n"
    "    fetchForecast(routePoints.mid.lat, routePoints.mid.lng),\n"
    "    fetchForecast(routePoints.dest.lat, routePoints.dest.lng)\n"
    "  ]);\n"
    "} catch (error) {\n"
    "  console.error(\"Weather fetching error:\", error);\n"
    "}"
)

# 3. Route-Weather Synchronisation & Timeline Generation
add_algo_section(
    "Algorithm 3: Route-Weather Synchronisation",
    "Compute arrival times (Mid = start + travelTime/2) → Initialize min difference → Compute absolute time difference from arrival time for each forecast → Store closest forecast.",
    "<b>How it works in the code:</b><br/>"
    "This is the mathematical core of the app. OpenWeather returns a large array of forecast blocks, one for every 3 hours over 5 days. We need to find the specific block that matches our expected arrival time.<br/><br/>"
    "<b>Syntax Used:</b> The code calculates arrival times in Unix milliseconds (Epoch time). It then uses the JavaScript Array method <code>.reduce()</code> inside the <code>getClosestForecast()</code> function. The reducer iterates through the 40 weather blocks. For each block, it calculates <code>Math.abs(curr.dt - targetSec)</code> to find the absolute difference between the forecast time and the estimated arrival time. The element with the smallest absolute difference is returned as the final weather prediction.",
    "// Calculate expected arrival times (in milliseconds)\n"
    "const startMs = currentDepartureTime;\n"
    "const midMs = startMs + (summary.totalTime / 2 * 1000);\n"
    "const destMs = startMs + (summary.totalTime * 1000);\n\n"
    "function getClosestForecast(forecastData, targetTimeMs) {\n"
    "  const targetSec = targetTimeMs / 1000; // Convert to Seconds\n\n"
    "  // Reduce array to the item with the smallest time difference\n"
    "  return forecastData.list.reduce((prev, curr) => {\n"
    "    return (Math.abs(curr.dt - targetSec) < \n"
    "            Math.abs(prev.dt - targetSec) ? curr : prev);\n"
    "  });\n"
    "}"
)

# 4. Backend Orchestration & API Delivery
add_algo_section(
    "Algorithm 4: Orchestration & API Delivery",
    "Read locations → Geocode → Request OSRM → Compute Midpoint → Fetch Weather → Match Forecasts → Analyze Warnings → Return structured response.",
    "<b>How it works in the code:</b><br/>"
    "<i>Note for Presentation:</i> While the pseudocode describes this as a 'Backend' Orchestration, our architecture is heavily optimized by making the <b>Client-Side (Frontend JavaScript)</b> act as the orchestrator. This reduces server load to zero for navigation logic.<br/><br/>"
    "The <code>calculateBtn.addEventListener('click')</code> and <code>routingControl.on('routesfound')</code> functions act as the Orchestrator. They chain the asynchronous promises together. Once the frontend orchestrator completes the routing, timeline syncing, and weather extraction, it <b>delivers</b> the finalized data payload to the Node.js Backend via a <code>POST /api/history</code> fetch request, where it is written to the JSON file database.",
    "calculateBtn.addEventListener('click', async () => {\n"
    "  // 1. Geocode\n"
    "  const startLoc = await getCoordinates(startInput);\n"
    "  const destLoc = await getCoordinates(destInput);\n\n"
    "  // 2. Orchestrate Routing (which then triggers Weather)\n"
    "  calculateRoute(startLoc, destLoc);\n"
    "});\n\n"
    "// 3. API Delivery (Saving to Backend Database)\n"
    "async function saveRouteToDatabase(record) {\n"
    "  await fetch('http://localhost:3000/api/history', {\n"
    "    method: 'POST',\n"
    "    headers: { 'Content-Type': 'application/json' },\n"
    "    body: JSON.stringify(record)\n"
    "  });\n"
    "}"
)

# 5. Frontend Visualisation & UI
add_algo_section(
    "Algorithm 5: Frontend Visualisation & UI",
    "Listen to typing → Fetch suggestions (delayed) → Clear UI → Render Route Map → Display Summaries → Render Weather Cards → Display Warnings.",
    "<b>How it works in the code:</b><br/>"
    "The UI is completely reactive. The application uses a <b>Debounce Design Pattern</b> for the search inputs. Instead of firing an API request for every keystroke, a <code>setTimeout</code> delays the execution by 400ms. If the user types another key, <code>clearTimeout</code> resets the timer.<br/><br/>"
    "For rendering, standard DOM manipulation is used. The <code>generateWarnings()</code> function creates a JavaScript <code>Set()</code> to prevent duplicate warnings. It scans the <code>weatherId</code> property provided by OpenWeather. If the ID is between 200-299, it flags a Thunderstorm. If wind speed > 10 m/s, it flags high winds. It dynamically creates HTML elements (<code>document.createElement('div')</code>) and appends them to the DOM to alert the user.",
    "// 1. Debounce Implementation for Autocomplete\n"
    "function debounce(func, delay) {\n"
    "  let timeoutId;\n"
    "  return function (...args) {\n"
    "    clearTimeout(timeoutId);\n"
    "    timeoutId = setTimeout(() => { func.apply(this, args); }, delay);\n"
    "  };\n"
    "}\n\n"
    "// 2. Dynamic Warning Generation\n"
    "function generateWarnings(weatherArray) {\n"
    "  const warnings = new Set(); // Prevent duplicates\n"
    "  weatherArray.forEach(data => {\n"
    "    const weatherId = data.weather[0].id;\n"
    "    const windSpeed = data.wind.speed;\n\n"
    "    if (weatherId >= 200 && weatherId < 300) {\n"
    "      warnings.add(\"⛈️ Thunderstorm conditions detected.\");\n"
    "    }\n"
    "    if (windSpeed > 10) {\n"
    "      warnings.add(\"💨 Strong wind conditions detected.\");\n"
    "    }\n"
    "  });\n"
    "  // Append to DOM\n"
    "}"
)

doc.build(elements)
