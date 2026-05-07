#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_file = "Predictive_Weather_Guidance_Project_Documentation.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch, leftMargin=0.75*inch, rightMargin=0.75*inch)

# Container for PDF elements
elements = []

# Define styles
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#1e40af'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#1e40af'),
    spaceAfter=10,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontSize=13,
    textColor=colors.HexColor('#2563eb'),
    spaceAfter=8,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    leading=14
)

# ============== TITLE PAGE ==============
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Predictive Weather Guidance<br/>with Route Planning", title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Complete Technical Documentation", styles['Normal']))
elements.append(Spacer(1, 0.1*inch))
elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
elements.append(Spacer(1, 0.8*inch))

# ============== PROJECT OVERVIEW ==============
elements.append(Paragraph("📌 Project Overview", heading_style))
elements.append(Paragraph(
    "This is a <b>full-stack web application</b> that intelligently predicts weather conditions at specific points "
    "along a travel route and aligns them with your actual arrival times. Unlike standard GPS and weather applications "
    "that only show current conditions at your destination, this application forecasts what the weather will be like "
    "<b>when you actually arrive there</b>.<br/><br/>"
    "<b>Core Purpose:</b> To provide travelers with accurate, time-synchronized weather predictions for their entire journey, "
    "enabling safer and more informed travel decisions.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== HOW IT WORKS ==============
elements.append(Paragraph("🎯 How It Works", heading_style))
elements.append(Paragraph(
    "Users input three pieces of information: a <b>Start Location</b>, a <b>Destination</b>, and a <b>Departure Time</b>. "
    "The application then:<br/><br/>"
    "1. <b>Converts location names to GPS coordinates</b> using geocoding APIs<br/>"
    "2. <b>Calculates the driving route</b> and total travel time<br/>"
    "3. <b>Determines the midpoint</b> of the journey<br/>"
    "4. <b>Calculates exact arrival times</b> for start, midpoint, and destination<br/>"
    "5. <b>Fetches weather forecasts</b> from a weather API<br/>"
    "6. <b>Matches arrival times to forecast data</b> (closest 3-hour window)<br/>"
    "7. <b>Generates safety warnings</b> for adverse conditions (rain, thunderstorms, fog, high winds)<br/>"
    "8. <b>Saves the journey</b> to a secure, admin-only database<br/><br/>"
    "All searches are permanently logged in a backend database accessible only through an admin portal, "
    "protected by CAPTCHA challenges and encrypted password authentication.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== ARCHITECTURE OVERVIEW ==============
elements.append(Paragraph("⚙️ Full-Stack Architecture", heading_style))
elements.append(Paragraph(
    "This project follows a <b>client-server architecture</b> with a browser-based frontend and a Node.js backend server. "
    "The two components communicate via RESTful API endpoints, enabling real-time data persistence and secure admin access.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== FRONTEND TECHNOLOGIES ==============
elements.append(Paragraph("Frontend Technologies", subheading_style))

frontend_data = [
    ['Technology', 'Purpose', 'How It\'s Used'],
    ['HTML5 (index.html)', 'Semantic Structure', 'Defines all UI elements: input fields, modals, weather cards, database table'],
    ['CSS3 (styles.css)', 'Visual Styling & Design', 'Implements glassmorphism, responsive layouts (Flexbox/Grid), animations, gradients'],
    ['Leaflet.js (CDN)', 'Interactive Mapping', 'Renders OpenStreetMap, displays route markers, integrates base tile layer'],
    ['Leaflet Routing Machine (CDN)', 'Route Calculation', 'Computes fastest driving paths, calculates distance/time, draws blue route line'],
    ['Nominatim API', 'Geocoding & Reverse Geocoding', 'Converts place names → GPS coordinates; reverse converts coordinates → place names; autocomplete suggestions'],
    ['OpenWeather Forecast API', 'Weather Predictions', 'Fetches 5-day forecasts in 3-hour intervals; provides temp, conditions, wind speed, humidity, weather icons'],
    ['Vanilla JavaScript (script.js)', 'Frontend Logic & Orchestration', 'Handles debouncing, API calls, route calculation, weather matching, warning generation, database communication'],
]

frontend_table = Table(frontend_data, colWidths=[1.3*inch, 1.5*inch, 2.5*inch])
frontend_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))

elements.append(frontend_table)
elements.append(Spacer(1, 0.2*inch))

# ============== FRONTEND FEATURES ==============
elements.append(Paragraph("Frontend Features in Detail", subheading_style))

elements.append(Paragraph("<b>1. Location Autocomplete with Debouncing</b>", body_style))
elements.append(Paragraph(
    "As users type in the start or destination fields, JavaScript triggers a debounced function (400ms delay) that calls Nominatim API. "
    "This prevents API spam and provides real-time location suggestions. When a user selects a suggestion, the coordinates are cached in the input element's data attributes.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>2. Current Location Detection</b>", body_style))
elements.append(Paragraph(
    "The 🎯 button uses the browser's Geolocation API (navigator.geolocation) to request the user's precise GPS coordinates. "
    "The app then reverse-geocodes those coordinates back to a place name (village/town/city) using Nominatim.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>3. Interactive Map with Route Visualization</b>", body_style))
elements.append(Paragraph(
    "Leaflet renders the map centered on India (latitude 10.0, longitude 76.2). When routes are calculated, Leaflet Routing Machine "
    "draws a blue line representing the fastest driving path. The app also places a marker at the midpoint of the route.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>4. Intelligent Midpoint Calculation</b>", body_style))
elements.append(Paragraph(
    "After Leaflet Routing Machine provides the route coordinates, the JavaScript code calculates the cumulative distance along the path, "
    "finds the point closest to the halfway mark, and reverse-geocodes it to determine the nearest city/town name.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>5. Parallel Weather API Calls</b>", body_style))
elements.append(Paragraph(
    "Instead of fetching weather sequentially (three separate API calls), JavaScript uses Promise.all() to fetch all three weather forecasts simultaneously. "
    "This reduces wait time and improves performance.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>6. Adaptive Weather Matching</b>", body_style))
elements.append(Paragraph(
    "OpenWeather provides forecasts in 3-hour intervals (00:00, 03:00, 06:00, etc.). The app finds the forecast timestamp closest to each calculated arrival time. "
    "If you arrive at 4:30 PM, it uses either the 3:00 PM or 6:00 PM forecast, whichever is nearer.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>7. Automatic Safety Warnings</b>", body_style))
elements.append(Paragraph(
    "The generateWarnings() function analyzes OpenWeather's weather ID codes and conditions to detect:<br/>"
    "• Thunderstorms (ID 200-299) → ⛈️ warning<br/>"
    "• Rain conditions → 🌧️ warning<br/>"
    "• Fog/Mist/Haze (ID 700-799) → 🌫️ warning<br/>"
    "• Wind speeds > 10 m/s → 💨 warning<br/><br/>"
    "Warnings are displayed as colored alert boxes before the weather cards.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== BACKEND TECHNOLOGIES ==============
elements.append(PageBreak())
elements.append(Paragraph("Backend Technologies", subheading_style))

backend_data = [
    ['Technology', 'Purpose', 'How It\'s Used'],
    ['Node.js', 'JavaScript Runtime', 'Runs server-side code outside the browser'],
    ['Express.js (v5.2.1)', 'Web Framework', 'Creates REST API endpoints, handles HTTP requests/responses, middleware management'],
    ['CORS Middleware', 'Cross-Origin Requests', 'Allows frontend to communicate with backend server'],
    ['fs (File System)', 'Persistent Storage', 'Reads/writes JSON files (.database.json, .users.json) for data persistence'],
    ['bcryptjs (v3.0.3)', 'Password Security', 'Hashes passwords using salting (bcrypt cost: 10) for secure storage'],
    ['svg-captcha (v1.4.0)', 'Bot Protection', 'Generates distorted SVG images as CAPTCHA puzzles; prevents automated bot attacks'],
]

backend_table = Table(backend_data, colWidths=[1.3*inch, 1.5*inch, 2.5*inch])
backend_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))

elements.append(backend_table)
elements.append(Spacer(1, 0.2*inch))

# ============== BACKEND API ENDPOINTS ==============
elements.append(Paragraph("REST API Endpoints", subheading_style))

elements.append(Paragraph("<b>GET /api/history</b>", body_style))
elements.append(Paragraph(
    "Returns an array of all route searches stored in .database.json. Used when opening the admin database panel. "
    "Returns JSON format: [{ startLocation, destination, departureTime, distanceKm, travelTimeMin, weatherData, timestamp }, ...]",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>POST /api/history</b>", body_style))
elements.append(Paragraph(
    "Saves a new route search to .database.json. Frontend sends route data after weather prediction completes. "
    "Server adds server-side timestamp if not provided, inserts at beginning of array (newest first), and writes to disk.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>DELETE /api/history</b>", body_style))
elements.append(Paragraph(
    "Clears all records from .database.json. Only accessible after successful admin login. "
    "Requires user confirmation before execution.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>GET /api/captcha</b>", body_style))
elements.append(Paragraph(
    "Generates a new CAPTCHA puzzle. Returns JSON with: { id, svg }. The ID uniquely identifies the challenge "
    "and is stored in a Map with a 5-minute auto-expiration. The SVG is rendered directly in the browser.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>POST /api/login</b>", body_style))
elements.append(Paragraph(
    "Validates login credentials. Receives: { username, password, captchaId, captchaAnswer }. "
    "Verifies CAPTCHA first, then uses bcrypt.compareSync() to check password against stored hash. "
    "Returns { success: true/false, message }.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>POST /api/register</b>", body_style))
elements.append(Paragraph(
    "Registers a new admin user. Receives: { username, password }. Checks for duplicate usernames, "
    "hashes the password with bcryptjs (cost: 10), saves to .users.json. Returns success/failure message.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== SECURITY FEATURES ==============
elements.append(Paragraph("🔒 Security Features", heading_style))

elements.append(Paragraph("<b>1. Password Hashing with bcryptjs</b>", body_style))
elements.append(Paragraph(
    "All passwords are never stored in plain text. When a user registers or admin creates an account, "
    "the password is hashed using bcryptjs with a salt cost of 10 (generates ~2^10 iterations). "
    "During login, bcrypt.compareSync() compares the entered password hash against the stored hash without revealing either password.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>2. CAPTCHA-Protected Login</b>", body_style))
elements.append(Paragraph(
    "Before any login attempt is processed, users must solve a CAPTCHA puzzle. The server generates SVG-based distorted text images. "
    "Correct answers are stored server-side and automatically deleted after 5 minutes. This prevents automated bot attacks on the admin portal.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>3. Password Strength Validation</b>", body_style))
elements.append(Paragraph(
    "When registering new users, passwords must meet strict requirements using Regular Expressions (RegEx):<br/>"
    "• Minimum 8 characters: /^.{8,}$/<br/>"
    "• Contains uppercase: /[A-Z]/<br/>"
    "• Contains lowercase: /[a-z]/<br/>"
    "• Contains digit: /[0-9]/<br/>"
    "• Contains special character: /[!@#$%^&*()_+\\-=\\[\\]{};':\\\"\\\\|,.<>\\/?]+/<br/><br/>"
    "The Register button remains disabled until all requirements are met. Frontend provides real-time visual feedback (✓ green / ✗ red).",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>4. Local File-Based Database</b>", body_style))
elements.append(Paragraph(
    "Instead of a cloud-hosted database, route history is stored locally in .database.json and user credentials in .users.json. "
    "These are prefixed with a dot to be hidden from file listings and prevent Live Server from auto-refreshing when they change.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== PROJECT WORKFLOW ==============
elements.append(PageBreak())
elements.append(Paragraph("📊 Complete User Workflow", heading_style))

elements.append(Paragraph("<b>Step 1: Route Planning</b>", body_style))
elements.append(Paragraph(
    "User enters Start Location (e.g., 'Kochi'), Destination (e.g., 'Thrissur'), and Departure Time (datetime picker). "
    "Autocomplete suggestions appear as they type, powered by Nominatim API with 400ms debouncing.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 2: Geocoding</b>", body_style))
elements.append(Paragraph(
    "When 'Plan Route & Weather' button is clicked, JavaScript calls getCoordinates() for both inputs. "
    "If user selected from autocomplete, cached coordinates are used. Otherwise, geocode() calls Nominatim API to convert place names to lat/lng.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 3: Route Calculation</b>", body_style))
elements.append(Paragraph(
    "Leaflet Routing Machine receives start and destination coordinates and calculates the fastest driving route. "
    "It returns total distance (meters) and travel time (seconds), which are converted to km and minutes for display.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 4: Midpoint & Time Calculation</b>", body_style))
elements.append(Paragraph(
    "JavaScript calculates cumulative distances along the route path. The point closest to 50% of total distance is identified as the midpoint. "
    "Arrival times are calculated: StartTime = user's departure time; MidpointTime = StartTime + (totalTime/2); DestinationTime = StartTime + totalTime.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 5: Weather Fetching</b>", body_style))
elements.append(Paragraph(
    "Promise.all() simultaneously fetches 5-day weather forecasts for the three points (start, midpoint, destination) from OpenWeather API. "
    "Each forecast contains 40 data points (5 days × 8 intervals per day) with 3-hour granularity.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 6: Weather Matching</b>", body_style))
elements.append(Paragraph(
    "For each arrival time, getClosestForecast() finds the forecast entry with the nearest timestamp. "
    "OpenWeather's dt field (Unix timestamp) is compared against each point's calculated arrival time. The reduce() function identifies the closest match.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 7: UI Rendering</b>", body_style))
elements.append(Paragraph(
    "Three weather cards are displayed showing:<br/>"
    "• Location name (reverse-geocoded)<br/>"
    "• Arrival time (formatted as 'Mon, Apr 23, 03:45 PM')<br/>"
    "• OpenWeather icon (PNG from OpenWeather CDN)<br/>"
    "• Temperature and weather description<br/>"
    "• Wind speed (m/s) and humidity (%)<br/><br/>"
    "generateWarnings() analyzes all three weather conditions and displays colored warning boxes for adverse conditions.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 8: Database Saving</b>", body_style))
elements.append(Paragraph(
    "saveRouteToDatabase() sends a POST request to /api/history with route details. Backend adds a server-side timestamp and writes the record to .database.json. "
    "This happens in the background without blocking the UI.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 9: Admin Database Access</b>", body_style))
elements.append(Paragraph(
    "When user clicks 'View Database', a login modal appears. A fresh CAPTCHA is generated via GET /api/captcha. "
    "User solves the puzzle and provides credentials. Backend validates CAPTCHA, then bcrypt-verifies the password. "
    "On success, GET /api/history is called and all route records are displayed in a table.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== FILE STRUCTURE ==============
elements.append(Paragraph("📁 Project File Structure", heading_style))

file_structure = [
    ['File', 'Type', 'Description'],
    ['index.html', 'HTML5', 'Main page structure; contains input fields, map container, modal dialogs'],
    ['styles.css', 'CSS3', 'Styling for glassmorphism design, responsive layouts, animations'],
    ['script.js', 'JavaScript', 'Frontend logic: geocoding, routing, weather fetching, API communication (713 lines)'],
    ['server.js', 'Node.js', 'Express backend: API endpoints, database management, CAPTCHA generation, auth (154 lines)'],
    ['package.json', 'Configuration', 'Project metadata and npm dependencies (bcryptjs, cors, express, svg-captcha)'],
    ['.database.json', 'JSON Data', 'Stores search history records (hidden file, auto-created on first save)'],
    ['.users.json', 'JSON Data', 'Stores admin credentials with bcrypt hashes (hidden file, auto-initialized with default admin)'],
]

file_table = Table(file_structure, colWidths=[1.3*inch, 1.2*inch, 2.8*inch])
file_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))

elements.append(file_table)
elements.append(Spacer(1, 0.2*inch))

# ============== DEPENDENCIES ==============
elements.append(Paragraph("📦 Project Dependencies", heading_style))

elements.append(Paragraph("<b>NPM Packages (Backend)</b>", body_style))
elements.append(Paragraph(
    "• <b>express@5.2.1</b> - Web framework for creating REST API<br/>"
    "• <b>cors@2.8.6</b> - Middleware for enabling cross-origin requests<br/>"
    "• <b>bcryptjs@3.0.3</b> - Password hashing library (salting + hashing)<br/>"
    "• <b>svg-captcha@1.4.0</b> - SVG-based CAPTCHA image generation<br/>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>CDN Libraries (Frontend)</b>", body_style))
elements.append(Paragraph(
    "• <b>Leaflet v1.9.4</b> (leaflet.css, leaflet.js) - Interactive mapping library<br/>"
    "• <b>Leaflet Routing Machine v3.2.12</b> - Route calculation and visualization plugin<br/>"
    "• <b>Google Fonts - Outfit</b> - Modern sans-serif font family<br/>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>External APIs</b>", body_style))
elements.append(Paragraph(
    "• <b>OpenStreetMap Nominatim API</b> (https://nominatim.openstreetmap.org) - Free geocoding & reverse geocoding<br/>"
    "• <b>OpenWeather Forecast API</b> (https://api.openweathermap.org) - Free 5-day weather forecast data<br/>"
    "• <b>OpenWeatherMap Icons CDN</b> - Weather condition icons<br/>",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== STRENGTHS & ADVANTAGES ==============
elements.append(PageBreak())
elements.append(Paragraph("✅ Project Strengths & Advantages", heading_style))

elements.append(Paragraph("<b>1. Highly Secure Architecture</b>", body_style))
elements.append(Paragraph(
    "Uses industry-standard bcryptjs for password hashing with salting and high iteration cost. "
    "CAPTCHA protection prevents automated bot attacks. No passwords are stored in plain text. "
    "This meets OWASP security standards for authentication.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>2. Cost-Effective Solution</b>", body_style))
elements.append(Paragraph(
    "Relies entirely on free-tier APIs: Nominatim (free geocoding), OpenWeather (free 5-day forecast). "
    "No paid cloud infrastructure required. Backend uses local file-based storage instead of expensive cloud databases.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>3. Privacy-Respecting Design</b>", body_style))
elements.append(Paragraph(
    "Location data stays between the user's browser and public APIs. No tracking or analytics. "
    "Route history is stored locally, not in cloud databases. Users have full control over their data and can clear history anytime.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>4. Seamless Single-Page Experience</b>", body_style))
elements.append(Paragraph(
    "Uses modern async/await and Promise.all() for responsive interactions. No page reloads required. "
    "Modal dialogs pop in and out smoothly. Weather updates in real-time as data arrives.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>5. Modern UI/UX Design</b>", body_style))
elements.append(Paragraph(
    "Glassmorphism design with backdrop blur effects. Smooth gradients and transitions. Responsive layout adapts to mobile, tablet, and desktop screens. "
    "Visual feedback (loading states, button animations, color-coded warnings) guides users through the workflow.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>6. Intelligent Route Analysis</b>", body_style))
elements.append(Paragraph(
    "Automatically detects midpoint based on distance, not arbitrary fixed points. Calculates accurate arrival times. "
    "Matches weather forecasts to arrival times intelligently rather than just showing current conditions.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== LIMITATIONS ==============
elements.append(Paragraph("⚠️ Limitations & Known Issues", heading_style))

elements.append(Paragraph("<b>1. Nominatim Geocoding Limitations</b>", body_style))
elements.append(Paragraph(
    "Nominatim excels at finding cities and towns but struggles with specific street addresses or local business names. "
    "For example, 'Starbucks, Times Square' may not resolve as accurately as 'New York'. "
    "Users may need to input broader location names (neighborhoods, cities) rather than specific addresses.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>2. Weather Forecast Granularity (3-Hour Chunks)</b>", body_style))
elements.append(Paragraph(
    "OpenWeather's free API provides forecasts in 3-hour intervals (00:00, 03:00, 06:00, 09:00, etc.). "
    "If you arrive at 4:30 PM, the app uses either 03:00 PM or 06:00 PM data. This is an approximation, not minute-by-minute precision. "
    "Real-time weather conditions at arrival time could differ slightly from the forecasted 3-hour window.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>3. API Rate Limiting</b>", body_style))
elements.append(Paragraph(
    "Free APIs have rate limits. Nominatim allows ~1 request per second. OpenWeather's free tier allows 60 calls/minute. "
    "If thousands of users simultaneously search routes, these APIs may temporarily block requests. "
    "This is a limitation of free-tier services; premium tiers would solve this.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>4. Browser Geolocation Requirements</b>", body_style))
elements.append(Paragraph(
    "The 'Use Current Location' feature requires users to grant browser permission for geolocation. "
    "Not all users allow this. Geolocation accuracy varies by device (5-50m accuracy depending on method: GPS vs cell tower).",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>5. Leaflet Routing Limitation</b>", body_style))
elements.append(Paragraph(
    "Leaflet Routing Machine calculates car routes but doesn't account for real-time traffic or road conditions. "
    "Estimated arrival times are based on ideal driving speeds, not actual traffic congestion.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>6. Server Dependency</b>", body_style))
elements.append(Paragraph(
    "The app requires a running Node.js backend server. If the server crashes or is not started, database access fails. "
    "Route planning and weather still work (no server needed), but saving to database won't work.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== KEY ALGORITHMS ==============
elements.append(Paragraph("🔧 Key Algorithms & Technical Concepts", heading_style))

elements.append(Paragraph("<b>1. Debouncing for Autocomplete</b>", body_style))
elements.append(Paragraph(
    "When typing in the location field, a debounce function delays the API call by 400ms. If the user types another character within 400ms, "
    "the timer resets. This ensures the API is only called after the user pauses, drastically reducing unnecessary API requests.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>2. Cumulative Distance Calculation</b>", body_style))
elements.append(Paragraph(
    "Leaflet returns route coordinates as an array. JavaScript calculates the haversine distance (latitude/longitude differences) between consecutive points. "
    "Cumulative sums create a distances array. The midpoint is found by locating the index where cumulative distance exceeds 50% of total distance.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>3. Closest Forecast Matching</b>", body_style))
elements.append(Paragraph(
    "Given an arrival time (milliseconds), getClosestForecast() uses the reduce() function to iterate through 40 forecast points. "
    "For each point, it calculates |forecast.dt - targetTime| (absolute difference). The point with minimum difference is returned. "
    "Time complexity: O(n) where n=40.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>4. Weather ID Classification</b>", body_style))
elements.append(Paragraph(
    "OpenWeather uses numeric IDs for weather conditions (e.g., 200-299 = thunderstorms, 500-599 = rain). "
    "generateWarnings() checks these ID ranges to classify conditions and generate appropriate warnings. "
    "This is more reliable than string matching and works across all supported languages.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>5. bcryptjs Hashing Algorithm</b>", body_style))
elements.append(Paragraph(
    "bcryptjs uses the Blowfish cipher adapted for passwords. With cost=10, passwords are hashed through 2^10 (1024) iterations. "
    "Each password also gets a unique random salt (16 bytes). This makes rainbow table attacks infeasible even if .users.json is compromised.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>6. Promise.all() for Parallel Operations</b>", body_style))
elements.append(Paragraph(
    "Instead of three sequential fetch() calls (sequential = 3x latency), Promise.all() fetches all three weather forecasts simultaneously. "
    "If each call takes 1 second, sequential = 3 seconds total; parallel = 1 second total. This dramatically improves user experience.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== SETUP INSTRUCTIONS ==============
elements.append(PageBreak())
elements.append(Paragraph("🚀 Setup & Installation Instructions", heading_style))

elements.append(Paragraph("<b>Prerequisites</b>", body_style))
elements.append(Paragraph(
    "• Node.js (v14 or higher) and npm<br/>"
    "• A modern web browser (Chrome, Firefox, Safari, Edge)<br/>"
    "• An OpenWeather API key (free tier: https://openweathermap.org/api)<br/>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Step 1: Install Dependencies</b>", body_style))
elements.append(Paragraph(
    "Navigate to the project directory and run:<br/>"
    "<font face='Courier' size='9'>npm install</font><br/><br/>"
    "This installs all npm packages listed in package.json (express, cors, bcryptjs, svg-captcha).",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Step 2: Start the Backend Server</b>", body_style))
elements.append(Paragraph(
    "Run:<br/>"
    "<font face='Courier' size='9'>npm start</font><br/>"
    "or<br/>"
    "<font face='Courier' size='9'>node server.js</font><br/><br/>"
    "You should see: 'Backend server running on http://localhost:3000'",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Step 3: Open in Browser</b>", body_style))
elements.append(Paragraph(
    "Open index.html in a web browser. You can use:<br/>"
    "• Live Server extension (VS Code): Right-click index.html → Open with Live Server<br/>"
    "• Python: <font face='Courier' size='9'>python3 -m http.server 8000</font><br/>"
    "• Any other local server<br/><br/>"
    "Navigate to http://localhost:8000 (or whatever port your server uses).",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Step 4: Add OpenWeather API Key</b>", body_style))
elements.append(Paragraph(
    "The current API key is hardcoded in script.js (line: const apiKey = ...). "
    "For production, replace it with your own key from https://openweathermap.org/api. "
    "Free tier allows 60 calls/minute and includes 5-day forecasts.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Step 5: Test Login (Optional)</b>", body_style))
elements.append(Paragraph(
    "Click 'View Database' button. Use default admin credentials:<br/>"
    "• Username: <b>admin</b><br/>"
    "• Password: <b>AdminPassword123!</b><br/><br/>"
    "Solve the CAPTCHA puzzle (enter the distorted text) to access the admin panel.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== USAGE GUIDE ==============
elements.append(Paragraph("📖 User Guide", heading_style))

elements.append(Paragraph("<b>Planning a Route</b>", body_style))
elements.append(Paragraph(
    "1. Enter Start Location (e.g., 'Kochi'). Autocomplete suggestions appear.<br/>"
    "2. Enter Destination (e.g., 'Thrissur'). Autocomplete suggestions appear.<br/>"
    "3. (Optional) Select a departure time using the datetime picker. If left blank, current time is used.<br/>"
    "4. Click 'Plan Route & Weather' button.<br/>"
    "5. The app calculates the route and fetches weather for all three points.<br/>"
    "6. Weather cards and warnings appear below the input section.<br/>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Using Current Location</b>", body_style))
elements.append(Paragraph(
    "Click the 🎯 button to auto-fill the Start Location field with your GPS coordinates. "
    "The browser will request location permission. After granting it, the nearest city/town name is auto-filled.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Viewing the Route on Map</b>", body_style))
elements.append(Paragraph(
    "The blue line on the interactive map shows the fastest driving route. "
    "The map auto-centers and zooms to show the entire route. A marker at the midpoint shows the halfway point.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Understanding Weather Cards</b>", body_style))
elements.append(Paragraph(
    "Three cards show weather predictions for Start (departure time), Midpoint (halfway through journey), and Destination (arrival). "
    "Each card shows temperature, conditions, wind speed, humidity, and an icon from OpenWeather. "
    "The 'Forecast for' timestamp indicates which 3-hour forecast window the data comes from.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Safety Warnings</b>", body_style))
elements.append(Paragraph(
    "If adverse weather is detected at any point, colored warning boxes appear above the weather cards. "
    "⛈️ = Thunderstorms, 🌧️ = Rain, 🌫️ = Fog/Haze, 💨 = Strong winds. "
    "These help you decide whether the journey is safe.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Accessing Search History</b>", body_style))
elements.append(Paragraph(
    "Click 'View Database' button. Log in with admin credentials and solve the CAPTCHA. "
    "All past route searches are displayed in a table with timestamps, locations, distances, travel times, and weather summaries. "
    "Admins can clear all history or register new users from this panel.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== TECHNICAL CHALLENGES & SOLUTIONS ==============
elements.append(Paragraph("🎯 Technical Challenges & Solutions", heading_style))

elements.append(Paragraph("<b>Challenge 1: Synchronizing Arrival Times with 3-Hour Forecast Windows</b>", body_style))
elements.append(Paragraph(
    "<b>Problem:</b> OpenWeather forecasts come in fixed 3-hour intervals. If you arrive at 4:30 PM, how do you pick between 3:00 PM and 6:00 PM data?<br/>"
    "<b>Solution:</b> The getClosestForecast() function calculates the absolute time difference for every forecast point and returns the one with minimum difference. "
    "This ensures the closest matching forecast is always selected, minimizing prediction error.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Challenge 2: Finding the True Midpoint of a Road Route</b>", body_style))
elements.append(Paragraph(
    "<b>Problem:</b> A road route isn't a straight line; it curves and follows roads. How do you find the geographic center?<br/>"
    "<b>Solution:</b> Calculate cumulative distances between consecutive route coordinates. The midpoint is where cumulative distance exceeds 50% of total. "
    "Then reverse-geocode that coordinate to find the nearest town name.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Challenge 3: Preventing API Spam During Typing</b>", body_style))
elements.append(Paragraph(
    "<b>Problem:</b> Without rate limiting, typing 10 characters triggers 10 Nominatim API calls, exhausting rate limits and slowing down UX.<br/>"
    "<b>Solution:</b> Debouncing delays the API call by 400ms. Each keystroke resets the timer. Only when the user pauses for 400ms does the API fire. "
    "This reduces API calls by ~90% while maintaining responsive suggestions.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Challenge 4: Secure Password Storage</b>", body_style))
elements.append(Paragraph(
    "<b>Problem:</b> Storing passwords in plain text in .users.json creates massive security risk if file is leaked.<br/>"
    "<b>Solution:</b> All passwords are hashed using bcryptjs with cost=10 (1024 iterations) and unique salts. "
    "Even if .users.json is leaked, an attacker cannot reverse the hash to get original passwords. "
    "During login, bcrypt.compareSync() verifies the password without storing or revealing it.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Challenge 5: Preventing Bot Attacks on Admin Login</b>", body_style))
elements.append(Paragraph(
    "<b>Problem:</b> Bots could brute-force admin credentials, trying thousands of username/password combinations per minute.<br/>"
    "<b>Solution:</b> Implement CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart). "
    "Server generates SVG-based distorted text images. Users must solve the puzzle before login credentials are checked. "
    "CAPTCHAs auto-expire after 5 minutes, preventing long-term reuse.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Challenge 6: Parallel API Calls for Performance</b>", body_style))
elements.append(Paragraph(
    "<b>Problem:</b> Fetching weather for three locations sequentially = 3x latency (if each call takes 1s, total = 3s).<br/>"
    "<b>Solution:</b> Use Promise.all() to fetch all three weather forecasts simultaneously. Parallel execution = 1s total instead of 3s. "
    "This provides snappier user experience and makes the app feel more responsive.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== FUTURE ENHANCEMENTS ==============
elements.append(PageBreak())
elements.append(Paragraph("🔮 Future Enhancement Ideas", heading_style))

elements.append(Paragraph(
    "1. <b>Real-Time Traffic Integration:</b> Integrate Google Maps API to account for traffic congestion and adjust arrival time predictions dynamically.<br/><br/>"
    "2. <b>Multiple Route Alternatives:</b> Show 2-3 different route options (fastest, shortest, least traffic) with weather predictions for each.<br/><br/>"
    "3. <b>Severe Weather Alerts:</b> Send push notifications or SMS alerts if severe weather (hurricanes, tornadoes) is detected on the route.<br/><br/>"
    "4. <b>Historical Weather Comparison:</b> Show what weather was predicted vs. what actually happened to validate prediction accuracy.<br/><br/>"
    "5. <b>Multi-Stop Route Planning:</b> Add support for routes with intermediate stops (e.g., Kochi → Ernakulam → Thrissur → Kannur).<br/><br/>"
    "6. <b>Cloud Database Migration:</b> Replace local JSON files with MongoDB or PostgreSQL for scalability and multi-user support.<br/><br/>"
    "7. <b>Mobile App Version:</b> Build native iOS/Android apps using React Native or Flutter for on-the-go access.<br/><br/>"
    "8. <b>User Accounts & Personalization:</b> Allow regular users to create accounts, save favorite routes, get personalized weather alerts.<br/><br/>"
    "9. <b>Weather Animation Maps:</b> Display animated weather radar overlays showing rain, clouds, wind patterns along the route.<br/><br/>"
    "10. <b>AI-Powered Recommendations:</b> Use machine learning to recommend optimal departure times based on historical weather patterns.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== CONCLUSION ==============
elements.append(Paragraph("📝 Conclusion", heading_style))

elements.append(Paragraph(
    "This Predictive Weather Guidance with Route Planning application demonstrates a sophisticated full-stack web development project. "
    "It seamlessly integrates multiple technologies—frontend frameworks (Leaflet), external APIs (Nominatim, OpenWeather), and backend services (Node.js/Express)—to deliver "
    "a practical, secure, and user-friendly travel planning tool.<br/><br/>"
    "The project showcases best practices in:<br/>"
    "✓ <b>Frontend UX/UI Design</b> - Modern glassmorphism aesthetics with smooth interactions<br/>"
    "✓ <b>Full-Stack Architecture</b> - Clean separation between frontend and backend<br/>"
    "✓ <b>API Integration</b> - Handling multiple external APIs with error management<br/>"
    "✓ <b>Security Implementation</b> - Password hashing, CAPTCHA protection, input validation<br/>"
    "✓ <b>Data Persistence</b> - Local file-based storage with backend management<br/>"
    "✓ <b>Performance Optimization</b> - Debouncing, parallel API calls, efficient algorithms<br/><br/>"
    "While the current implementation uses free-tier APIs and local storage, the architecture is scalable and can be enhanced with premium services, "
    "cloud databases, and advanced features for production deployment.",
    body_style
))
elements.append(Spacer(1, 0.3*inch))

# Add footer
elements.append(Paragraph(
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br/>"
    "<i>This documentation was auto-generated with complete technical details about the Predictive Weather Guidance with Route Planning project.</i>",
    styles['Normal']
))

# Build PDF
doc.build(elements)
print(f"✅ PDF created successfully: {pdf_file}")
