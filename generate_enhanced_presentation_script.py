#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors

pdf_file = "Enhanced_Presentation_Script.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch, leftMargin=0.75*inch, rightMargin=0.75*inch)

elements = []
styles = getSampleStyleSheet()

title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#1e40af'), spaceAfter=12, alignment=TA_CENTER, fontName='Helvetica-Bold')
slide_heading_style = ParagraphStyle('SlideHeading', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#dc2626'), spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold')
section_heading_style = ParagraphStyle('SectionHeading', parent=styles['Heading3'], fontSize=12, textColor=colors.HexColor('#2563eb'), spaceAfter=4, spaceBefore=4, fontName='Helvetica-Bold')
body_style = ParagraphStyle('CustomBody', parent=styles['BodyText'], fontSize=11, alignment=TA_LEFT, spaceAfter=8, leading=14)
italic_style = ParagraphStyle('CustomItalic', parent=styles['BodyText'], fontSize=10, fontName='Helvetica-Oblique', textColor=colors.HexColor('#4b5563'), spaceAfter=8, leading=13)

def add_title(text):
    elements.append(Paragraph(text, title_style))
    elements.append(Spacer(1, 0.2*inch))

def add_slide(title, what_to_say, behind_scenes=None):
    slide_content = []
    slide_content.append(Paragraph(title, slide_heading_style))
    slide_content.append(Paragraph("What to Say:", section_heading_style))
    slide_content.append(Paragraph(f"\"{what_to_say}\"", body_style))
    
    if behind_scenes:
        slide_content.append(Paragraph("Behind the Scenes / Explanation:", section_heading_style))
        slide_content.append(Paragraph(behind_scenes, italic_style))
    
    slide_content.append(Spacer(1, 0.2*inch))
    elements.append(KeepTogether(slide_content))

# --- Document Content ---
add_title("Presentation Script & Speaker Notes: Predictive Weather Guidance")
elements.append(Paragraph("This document is your complete guide to presenting your project. For every single slide, you will find a <b>'What to Say'</b> section (your actual script to speak out loud) and a <b>'Behind the Scenes / Explanation'</b> section (for your own understanding so you can answer questions confidently).", body_style))
elements.append(Spacer(1, 0.2*inch))

add_slide(
    "Slide 1: Title Slide",
    "Good morning everyone. Today, my team—Riya, Nandhakrishna, Pavithra, Nihal, and myself, Nimish—are excited to present our project: 'Predictive Weather Guidance with Route Engine'. It is a web application designed to make travel safer and more predictable.",
    "Stand confidently. This is just to introduce the team and the name of the project."
)

add_slide(
    "Slide 2: Introduction",
    "When we use navigation apps like Google Maps, they prioritize the shortest distance or the fastest time. However, they overlook a critical factor: the weather. Rain, fog, or storms heavily impact our safety and driving comfort. Right now, if you want to know the weather for your trip, you have to constantly switch between your map app and your weather app. Our project integrates both into a single seamless platform, allowing for smarter and safer travel planning."
)

add_slide(
    "Slide 3: Problem Statement",
    "The core problem we are addressing is that traditional route planners do not treat weather as a key decision factor. Origin-only weather data is insufficient because weather varies significantly along a route. If you drive from Kochi to Thrissur, the weather when you leave is different from the weather when you arrive. Users currently have to manually calculate their arrival times and manually check the weather at those specific times for multiple locations. We needed a system to automate this."
)

add_slide(
    "Slide 4: Aim of the Project",
    "The aim of our project is to develop a comprehensive web application that generates driving routes and accurately predicts the weather conditions along that path. Our goal is to enable users to make highly informed decisions before they even start their engines."
)

add_slide(
    "Slide 5: Objectives",
    "To achieve our aim, we set five clear objectives:<br/>1. Build an interactive, map-based web interface.<br/>2. Dynamically generate routes between a source and a destination.<br/>3. Automatically extract key coordinates, specifically the start, the exact midpoint, and the destination.<br/>4. Fetch real-time and forecasted weather data for these specific points.<br/>5. Display the route and the synchronized weather conditions together in a clear, user-friendly manner."
)

add_slide(
    "Slide 6: Literature Review (Introduction)",
    "Before building our system, we conducted a thorough literature review to understand existing solutions in smart navigation and identify their limitations. We analyzed several recent papers focusing on weather integration in routing.",
    "Use this slide as a brief transition to signal that your project is built on academic research, not just a random idea."
)

add_slide(
    "Slide 7: Literature Review (Kumar et al. & Smith et al.)",
    "First, we looked at Kumar et al., who developed a web-based navigation system with weather forecasting. However, their major limitation was that they only considered weather at the starting point and the destination, completely ignoring the conditions along the route.<br/><br/>Next, we reviewed Smith et al. They integrated real-time weather data into routes using mapping APIs, but they relied on static checkpoints. They did not dynamically adjust or synchronize the weather based on the traveler's specific time of arrival.",
    "You are setting up the problem here. Highlight the words 'ignoring the route' and 'static checkpoints'."
)

add_slide(
    "Slide 8: Literature Review (Lee et al.)",
    "Finally, we analyzed Lee et al., who highlighted the critical importance of real-time data in improving travel safety. While their theoretical framework was strong, their implementation lacked a detailed, user-friendly visualization of the weather conditions along the actual route.<br/><br/>By identifying these three limitations—ignoring the midpoint, lacking time synchronization, and poor visualization—we designed our system to specifically solve these gaps.",
    "This is your 'punchline' for the literature review. You are showing the panel exactly why your project is necessary and superior to past attempts."
)

add_slide(
    "Slide 9: Proposed System",
    "Our proposed system works like this: The user enters a start point, destination, and departure time. The app generates a route on an interactive map. We then sample the route geometry to find the exact midpoint. The app calculates exactly when the user will reach the start, midpoint, and destination, and requests the weather forecast for those specific times and locations. Finally, it displays weather cards and automatic safety warnings—like 'Strong Winds' or 'Rain'—beside the map."
)

elements.append(PageBreak())

add_slide(
    "Slide 10: Dataset",
    "For our data sources, we rely on a combination of highly accurate APIs rather than static local datasets. We use OpenStreetMap for the road network, Nominatim for converting city names to coordinates, OSRM for calculating the physical driving route, and the OpenWeather 5-day Forecast API to pull environmental data.",
    "If asked about Machine Learning / Model Training:<br/>You might wonder why we didn't train a machine learning model for this. The reason is that weather forecasting is a highly complex meteorological science requiring supercomputers and global satellite data. OpenWeather already runs these advanced predictive models. Our application is an intelligent Decision-Support System and API orchestrator. Our goal is not to predict raw weather from scratch, but rather to consume, synchronize, and contextualize that data against a dynamic routing algorithm (which uses Dijkstra's/A* pathfinding behind the scenes)."
)

add_slide(
    "Slide 11: Technology Stack",
    "Our technology stack is fully JavaScript-based. For the frontend, we used Vanilla JavaScript, HTML5, and CSS3. We intentionally avoided heavy frameworks to ensure a lightweight and incredibly fast user interface, demonstrating strong fundamental programming skills. We integrated Leaflet.js to render the interactive maps. For the backend, we used Node.js and Express.js to build our REST API, handling our database storage and security logic."
)

add_slide(
    "Slide 12: System Architecture",
    "Our architecture follows a standard Client-Server model. The Frontend handles all the UI, map rendering, and direct communication with external APIs like OpenWeather and OSRM. Once a route and weather prediction is complete, the frontend packages this data into JSON and sends it to our Node.js Backend via a RESTful API, where it is securely stored in our backend database for admin review."
)

add_slide(
    "Slide 13: Pseudocode - Road Mapping Algorithm",
    "Now, let's dive into the algorithms powering the system. Our first algorithm is the Road Mapping & Path Computation. When a user inputs locations, we geocode them into coordinates. If valid, we hit the OSRM routing service. The key part of this algorithm is how we find the midpoint. We extract the full array of coordinates that make up the driving path, calculate the total distance of that polyline, and programmatically find the exact coordinate that sits at the halfway distance mark. We then draw this path on the map.",
    "The 'midpoint' isn't just a straight line drawn through the air between City A and City B. It traces the actual curved road (the polyline) and finds the exact halfway driving distance."
)

add_slide(
    "Slide 14: Pseudocode - Weather Forecast Extraction",
    "The second algorithm handles Weather API Integration. Once we have the coordinates for the start, midpoint, and destination, we construct API URLs for OpenWeather. To maximize speed and reduce loading times for the user, we fetch the forecast data for all three locations simultaneously in parallel. We then extract and assign this data to variables for the next step.",
    "In your code, you use Promise.all() to fetch all three weather requests at the same time. Mentioning 'asynchronous parallel fetching' sounds very impressive."
)

add_slide(
    "Slide 15: Pseudocode - Route-Weather Synchronisation",
    "This is the most crucial algorithm in our system: Route-Weather Synchronisation. We take the user's departure time and add the driving duration to find the exact Arrival Time at the midpoint and the destination. OpenWeather provides forecasts in 3-hour blocks. For each location, our algorithm iterates through the forecast blocks, calculates the absolute time difference between the forecast time and our expected arrival time, and locks in the forecast that is closest to when the driver will actually be there.",
    "You are solving the 'time-travel' problem. If I drive for 4 hours, I need the weather 4 hours from now, not the weather right now."
)

elements.append(PageBreak())

add_slide(
    "Slide 16: Pseudocode - Backend Orchestration & API Delivery",
    "Our Backend Orchestration algorithm acts as the traffic controller for the data. It validates the geocoded coordinates, handles the OSRM route extraction, and fetches the weather data. Once the arrival times are computed and synchronized with the forecasts, this algorithm analyzes the weather conditions to generate safety warnings. Finally, it constructs a clean, structured JSON response containing the entire route and weather package.",
    "This algorithm ensures that raw data from 3 different APIs is cleaned up, calculated, and bundled into one neat package before it gets painted on the screen."
)

add_slide(
    "Slide 17: Pseudocode - Frontend Visualisation & UI",
    "Our Frontend Visualization algorithm handles the user experience. As the user types, it fetches location suggestions. When the route data is received from the backend, it clears any old UI elements, dynamically adjusts the map zoom to fit the entire route perfectly, and renders the weather cards. If our orchestration algorithm flagged any severe weather, it displays the warnings prominently on the screen.",
    "If asked about performance, mention 'Debouncing'. The app waits for the user to stop typing for 400 milliseconds before making a location search request, preventing API spam."
)

add_slide(
    "Slide 18: Backend Technologies & API Overview",
    "For our backend, we used Node.js with Express.js to create our API endpoints. We implemented a flat-file JSON Document database (.database.json).",
    "If asked why you didn't use SQL/Relational Database:<br/>We deliberately chose a JSON NoSQL approach over a traditional relational database like MySQL. A route search is a singular, flat transactional event. There are no complex relational entities—like Users having multiple Orders with multiple Products—that require SQL JOIN operations. Because our data structure natively mirrors JSON, storing it directly as JSON prevents the need for heavy Object-Relational Mappers (ORMs). This serverless, document-store approach minimizes overhead and makes the system incredibly fast and portable."
)

add_slide(
    "Slide 19: CAPTCHA & Password Security",
    "Security was a major priority for our admin database portal. First, we built a robust Password Validation system. The frontend requires 5 strict criteria (length, uppercase, lowercase, number, special char) with real-time visual feedback. On the backend, we never store plain-text passwords; they are cryptographically hashed using bcryptjs with salting. Second, we implemented a custom SVG CAPTCHA system to prevent bot attacks. The backend generates a mathematically distorted vector graphic that rotates and skews characters and adds noise lines. This completely defeats Optical Character Recognition (OCR) bots."
)

add_slide(
    "Slide 20: Workflow",
    "To summarize the entire workflow: The user inputs data -> The frontend geocodes it -> OSRM calculates the physical route -> The precise midpoint is extracted -> Future arrival times are calculated -> OpenWeather data is fetched and time-synchronized -> Safety warnings are generated -> The UI updates -> and finally, the record is securely saved to our backend JSON database."
)

add_slide(
    "Slide 21: Future Scope",
    "While our system is fully functional, there is exciting future scope. We aim to integrate live traffic data alongside weather for holistic planning. We want to implement Dynamic Route Adjustment—where the app automatically suggests a different road if a thunderstorm is detected on the primary route. Finally, we envision wrapping this web app into a dedicated mobile application with voice-assistance for hands-free updates while driving."
)

elements.append(PageBreak())

add_slide(
    "Slide 22: References",
    "Our project was built on the shoulders of excellent open-source technologies. We relied heavily on the official documentation for OpenStreetMap, the OSRM Routing API, OpenWeather, Nominatim for geocoding, and Leaflet.js for interactive mapping.",
    "Acknowledge the open-source community. It shows you know how to read and implement raw technical documentation."
)

add_slide(
    "Slide 23: Publications",
    "We also drew inspiration from various technical publications and developer blogs, particularly those detailing the integration of weather awareness into Google Maps and other navigation systems. These helped guide our logic for timeline synchronization and midpoint extraction."
)

add_slide(
    "Slide 24: Conclusion",
    "In conclusion, our Predictive Weather Route Planner successfully merges route navigation with time-synchronized weather forecasting into a single, intuitive interface. It solves a highly practical user need, prioritizes traveler safety, and demonstrates a robust integration of geospatial APIs, full-stack web technologies, and secure backend architecture. Thank you for your time. We are now open to any questions you may have."
)

doc.build(elements)
