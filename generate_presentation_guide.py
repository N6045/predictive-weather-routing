#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors

pdf_file = "Presentation_Guide_Predictive_Weather.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch, leftMargin=0.75*inch, rightMargin=0.75*inch)

elements = []
styles = getSampleStyleSheet()

title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor('#1e40af'), spaceAfter=12, alignment=TA_CENTER, fontName='Helvetica-Bold')
heading_style = ParagraphStyle('CustomHeading', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#1e40af'), spaceAfter=10, spaceBefore=12, fontName='Helvetica-Bold')
subheading_style = ParagraphStyle('CustomSubHeading', parent=styles['Heading3'], fontSize=13, textColor=colors.HexColor('#2563eb'), spaceAfter=8, spaceBefore=8, fontName='Helvetica-Bold')
body_style = ParagraphStyle('CustomBody', parent=styles['BodyText'], fontSize=11, alignment=TA_JUSTIFY, spaceAfter=8, leading=14)
bullet_style = ParagraphStyle('BulletStyle', parent=styles['BodyText'], fontSize=11, spaceAfter=4, leading=14, leftIndent=10)

def add_title(text):
    elements.append(Paragraph(text, title_style))
    elements.append(Spacer(1, 0.2*inch))

def add_heading(text):
    elements.append(Paragraph(text, heading_style))

def add_subheading(text):
    elements.append(Paragraph(text, subheading_style))

def add_paragraph(text):
    elements.append(Paragraph(text, body_style))

def add_bullet(text):
    elements.append(Paragraph(f"• {text}", bullet_style))

# --- PAGE 1: Core System & Workflows ---
add_title("Presentation Guide: Predictive Weather Routing")
add_paragraph("This guide is designed to provide you with an in-depth understanding of your project for your presentation tomorrow. It covers the system's architecture, technologies, data models, APIs, and strategies for discussing your database choice.")

add_heading("1. Application Overview & Workflows")
add_paragraph("<b>What it does:</b> The application is a predictive weather routing dashboard. It doesn't just tell the user the weather at their destination *right now*; it calculates their driving time and predicts the weather at their destination *at the exact time they will arrive*. It also calculates a midpoint and predicts the weather there for when they pass through.")
add_paragraph("<b>How it works (The Core Workflow):</b>")
add_paragraph("1. <b>Input:</b> The user enters a Start, Destination, and Departure Time.")
add_paragraph("2. <b>Geocoding:</b> The app converts these location names into GPS coordinates (Latitude/Longitude).")
add_paragraph("3. <b>Routing:</b> It calculates the optimal driving route, total distance, and total travel time.")
add_paragraph("4. <b>Midpoint Extraction:</b> It analyzes the route polyline to find the exact halfway coordinate.")
add_paragraph("5. <b>Time Calculation:</b> It calculates the expected arrival time at the midpoint and destination.")
add_paragraph("6. <b>Weather Matching:</b> It fetches 5-day weather forecasts and matches the calculated arrival times to the closest 3-hour forecast block.")
add_paragraph("7. <b>Warning System:</b> It analyzes the weather data to generate safety warnings (e.g., thunderstorms, high winds, fog).")

add_heading("2. Technologies Used & Why")
add_paragraph("<b>Frontend: Vanilla JavaScript, HTML5, CSS3</b><br/><i>Why:</i> To maintain a lightweight, fast-loading application without the overhead of heavy frameworks like React or Angular. It demonstrates strong fundamental programming skills.")
add_paragraph("<b>Backend: Node.js with Express.js</b><br/><i>Why:</i> Using JavaScript on both the frontend and backend allows for a unified language ecosystem, making data serialization (JSON) seamless and development faster.")
add_paragraph("<b>Security: bcryptjs & svg-captcha</b><br/><i>Why:</i> `bcryptjs` provides industry-standard password hashing with salting to protect admin credentials. `svg-captcha` prevents automated bot attacks by generating dynamic, mathematically distorted vector graphics that defeat OCR tools.")

elements.append(PageBreak())

# --- PAGE 2: APIs & Data Types ---
add_heading("3. API Ecosystem Explained")
add_paragraph("Your application is heavily API-driven, orchestrating multiple external and internal APIs asynchronously.")

add_subheading("External APIs")
add_paragraph("• <b>Nominatim API (OpenStreetMap):</b> Used for Forward Geocoding (converting 'Kochi' to Lat/Lng) and Reverse Geocoding (converting the midpoint Lat/Lng back to a human-readable town name). <i>Workflow:</i> Called via debounced fetch requests for autocomplete.")
add_paragraph("• <b>Leaflet Routing Machine (OSRM Backend):</b> Used to calculate the polyline (driving path), distance, and duration. <i>Workflow:</i> Takes the start/end coordinates and returns a detailed array of waypoints representing the road network.")
add_paragraph("• <b>OpenWeather API (5-Day/3-Hour Forecast):</b> Used to get future weather. <i>Workflow:</i> Called concurrently using `Promise.all()` for the start, mid, and end points to reduce latency. Returns an array of forecasts every 3 hours.")

add_subheading("Internal APIs (Your Node.js Backend)")
add_paragraph("• <b>GET /api/captcha:</b> Generates a unique SVG string and ID. Clears from memory after 5 minutes.")
add_paragraph("• <b>POST /api/login:</b> Validates the CAPTCHA answer and bcrypt password hash.")
add_paragraph("• <b>GET & POST /api/history:</b> Reads and writes the route history to the JSON database.")

add_heading("4. Data Types & Structures")
add_paragraph("The application primarily relies on JSON objects, Arrays, and Promises.")
add_paragraph("<b>Route Coordinates Object:</b> `{ lat: Float, lng: Float, name: String }`")
add_paragraph("<b>Weather Forecast Array:</b> OpenWeather returns a list of objects containing Unix Timestamps (Integers), Temperature (Floats), and Weather Condition Arrays (Strings like 'Rain').")
add_paragraph("<b>History Database Record:</b>")
add_paragraph("`{`<br/>&nbsp;&nbsp;`startLocation: String,`<br/>&nbsp;&nbsp;`destination: String,`<br/>&nbsp;&nbsp;`departureTime: Integer (Unix Epoch Ms),`<br/>&nbsp;&nbsp;`distanceKm: String (Parsed Float),`<br/>&nbsp;&nbsp;`travelTimeMin: Integer,`<br/>&nbsp;&nbsp;`weatherData: String (HTML Formatted)`<br/>`}`")

elements.append(PageBreak())

# --- PAGE 3: The Database Strategy ---
add_heading("5. Database Strategy & Handling Questions")
add_paragraph("Your system uses a <b>File-based JSON Document Store</b> (`.database.json` and `.users.json`) rather than a relational SQL database like MySQL or PostgreSQL.")

add_subheading("Smart Ways to Steer Away from Relational Questions")
add_paragraph("If a panelist asks, 'Why didn't you use MySQL/PostgreSQL?' or 'How are your tables related?', you want to confidently pivot to the concept of Document/NoSQL databases.")
add_paragraph("<b>Pivot Strategy 1: Emphasize the Data Structure</b><br/>'For this specific use case, our data is entirely transactional and flat. A route search is a singular event—it doesn’t need to be joined with complex relational tables. Because the data structure natively mirrors JSON, a NoSQL Document approach was the most efficient architectural choice.'")
add_paragraph("<b>Pivot Strategy 2: Focus on Speed and Portability</b><br/>'We intentionally opted for a serverless/file-based document store to prioritize high read/write speeds for logging, zero-configuration portability, and to minimize overhead. It allowed us to focus our computing resources on the complex asynchronous API orchestrations rather than database management.'")

add_subheading("Good Technical Reasons for NOT Using a Relational DB Here")
add_bullet("<b>No Complex Relationships:</b> Relational databases excel when you have heavily linked data (e.g., Users -> Orders -> Products). Your history logs are independent events. There are no JOINs required.")
add_bullet("<b>Schema Flexibility:</b> JSON storage allows you to easily add new fields (like a new weather parameter) without needing to write database migration scripts or alter table schemas.")
add_bullet("<b>JSON Native:</b> Since the frontend and the OpenWeather API both communicate entirely in JSON, saving the data directly as JSON objects prevents the need for an ORM (Object-Relational Mapper) or constant data transformation/parsing.")
add_bullet("<b>Microservice Architecture Friendly:</b> In modern cloud deployments, lightweight, independent services often use document stores (like MongoDB or DynamoDB) rather than heavy relational servers.")

add_paragraph("<b>If they press the issue:</b> Acknowledge scalability. Say: 'While the current file-based document store is perfect for the prototype and handles current loads beautifully, the application architecture is highly decoupled. The data access layer in Express.js is isolated, meaning we could seamlessly swap the JSON store for MongoDB in production without altering the frontend or core logic.'")

doc.build(elements)
