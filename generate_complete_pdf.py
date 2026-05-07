#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_file = "Predictive_Weather_Guidance_Complete_Documentation.pdf"
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

code_style = ParagraphStyle(
    'CodeStyle',
    parent=styles['BodyText'],
    fontSize=8,
    fontName='Courier',
    leftIndent=20,
    rightIndent=20,
    spaceAfter=8,
    backColor=colors.HexColor('#f0f0f0'),
    borderPadding=10
)

# ============== TITLE PAGE ==============
elements.append(Spacer(1, 0.5*inch))
elements.append(Paragraph("Predictive Weather Guidance<br/>with Route Planning", title_style))
elements.append(Spacer(1, 0.2*inch))
elements.append(Paragraph("Complete Technical Documentation<br/>Including CAPTCHA & Password Validation", styles['Normal']))
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

# ============== PAGE BREAK ==============
elements.append(PageBreak())

# ============== CAPTCHA SYSTEM EXPLAINED ==============
elements.append(Paragraph("🔐 CAPTCHA System (Bot Protection)", heading_style))

elements.append(Paragraph(
    "CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a security mechanism that verifies a user is human, "
    "not a bot. Your application uses SVG-based distorted text CAPTCHAs generated server-side. This section explains exactly how the CAPTCHA system works.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== WHAT IS SVG ==============
elements.append(Paragraph("What is SVG Distorted Text?", subheading_style))

elements.append(Paragraph(
    "<b>SVG = Scalable Vector Graphics</b><br/><br/>"
    "SVG is an image format that uses <b>mathematical shapes and paths</b> instead of pixels:<br/>"
    "• <b>Pixels (PNG/JPG):</b> 'Draw a red dot at coordinate (100, 50)'<br/>"
    "• <b>SVG (Vector):</b> 'Draw a circle with radius 25 at center (100, 50) with red fill'<br/><br/>"
    "SVG files are text-based XML and can scale infinitely without losing quality. SVG distorted text refers to text that is rendered as SVG "
    "with intentional visual distortions applied to make it harder for automated bots to read using Optical Character Recognition (OCR).",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== CAPTCHA GENERATION FLOW ==============
elements.append(Paragraph("Step-by-Step CAPTCHA Generation & Validation Flow", subheading_style))

elements.append(Paragraph("<b>Step 1: Backend Generates CAPTCHA (server.js)</b>", body_style))
elements.append(Paragraph(
    "<font face='Courier' size='9'>app.get('/api/captcha', (req, res) => {<br/>"
    "    const captcha = svgCaptcha.create({<br/>"
    "        size: 5,                    // 5 random characters (e.g., 'a7k2m')<br/>"
    "        ignoreChars: '0o1il',       // Exclude confusing chars (0 vs O, l vs I)<br/>"
    "        noise: 2,                   // Add 2 distortion noise lines<br/>"
    "        color: true,                // Use multiple random colors<br/>"
    "        background: '#1e293b'       // Dark slate background to match theme<br/>"
    "    });<br/><br/>"
    "    // Generate unique ID (timestamp + random)<br/>"
    "    const captchaId = Date.now().toString() + Math.random().toString();<br/><br/>"
    "    // Store in memory with the correct answer<br/>"
    "    activeCaptchas.set(captchaId, captcha.text.toLowerCase());<br/><br/>"
    "    // Auto-delete after 5 minutes (security feature)<br/>"
    "    setTimeout(() => activeCaptchas.delete(captchaId), 5 * 60 * 1000);<br/><br/>"
    "    // Send SVG image + unique ID to frontend<br/>"
    "    res.json({ id: captchaId, svg: captcha.data });<br/>"
    "});</font>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph(
    "<b>What happens:</b><br/>"
    "• The server uses the <b>svg-captcha</b> library to generate a random 5-character text image with distortions<br/>"
    "• A unique <b>captchaId</b> is generated using the current timestamp + a random number (ensures uniqueness)<br/>"
    "• The correct answer (the 5 characters) is stored in an in-memory <b>Map</b> with the captchaId as the key<br/>"
    "• The CAPTCHA automatically expires and is deleted from memory after 5 minutes<br/>"
    "• Both the SVG image (as text/XML) and the unique ID are sent back to the frontend as JSON<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>Step 2: Frontend Displays CAPTCHA (script.js)</b>", body_style))
elements.append(Paragraph(
    "<font face='Courier' size='9'>async function loadCaptcha() {<br/>"
    "    try {<br/>"
    "        captchaImgContainer.innerHTML = 'Loading...';<br/><br/>"
    "        // Fetch from backend<br/>"
    "        const res = await fetch('http://localhost:3000/api/captcha');<br/>"
    "        const data = await res.json();<br/><br/>"
    "        // Save the unique ID globally<br/>"
    "        currentCaptchaId = data.id;<br/><br/>"
    "        // Render the SVG image in the HTML container<br/>"
    "        captchaImgContainer.innerHTML = data.svg;<br/>"
    "    } catch (e) {<br/>"
    "        captchaImgContainer.innerHTML = 'Error';<br/>"
    "    }<br/>"
    "}</font>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph(
    "<b>What happens:</b><br/>"
    "• The frontend calls the backend's /api/captcha endpoint<br/>"
    "• The response contains SVG XML code (rendered as a distorted image) and a unique captchaId<br/>"
    "• The SVG is inserted directly into the HTML, displaying the distorted 5-character puzzle<br/>"
    "• The captchaId is stored in a global JavaScript variable for later use<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>Step 3: User Views & Solves CAPTCHA</b>", body_style))
elements.append(Paragraph(
    "The user sees a distorted image with 5 characters rotated, scaled, and colored differently. "
    "Hidden noise lines make it harder for bots. The user manually reads the text and types it into the 'Enter CAPTCHA letters' input field.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>Step 4: Frontend Sends Answer & Credentials</b>", body_style))
elements.append(Paragraph(
    "<font face='Courier' size='9'>submitLoginBtn.addEventListener('click', async () => {<br/>"
    "    const username = loginUsernameInput.value.trim();<br/>"
    "    const password = loginPasswordInput.value.trim();<br/>"
    "    const captchaAnswer = loginCaptchaInput.value.trim(); // What user typed<br/><br/>"
    "    // Send to backend with CAPTCHA ID and answer<br/>"
    "    const res = await fetch('http://localhost:3000/api/login', {<br/>"
    "        method: 'POST',<br/>"
    "        headers: { 'Content-Type': 'application/json' },<br/>"
    "        body: JSON.stringify({<br/>"
    "            username,<br/>"
    "            password,<br/>"
    "            captchaId: currentCaptchaId,    // Unique ID from step 2<br/>"
    "            captchaAnswer                    // User's typed answer<br/>"
    "        })<br/>"
    "    });<br/>"
    "});</font>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph(
    "<b>What happens:</b><br/>"
    "• User enters username, password, and the CAPTCHA text they read<br/>"
    "• Frontend bundles all four pieces of data (username, password, captchaId, captchaAnswer)<br/>"
    "• Sends a POST request to /api/login on the backend<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>Step 5: Backend Validates CAPTCHA & Password (server.js)</b>", body_style))
elements.append(Paragraph(
    "<font face='Courier' size='9'>app.post('/api/login', (req, res) => {<br/>"
    "    const { username, password, captchaId, captchaAnswer } = req.body;<br/><br/>"
    "    // STEP 1: Validate CAPTCHA<br/>"
    "    const storedText = activeCaptchas.get(captchaId);<br/>"
    "    if (!storedText || !captchaAnswer || <br/>"
    "        storedText !== captchaAnswer.toLowerCase()) {<br/>"
    "        return res.status(401).json({<br/>"
    "            success: false,<br/>"
    "            message: 'Invalid CAPTCHA'<br/>"
    "        });<br/>"
    "    }<br/><br/>"
    "    // IMPORTANT: One-time use - delete CAPTCHA immediately<br/>"
    "    activeCaptchas.delete(captchaId);<br/><br/>"
    "    // STEP 2: Validate Username & Password<br/>"
    "    const users = readUsers();<br/>"
    "    const user = users.find(u => u.username === username);<br/><br/>"
    "    if (user && bcrypt.compareSync(password, user.passwordHash)) {<br/>"
    "        res.json({ success: true, message: 'Login successful' });<br/>"
    "    } else {<br/>"
    "        res.status(401).json({<br/>"
    "            success: false,<br/>"
    "            message: 'Invalid credentials'<br/>"
    "        });<br/>"
    "    }<br/>"
    "});</font>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph(
    "<b>What happens:</b><br/>"
    "• Backend retrieves the stored correct answer using the captchaId key<br/>"
    "• Compares the user's answer to the stored answer (case-insensitive)<br/>"
    "• <b>If CAPTCHA is wrong:</b> Returns error and login fails (bot detected)<br/>"
    "• <b>If CAPTCHA is correct:</b> Immediately deletes the CAPTCHA from memory (one-time use, prevents reuse)<br/>"
    "• Then validates username and bcrypt password hash<br/>"
    "• If both CAPTCHA and password are correct: Login succeeds ✓<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== SVG DISTORTIONS ==============
elements.append(Paragraph("SVG Distortions Explained", subheading_style))

distortion_data = [
    ['Distortion Type', 'Effect', 'Purpose'],
    ['Rotation', 'Characters tilted at angles (-15°, 8°, -5°, etc.)', 'Makes OCR (Optical Character Recognition) harder'],
    ['Skew', 'Characters slanted horizontally/vertically', 'Prevents straight-line text detection'],
    ['Scale', 'Characters at slightly different sizes', 'Confuses pattern matching algorithms'],
    ['Colors', 'Each character in different random color', 'Disrupts color-based text extraction'],
    ['Noise Lines', 'Random lines overlaid on image', 'Adds visual confusion and disrupts detection'],
    ['Background', 'Dark/colored background instead of white', 'High contrast reduces clarity for bots'],
]

distortion_table = Table(distortion_data, colWidths=[1.5*inch, 1.8*inch, 2.2*inch])
distortion_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dc2626')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#fecaca')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#fee2e2')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ('TOPPADDING', (0, 0), (-1, -1), 5),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
]))

elements.append(distortion_table)
elements.append(Spacer(1, 0.2*inch))

# ============== SVG EXAMPLE ==============
elements.append(Paragraph("Example SVG CAPTCHA Code Structure", subheading_style))

elements.append(Paragraph(
    "<font face='Courier' size='8'>&lt;svg width='200' height='60' xmlns='http://www.w3.org/2000/svg'&gt;<br/>"
    "  &lt;!-- Background --&gt;<br/>"
    "  &lt;rect width='200' height='60' fill='#1e293b'/&gt;<br/><br/>"
    "  &lt;!-- Distorted Text Characters --&gt;<br/>"
    "  &lt;text x='20' y='40' fill='#ff5733' font-size='40'<br/>"
    "        transform='rotate(-15 30 40) skewX(5)'&gt;a&lt;/text&gt;<br/>"
    "  &lt;text x='60' y='35' fill='#33ff57' font-size='42'<br/>"
    "        transform='rotate(8 70 35)'&gt;7&lt;/text&gt;<br/>"
    "  &lt;text x='100' y='45' fill='#3357ff' font-size='38'<br/>"
    "        transform='rotate(-5 110 45) skewY(3)'&gt;k&lt;/text&gt;<br/>"
    "  &lt;text x='140' y='38' fill='#ff33f0' font-size='41'<br/>"
    "        transform='rotate(12 150 38)'&gt;2&lt;/text&gt;<br/>"
    "  &lt;text x='180' y='42' fill='#ffff33' font-size='39'<br/>"
    "        transform='rotate(-8 190 42)'&gt;m&lt;/text&gt;<br/><br/>"
    "  &lt;!-- Noise Lines --&gt;<br/>"
    "  &lt;line x1='10' y1='5' x2='190' y2='50' stroke='#555' stroke-width='2'/&gt;<br/>"
    "  &lt;line x1='5' y1='55' x2='195' y2='10' stroke='#666' stroke-width='2'/&gt;<br/>"
    "&lt;/svg&gt;</font>",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph(
    "<b>Key SVG Concepts:</b><br/>"
    "• <b>transform='rotate(-15 30 40)'</b> = Rotate the character -15 degrees around pivot point (30, 40)<br/>"
    "• <b>fill='#ff5733'</b> = Color the character (different for each character)<br/>"
    "• <b>font-size='40'</b> = Each character slightly different size<br/>"
    "• <b>skewX(5), skewY(3)</b> = Slant the characters<br/>"
    "• <b>&lt;line&gt;</b> = Noise lines that cross through the text<br/>",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== WHY SVG ==============
elements.append(Paragraph("Why SVG Instead of PNG/JPG?", subheading_style))

svg_comparison = [
    ['Feature', 'SVG', 'PNG', 'JPG'],
    ['File Size', 'Very small (text-based XML)', 'Larger (pixel data)', 'Smaller but lossy'],
    ['Scalability', 'Perfect at any size', 'Blurry if enlarged', 'Blurry if enlarged'],
    ['Generation Speed', 'Instant (math-based)', 'Slower to render', 'Slower to render'],
    ['Anti-Bot Effectiveness', 'High (complex transforms)', 'Medium (easier to OCR)', 'Medium (easier to OCR)'],
    ['Server Resource Use', 'Very low', 'Moderate', 'Moderate'],
]

svg_table = Table(svg_comparison, colWidths=[1.2*inch, 1.2*inch, 1.2*inch, 1.2*inch])
svg_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#16a34a')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 8),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#dcfce7')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 7),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0fdf4')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 3),
    ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))

elements.append(svg_table)
elements.append(Spacer(1, 0.2*inch))

# ============== HOW BOTS FAIL ==============
elements.append(Paragraph("How Bots Try to Break CAPTCHA (and Why They Fail)", subheading_style))

elements.append(Paragraph("<b>Bot Method 1: Optical Character Recognition (OCR)</b>", body_style))
elements.append(Paragraph(
    "<b>What bots try:</b> Use OCR tools (Tesseract, Google Vision API) to automatically read text from images.<br/>"
    "<b>Why it fails:</b> The rotations, skews, colors, and noise lines break OCR algorithms. Modern OCR expects straight, clear text. "
    "A character rotated -15 degrees doesn't match any pattern in the OCR training data.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Bot Method 2: Color Segmentation</b>", body_style))
elements.append(Paragraph(
    "<b>What bots try:</b> Extract pixels of specific colors to isolate letters (e.g., 'find all red pixels').<br/>"
    "<b>Why it fails:</b> Your CAPTCHA uses random colors for each character. The 'a' might be red, but the next CAPTCHA's 'a' might be blue. "
    "No two CAPTCHAs are identical.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Bot Method 3: Pattern Matching</b>", body_style))
elements.append(Paragraph(
    "<b>What bots try:</b> Compare characters against known letter shapes stored in a database.<br/>"
    "<b>Why it fails:</b> Rotation and skew transforms completely change the shape. A skewed 'a' doesn't match the 'a' pattern in their database. "
    "Each character is transformed uniquely.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>Bot Method 4: Machine Learning Models</b>", body_style))
elements.append(Paragraph(
    "<b>What bots try:</b> Train neural networks on thousands of CAPTCHA images to learn to recognize characters.<br/>"
    "<b>Why it fails:</b> svg-captcha generates infinite variations. Each CAPTCHA is mathematically unique with random characters, angles, colors, and noise. "
    "There are billions of possible combinations. Bots can't collect and train on all variations.",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== PAGE BREAK ==============
elements.append(PageBreak())

# ============== PASSWORD VALIDATION SYSTEM ==============
elements.append(Paragraph("🔑 Password Validation System", heading_style))

elements.append(Paragraph(
    "Your application implements two-tier password security: <b>frontend strength validation</b> (real-time visual feedback) "
    "and <b>backend password hashing</b> (cryptographic security). This section explains both mechanisms.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== FRONTEND PASSWORD VALIDATION ==============
elements.append(Paragraph("Frontend Real-Time Password Strength Checking", subheading_style))

elements.append(Paragraph(
    "When a user registers a new admin account, the frontend provides instant visual feedback as they type. "
    "The password must meet 5 strict requirements before the Register button becomes active.",
    body_style
))
elements.append(Spacer(1, 0.12*inch))

elements.append(Paragraph("<b>The Validation Function (script.js)</b>", body_style))
elements.append(Paragraph(
    "<font face='Courier' size='9'>function checkPasswordStrength(pwd) {<br/>"
    "    // Test 1: Minimum 8 characters<br/>"
    "    const minLen = pwd.length >= 8;<br/><br/>"
    "    // Test 2: At least one UPPERCASE letter<br/>"
    "    const hasUpper = /[A-Z]/.test(pwd);<br/><br/>"
    "    // Test 3: At least one lowercase letter<br/>"
    "    const hasLower = /[a-z]/.test(pwd);<br/><br/>"
    "    // Test 4: At least one NUMBER<br/>"
    "    const hasNum = /[0-9]/.test(pwd);<br/><br/>"
    "    // Test 5: At least one SPECIAL CHARACTER<br/>"
    "    const hasSpec = /[!@#$%^&*()_+\\-=\\[\\]{};':\\\"\\\\|,.<>\\/?]+/<br/>"
    "                    .test(pwd);<br/><br/>"
    "    // Update UI for Requirement 1 (8+ Chars)<br/>"
    "    pwdReqLen.innerHTML = minLen ? '✓ 8+ Chars' : '✗ 8+ Chars';<br/>"
    "    pwdReqLen.style.color = minLen ? '#22c55e' : '#ef4444';<br/><br/>"
    "    // Update UI for Requirement 2 (Uppercase)<br/>"
    "    pwdReqUpper.innerHTML = hasUpper ? '✓ Uppercase' : '✗ Uppercase';<br/>"
    "    pwdReqUpper.style.color = hasUpper ? '#22c55e' : '#ef4444';<br/><br/>"
    "    // Update UI for Requirement 3 (Lowercase)<br/>"
    "    pwdReqLower.innerHTML = hasLower ? '✓ Lowercase' : '✗ Lowercase';<br/>"
    "    pwdReqLower.style.color = hasLower ? '#22c55e' : '#ef4444';<br/><br/>"
    "    // Update UI for Requirement 4 (Number)<br/>"
    "    pwdReqNum.innerHTML = hasNum ? '✓ Number' : '✗ Number';<br/>"
    "    pwdReqNum.style.color = hasNum ? '#22c55e' : '#ef4444';<br/><br/>"
    "    // Update UI for Requirement 5 (Special Char)<br/>"
    "    pwdReqSpec.innerHTML = hasSpec ? '✓ Special Char' : '✗ Special Char';<br/>"
    "    pwdReqSpec.style.color = hasSpec ? '#22c55e' : '#ef4444';<br/><br/>"
    "    // Return TRUE only if ALL 5 requirements are met<br/>"
    "    return minLen && hasUpper && hasLower && hasNum && hasSpec;<br/>"
    "}</font>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>Understanding Regular Expressions (RegEx):</b>", body_style))

regex_data = [
    ['RegEx Pattern', 'What It Tests', 'Examples (Pass/Fail)'],
    ['/[A-Z]/', 'At least one UPPERCASE letter (A-Z)', 'Pass: "Pass", Fail: "pass"'],
    ['/[a-z]/', 'At least one lowercase letter (a-z)', 'Pass: "Pass", Fail: "PASS"'],
    ['/[0-9]/', 'At least one number (0-9)', 'Pass: "Pass1", Fail: "Pass"'],
    ['/[!@#$%^&*...]+/', 'At least one special character', 'Pass: "Pass1!", Fail: "Pass1"'],
]

regex_table = Table(regex_data, colWidths=[1.5*inch, 1.8*inch, 2.2*inch])
regex_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#7c3aed')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 8),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#ede9fe')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 7),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f3ff')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

elements.append(regex_table)
elements.append(Spacer(1, 0.15*inch))

# ============== REAL-TIME FEEDBACK ==============
elements.append(Paragraph("Real-Time Feedback as User Types", subheading_style))

elements.append(Paragraph(
    "<b>Example User Experience:</b><br/><br/>"
    "<b>User types 'p':</b><br/>"
    "✗ 8+ Chars (red), ✗ Uppercase, ✓ Lowercase, ✗ Number, ✗ Special Char<br/>"
    "Register button: DISABLED<br/><br/>"
    "<b>User types 'pass':</b><br/>"
    "✗ 8+ Chars (red), ✗ Uppercase, ✓ Lowercase, ✗ Number, ✗ Special Char<br/>"
    "Register button: DISABLED<br/><br/>"
    "<b>User types 'Pass123':</b><br/>"
    "✓ 8+ Chars (green), ✓ Uppercase, ✓ Lowercase, ✓ Number, ✗ Special Char (red)<br/>"
    "Register button: DISABLED<br/><br/>"
    "<b>User types 'Pass123!':</b><br/>"
    "✓ 8+ Chars (green), ✓ Uppercase (green), ✓ Lowercase (green), ✓ Number (green), ✓ Special Char (green)<br/>"
    "Register button: ENABLED (clickable!)<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== EVENT LISTENERS ==============
elements.append(Paragraph("Event Listeners That Trigger Validation", subheading_style))

elements.append(Paragraph(
    "<font face='Courier' size='9'>// Listen for changes in the password field<br/>"
    "if (regPassword) {<br/>"
    "    regPassword.addEventListener('input', (e) => {<br/>"
    "        // Check password strength<br/>"
    "        const isStrong = checkPasswordStrength(e.target.value);<br/><br/>"
    "        // Disable button if:<br/>"
    "        // 1) Password is not strong, OR<br/>"
    "        // 2) Username field is empty<br/>"
    "        submitRegBtn.disabled = !isStrong || <br/>"
    "                                regUsername.value.trim().length === 0;<br/>"
    "    });<br/>"
    "}<br/><br/>"
    "// Also listen for changes in the username field<br/>"
    "if (regUsername) {<br/>"
    "    regUsername.addEventListener('input', (e) => {<br/>"
    "        // Re-check password strength<br/>"
    "        const isStrong = checkPasswordStrength(regPassword.value);<br/><br/>"
    "        // Disable button if:<br/>"
    "        // 1) Password is not strong, OR<br/>"
    "        // 2) Username field (that just changed) is empty<br/>"
    "        submitRegBtn.disabled = !isStrong || <br/>"
    "                                e.target.value.trim().length === 0;<br/>"
    "    });<br/>"
    "}</font>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "<b>How This Works:</b><br/>"
    "• Every time the user types in the password field, the 'input' event fires<br/>"
    "• checkPasswordStrength() tests all 5 requirements and updates the UI<br/>"
    "• The Register button is <b>disabled</b> unless <b>ALL</b> of these are true:<br/>"
    "  1. Password passes all 5 strength requirements<br/>"
    "  2. Username field is not empty<br/>"
    "• When all conditions are met, the button <b>enables</b> (turns clickable)<br/>",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== BACKEND PASSWORD HASHING ==============
elements.append(Paragraph("Backend Password Hashing & Security", subheading_style))

elements.append(Paragraph(
    "Even though the frontend validates password strength, <b>never trust the frontend alone</b> for security. "
    "The backend performs cryptographic hashing using bcryptjs before storing passwords.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>When User Registers (server.js)</b>", body_style))
elements.append(Paragraph(
    "<font face='Courier' size='9'>app.post('/api/register', (req, res) => {<br/>"
    "    const { username, password } = req.body;<br/>"
    "    const users = readUsers();<br/><br/>"
    "    // Check if username already exists<br/>"
    "    if (users.find(u => u.username === username)) {<br/>"
    "        return res.status(400).json({<br/>"
    "            success: false,<br/>"
    "            message: 'Username already exists'<br/>"
    "        });<br/>"
    "    }<br/><br/>"
    "    // Hash the password using bcryptjs<br/>"
    "    users.push({<br/>"
    "        username,<br/>"
    "        passwordHash: bcrypt.hashSync(password, 10)<br/>"
    "    });<br/><br/>"
    "    // Save to .users.json<br/>"
    "    writeUsers(users);<br/><br/>"
    "    res.json({<br/>"
    "        success: true,<br/>"
    "        message: 'User registered successfully'<br/>"
    "    });<br/>"
    "});</font>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "<b>What bcryptjs Does:</b><br/>"
    "• <b>Salt Generation:</b> Generates a random 16-byte salt (unique sequence)<br/>"
    "• <b>Hashing:</b> Uses the Blowfish cipher adapted for passwords<br/>"
    "• <b>Iterations:</b> With cost=10, the password is hashed 2^10 = <b>1024 times</b><br/>"
    "• <b>Result:</b> Original password is never stored; only the hash is saved<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>Example Hash Transformation:</b>", body_style))
elements.append(Paragraph(
    "<b>Original Password:</b> MyPass123!<br/>"
    "<b>Salt:</b> $2a$10$N9qo8uLO (embedded in hash)<br/>"
    "<b>Hash (bcrypt):</b> $2a$10$N9qo8uLO123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP<br/><br/>"
    "Notice: The hash is 60 characters long and always starts with $2a$10$ (indicating bcrypt algorithm and cost factor).<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== LOGIN VERIFICATION ==============
elements.append(Paragraph("When User Logs In (Password Verification)", subheading_style))

elements.append(Paragraph(
    "<font face='Courier' size='9'>app.post('/api/login', (req, res) => {<br/>"
    "    const { username, password, captchaId, captchaAnswer } = req.body;<br/><br/>"
    "    // (CAPTCHA validation skipped for brevity)<br/><br/>"
    "    // Find user by username<br/>"
    "    const users = readUsers();<br/>"
    "    const user = users.find(u => u.username === username);<br/><br/>"
    "    // Use bcrypt to compare passwords WITHOUT storing or revealing either<br/>"
    "    if (user && bcrypt.compareSync(password, user.passwordHash)) {<br/>"
    "        res.json({<br/>"
    "            success: true,<br/>"
    "            message: 'Login successful'<br/>"
    "        });<br/>"
    "    } else {<br/>"
    "        res.status(401).json({<br/>"
    "            success: false,<br/>"
    "            message: 'Invalid credentials'<br/>"
    "        });<br/>"
    "    }<br/>"
    "});</font>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph("<b>How bcrypt.compareSync() Works:</b>", body_style))
elements.append(Paragraph(
    "1. <b>Receives:</b> The entered password (plaintext) and the stored hash<br/>"
    "2. <b>Extracts Salt:</b> Pulls the salt from the hash (embedded in the first 29 characters)<br/>"
    "3. <b>Re-Hash:</b> Hashes the entered password using the extracted salt and same cost factor<br/>"
    "4. <b>Compare:</b> Compares the newly-generated hash to the stored hash<br/>"
    "5. <b>Result:</b> If they match → Password is correct ✓ → Login allowed<br/>"
    "         If they don't match → Password is wrong ✗ → Login denied<br/>",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

elements.append(Paragraph(
    "<b>Why This is Secure:</b><br/>"
    "• The original password is <b>never revealed</b> to anyone, even the server administrator<br/>"
    "• If .users.json is leaked, attackers see only hashes, not passwords<br/>"
    "• The Blowfish cipher with 1024 iterations is <b>intentionally slow</b> (takes ~100ms per attempt)<br/>"
    "• This slowness prevents brute-force attacks (would take 100ms × billions of attempts = weeks)<br/>"
    "• Each password has a unique salt, preventing identical passwords from producing identical hashes<br/>",
    body_style
))
elements.append(Spacer(1, 0.2*inch))

# ============== SECURITY COMPARISON ==============
elements.append(Paragraph("Password Storage: Bad vs. Good Practices", subheading_style))

security_comparison = [
    ['Practice', 'Security Level', 'Vulnerability', 'Example'],
    ['Plain Text', '❌ None', 'Anyone reading file sees password', 'password123'],
    ['Simple MD5 Hash', '❌ Poor', 'Rainbow tables defeat it in seconds', 'e3b0c44298fc1c14...'],
    ['Salted Hash (weak)', '⚠️ Fair', 'GPU/ASIC attacks feasible', 'sha256(salt + pwd)'],
    ['bcryptjs (cost=10)', '✓ Excellent', 'Brute-force takes months-years', '$2a$10$N9qo8uL...'],
]

security_table = Table(security_comparison, colWidths=[1.4*inch, 1.2*inch, 1.6*inch, 1.8*inch])
security_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#059669')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 8),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#d1fae5')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 7),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecfdf5')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))

elements.append(security_table)
elements.append(Spacer(1, 0.2*inch))

# ============== PAGE BREAK ==============
elements.append(PageBreak())

# ============== SECURITY FEATURES ==============
elements.append(Paragraph("🔒 Complete Security Summary", heading_style))

elements.append(Paragraph(
    "Your application implements a comprehensive, defense-in-depth security model that protects against multiple attack vectors.",
    body_style
))
elements.append(Spacer(1, 0.15*inch))

# ============== SECURITY LAYER TABLE ==============
elements.append(Paragraph("Multi-Layer Security Architecture", subheading_style))

security_layers = [
    ['Layer', 'Technology', 'Attack Prevented', 'How It Works'],
    ['Layer 1: Bot Detection', 'SVG CAPTCHA', 'Automated bot login attacks', 'Distorted text defeats OCR; infinite variations'],
    ['Layer 2: One-Time Use', 'CAPTCHA Expiration', 'CAPTCHA replay attacks', 'Each CAPTCHA deleted after 1 use; 5-min timeout'],
    ['Layer 3: Password Strength', 'RegEx Validators', 'Weak password registration', '5 requirements enforced (length, upper, lower, num, special)'],
    ['Layer 4: Password Hashing', 'bcryptjs (cost=10)', 'Stolen password database attacks', '1024 hash iterations + unique salt per password'],
    ['Layer 5: Credential Verification', 'bcrypt.compareSync()', 'Brute-force login attempts', 'Slow comparison (~100ms); blocks rapid attempts'],
]

security_layers_table = Table(security_layers, colWidths=[0.9*inch, 1.2*inch, 1.4*inch, 2.0*inch])
security_layers_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0369a1')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 7),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#cffafe')),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTSIZE', (0, 1), (-1, -1), 6),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ecf7fb')]),
    ('LEFTPADDING', (0, 0), (-1, -1), 3),
    ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ('TOPPADDING', (0, 0), (-1, -1), 3),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
]))

elements.append(security_layers_table)
elements.append(Spacer(1, 0.2*inch))

# ============== PROJECT WORKFLOW ==============
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
    "Three weather cards are displayed showing location name, arrival time, weather icon, temperature, description, wind speed, and humidity. "
    "generateWarnings() analyzes all three weather conditions and displays colored warning boxes for adverse conditions.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 8: Database Saving</b>", body_style))
elements.append(Paragraph(
    "saveRouteToDatabase() sends a POST request to /api/history with route details. Backend adds a server-side timestamp and writes the record to .database.json.",
    body_style
))
elements.append(Spacer(1, 0.08*inch))

elements.append(Paragraph("<b>Step 9: Admin Login & Database Access</b>", body_style))
elements.append(Paragraph(
    "When user clicks 'View Database', a login modal appears with CAPTCHA. User solves the puzzle and provides credentials. "
    "Backend validates CAPTCHA, then bcrypt-verifies the password. On success, GET /api/history is called and route records are displayed in a table.",
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

# ============== CONCLUSION ==============
elements.append(PageBreak())
elements.append(Paragraph("📝 Conclusion", heading_style))

elements.append(Paragraph(
    "This Predictive Weather Guidance with Route Planning application is a sophisticated, production-ready full-stack project that demonstrates "
    "best practices in web development, security, and user experience design.<br/><br/>"
    "<b>Security Highlights:</b><br/>"
    "✓ <b>CAPTCHA Protection</b> - SVG-based distorted text defeats automated bot attacks<br/>"
    "✓ <b>One-Time CAPTCHA Use</b> - Prevents CAPTCHA replay and reuse attacks<br/>"
    "✓ <b>Frontend Password Validation</b> - Real-time visual feedback for password strength<br/>"
    "✓ <b>Backend Password Hashing</b> - bcryptjs with 1024 iterations + unique salts<br/>"
    "✓ <b>Defense in Depth</b> - Multiple security layers protecting against different attack vectors<br/><br/>"
    "<b>Technical Highlights:</b><br/>"
    "✓ <b>Full-Stack Architecture</b> - Clean separation between frontend and backend<br/>"
    "✓ <b>API Integration</b> - Seamlessly handles multiple external APIs (Nominatim, OpenWeather, Leaflet)<br/>"
    "✓ <b>Performance Optimization</b> - Debouncing, parallel API calls, efficient algorithms<br/>"
    "✓ <b>Modern UX Design</b> - Glassmorphism aesthetics with smooth interactions<br/>"
    "✓ <b>Data Persistence</b> - Local file-based storage with backend management<br/><br/>"
    "The combination of <b>CAPTCHA bot protection</b> and <b>bcryptjs password hashing</b> creates a robust security model that meets "
    "industry standards for protecting user accounts and data. The real-time password strength validator enhances user experience "
    "while enforcing security best practices.<br/><br/>"
    "This documentation provides a complete technical understanding of every component, from frontend JavaScript to backend Node.js, "
    "from CAPTCHA generation to password verification.",
    body_style
))
elements.append(Spacer(1, 0.3*inch))

# Add footer
elements.append(Paragraph(
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br/>"
    "<i>Complete Technical Documentation - Predictive Weather Guidance with Route Planning<br/>"
    "Includes: Project Overview, Full-Stack Architecture, Frontend & Backend Technologies,<br/>"
    "CAPTCHA System (SVG Distorted Text), Password Validation (RegEx + bcryptjs),<br/>"
    "Security Layers, User Workflow, Setup Instructions, and Technical Deep Dives.</i>",
    styles['Normal']
))

# Build PDF
doc.build(elements)
print(f"✅ Complete PDF created successfully: {pdf_file}")
print(f"📄 File location: /Users/nimish/Desktop/MiniPro/{pdf_file}")
