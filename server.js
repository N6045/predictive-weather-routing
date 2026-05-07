const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');
const bcrypt = require('bcryptjs');
const svgCaptcha = require('svg-captcha');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const DB_FILE = path.join(__dirname, '.database.json');
const USERS_FILE = path.join(__dirname, '.users.json');

const activeCaptchas = new Map();

// Security middleware
app.use(helmet());
app.use(cors({
    origin: '*', // Be more specific in production
    methods: ['GET', 'POST', 'DELETE']
}));
app.use(express.json());

// Rate limiting
const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api/', limiter);

// Middleware to verify JWT token
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    if (token == null) return res.status(401).json({ success: false, message: "No token provided" });

    jwt.verify(token, process.env.JWT_SECRET || 'fallback_secret_key', (err, user) => {
        if (err) return res.status(403).json({ success: false, message: "Invalid or expired token" });
        req.user = user;
        next();
    });
};

function initUsersDB() {
    if (!fs.existsSync(USERS_FILE)) {
        const defaultAdmin = {
            username: 'admin',
            passwordHash: bcrypt.hashSync('AdminPassword123!', 10)
        };
        fs.writeFileSync(USERS_FILE, JSON.stringify([defaultAdmin], null, 2), 'utf8');
    }
}
initUsersDB();

function readUsers() {
    try { return JSON.parse(fs.readFileSync(USERS_FILE, 'utf8')); } 
    catch (e) { return []; }
}

function writeUsers(data) {
    fs.writeFileSync(USERS_FILE, JSON.stringify(data, null, 2), 'utf8');
}

// Helper to read DB
function readDatabase() {
    try {
        if (!fs.existsSync(DB_FILE)) {
            return [];
        }
        const data = fs.readFileSync(DB_FILE, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error("Error reading database:", error);
        return [];
    }
}

// Helper to write DB
function writeDatabase(data) {
    try {
        fs.writeFileSync(DB_FILE, JSON.stringify(data, null, 2), 'utf8');
    } catch (error) {
        console.error("Error writing database:", error);
    }
}

// Get all search history (protected)
app.get('/api/history', authenticateToken, (req, res) => {
    const history = readDatabase();
    res.json(history);
});

// Add to search history
app.post('/api/history', (req, res) => {
    const newRecord = req.body;
    
    // Add server timestamp if not provided by client
    if (!newRecord.timestamp) {
        newRecord.timestamp = new Date().toISOString();
    }

    const history = readDatabase();
    history.unshift(newRecord); // Add to beginning (newest first)
    
    writeDatabase(history);

    res.status(201).json({ message: "Record saved successfully", record: newRecord });
});

// Clear search history (protected)
app.delete('/api/history', authenticateToken, (req, res) => {
    writeDatabase([]);
    res.json({ message: "Database cleared successfully" });
});

// Captcha Endpoint
app.get('/api/captcha', (req, res) => {
    const captcha = svgCaptcha.create({
        size: 5,
        ignoreChars: '0o1il',
        noise: 2,
        color: true,
        background: '#1e293b' // Dark slate background to match theme
    });
    
    const captchaId = Date.now().toString() + Math.random().toString();
    activeCaptchas.set(captchaId, captcha.text.toLowerCase());
    
    // Auto cleanup after 5 minutes
    setTimeout(() => activeCaptchas.delete(captchaId), 5 * 60 * 1000);
    
    res.json({ id: captchaId, svg: captcha.data });
});

// Login
app.post('/api/login', (req, res) => {
    const { username, password, captchaId, captchaAnswer } = req.body;
    
    // Captcha validation
    const storedText = activeCaptchas.get(captchaId);
    if (!storedText || !captchaAnswer || storedText !== captchaAnswer.toLowerCase()) {
        return res.status(401).json({ success: false, message: "Invalid CAPTCHA" });
    }
    
    // Consume captcha
    activeCaptchas.delete(captchaId);

    const users = readUsers();
    const user = users.find(u => u.username === username);
    
    if (user && bcrypt.compareSync(password, user.passwordHash)) {
        // Generate JWT
        const token = jwt.sign({ username: user.username }, process.env.JWT_SECRET || 'fallback_secret_key', { expiresIn: '1h' });
        res.json({ success: true, message: "Login successful", token: token });
    } else {
        res.status(401).json({ success: false, message: "Invalid credentials" });
    }
});

// Register
app.post('/api/register', (req, res) => {
    const { username, password } = req.body;
    const users = readUsers();
    
    if (users.find(u => u.username === username)) {
        return res.status(400).json({ success: false, message: "Username already exists" });
    }
    
    users.push({
        username,
        passwordHash: bcrypt.hashSync(password, 10)
    });
    writeUsers(users);
    
    res.json({ success: true, message: "User registered successfully" });
});

// Proxy Weather API
app.get('/api/weather', async (req, res) => {
    const { lat, lon } = req.query;
    if (!lat || !lon) {
        return res.status(400).json({ error: 'Latitude and longitude are required' });
    }
    
    const apiKey = process.env.WEATHER_API_KEY;
    if (!apiKey) {
        return res.status(500).json({ error: 'Weather API key not configured' });
    }

    try {
        const url = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
        // dynamically import node-fetch if needed, or use native fetch in node 18+
        const response = await fetch(url);
        if (!response.ok) {
            return res.status(response.status).json({ error: 'Weather API returned an error' });
        }
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error("Error fetching weather:", error);
        res.status(500).json({ error: 'Failed to fetch weather data' });
    }
});

app.listen(PORT, () => {
    console.log(`Backend server running on http://localhost:${PORT}`);
    console.log(`Open your HTML file in the browser, and searches will be logged to database.json`);
});
