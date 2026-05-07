// API Key is now handled securely on the backend
// We fetch weather data through our local server

const map = L.map('map').setView([10.0, 76.2], 8);

L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>'
}).addTo(map);

let routingControl = null;

let routePoints = {
    start: null,
    mid: null,
    dest: null
};

const startInput = document.getElementById('start-input');
const destInput = document.getElementById('dest-input');
const currentLocBtn = document.getElementById('current-loc-btn');
const calculateBtn = document.getElementById('calculate-btn');
const viewDbBtn = document.getElementById('view-db-btn');
const departureTimeInput = document.getElementById('departure-time');
const setTimeBtn = document.getElementById('set-time-btn');

const dbModal = document.getElementById('db-modal');
const closeDbBtn = document.getElementById('close-db-btn');
const clearDbBtn = document.getElementById('clear-db-btn');
const historyTbody = document.getElementById('history-tbody');

const loginModal = document.getElementById('login-modal');
const closeLoginBtn = document.getElementById('close-login-btn');
const loginUsernameInput = document.getElementById('login-username');
const loginPasswordInput = document.getElementById('login-password');
const captchaImgContainer = document.getElementById('captcha-img-container');
const refreshCaptchaBtn = document.getElementById('refresh-captcha-btn');
const loginCaptchaInput = document.getElementById('login-captcha');
const submitLoginBtn = document.getElementById('submit-login-btn');
const loginError = document.getElementById('login-error');

let currentCaptchaId = null;

async function loadCaptcha() {
    try {
        captchaImgContainer.innerHTML = '<span style="color: rgba(255,255,255,0.5); font-size: 14px;">Loading...</span>';
        const res = await fetch('http://localhost:3000/api/captcha');
        const data = await res.json();
        currentCaptchaId = data.id;
        captchaImgContainer.innerHTML = data.svg;
    } catch (e) {
        captchaImgContainer.innerHTML = '<span style="color: #ef4444; font-size: 14px;">Error</span>';
    }
}

const toggleRegisterBtn = document.getElementById('toggle-register-btn');
const registrationPortal = document.getElementById('registration-portal');
const regUsername = document.getElementById('reg-username');
const regPassword = document.getElementById('reg-password');
const submitRegBtn = document.getElementById('submit-reg-btn');
const regMsg = document.getElementById('reg-msg');

const pwdReqLen = document.getElementById('pwd-req-len');
const pwdReqUpper = document.getElementById('pwd-req-upper');
const pwdReqLower = document.getElementById('pwd-req-lower');
const pwdReqNum = document.getElementById('pwd-req-num');
const pwdReqSpec = document.getElementById('pwd-req-spec');

const handleEnterKey = (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        calculateBtn.click();
    }
};

startInput.addEventListener('keydown', handleEnterKey);
destInput.addEventListener('keydown', handleEnterKey);
departureTimeInput.addEventListener('keydown', handleEnterKey);

const startSuggestions = document.getElementById('start-suggestions');
const destSuggestions = document.getElementById('dest-suggestions');

const routeSummary = document.getElementById('route-summary');
const summaryStart = document.getElementById('summary-start');
const summaryDest = document.getElementById('summary-dest');
const distVal = document.getElementById('dist-val');
const timeVal = document.getElementById('time-val');

const weatherSection = document.getElementById('weather-section');
const warningsSection = document.getElementById('warnings-section');

async function geocode(placeName) {
    try {
        const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(placeName)}`);
        const data = await response.json();
        if (data && data.length > 0) {
            return {
                lat: parseFloat(data[0].lat),
                lng: parseFloat(data[0].lon),
                name: data[0].display_name.split(',')[0]
            };
        }
        throw new Error(`Location not found: ${placeName}`);
    } catch (error) {
        console.error("Geocoding error:", error);
        alert(error.message);
        return null;
    }
}

function debounce(func, delay) {
    let timeoutId;
    return function (...args) {
        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            func.apply(this, args);
        }, delay);
    };
}

function setupAutocomplete(inputEl, suggestionsEl) {
    const handleInput = debounce(async (e) => {
        const query = e.target.value.trim();
        if (query.length < 3) {
            suggestionsEl.innerHTML = '';
            suggestionsEl.classList.add('hidden');
            return;
        }

        try {
            const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=5`);
            const results = await response.json();

            suggestionsEl.innerHTML = '';

            if (results && results.length > 0) {
                results.forEach(item => {
                    const div = document.createElement('div');
                    div.className = 'suggestion-item';
                    div.textContent = item.display_name;
                    div.addEventListener('click', () => {
                        const shortName = item.display_name.split(',')[0];
                        inputEl.value = shortName;
                        inputEl.dataset.lat = item.lat;
                        inputEl.dataset.lon = item.lon;
                        inputEl.dataset.text = shortName;
                        suggestionsEl.innerHTML = '';
                        suggestionsEl.classList.add('hidden');
                    });
                    suggestionsEl.appendChild(div);
                });
                suggestionsEl.classList.remove('hidden');
            } else {
                suggestionsEl.classList.add('hidden');
            }
        } catch (error) {
            console.error("Autocomplete error:", error);
        }
    }, 400);

    inputEl.addEventListener('input', (e) => {
        delete inputEl.dataset.lat;
        delete inputEl.dataset.lon;
        delete inputEl.dataset.text;
        handleInput(e);
    });

    document.addEventListener('click', (e) => {
        if (!inputEl.contains(e.target) && !suggestionsEl.contains(e.target)) {
            suggestionsEl.classList.add('hidden');
        }
    });
}

setupAutocomplete(startInput, startSuggestions);
setupAutocomplete(destInput, destSuggestions);

async function getCoordinates(inputEl) {
    const text = inputEl.value.trim();
    if (!text) return null;

    if (inputEl.dataset.lat && inputEl.dataset.lon && inputEl.dataset.text === text) {
        return {
            lat: parseFloat(inputEl.dataset.lat),
            lng: parseFloat(inputEl.dataset.lon),
            name: text
        };
    }
    return await geocode(text);
}

if (currentLocBtn) {
    currentLocBtn.addEventListener('click', () => {
        if (navigator.geolocation) {
            currentLocBtn.textContent = '⏳';
            navigator.geolocation.getCurrentPosition(async (position) => {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;

                let locName = "My Location";
                try {
                    const revRes = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`);
                    const revData = await revRes.json();
                    if (revData && revData.address) {
                        const addr = revData.address;
                        locName = addr.road || addr.suburb || addr.village || addr.town || "My Location";
                    }
                } catch (e) { }

                startInput.value = locName;
                startInput.dataset.lat = lat;
                startInput.dataset.lon = lon;
                startInput.dataset.text = locName;

                currentLocBtn.textContent = '🎯';
            }, (error) => {
                console.error("Geolocation error:", error);
                alert("Could not get your location. Please ensure location permissions are granted.");
                currentLocBtn.textContent = '🎯';
            });
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    });
}

let currentDepartureTime = null;

async function saveRouteToDatabase(record) {
    try {
        await fetch('http://localhost:3000/api/history', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(record)
        });
    } catch (error) {
        console.error("Could not save to database. Is the server running?", error);
    }
}

async function openDatabasePanel() {
    dbModal.classList.remove('hidden');
    historyTbody.innerHTML = '<tr><td colspan="7" style="text-align:center;">Loading...</td></tr>';
    
    const token = localStorage.getItem('token');
    if (!token) {
        historyTbody.innerHTML = '<tr><td colspan="7" style="text-align:center;color:#ef4444;">Not authenticated.</td></tr>';
        return;
    }

    try {
        const response = await fetch('http://localhost:3000/api/history', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        if (!response.ok) {
            if (response.status === 401 || response.status === 403) {
                 localStorage.removeItem('token'); // Clear invalid token
                 historyTbody.innerHTML = '<tr><td colspan="7" style="text-align:center;color:#ef4444;">Session expired. Please log in again.</td></tr>';
                 return;
            }
            throw new Error("Server error");
        }
        const data = await response.json();
        
        historyTbody.innerHTML = '';
        if (data.length === 0) {
            historyTbody.innerHTML = '<tr><td colspan="7" style="text-align:center;">No routes searched yet.</td></tr>';
            return;
        }
        
        data.forEach(item => {
            const tr = document.createElement('tr');
            const searchDate = new Date(item.timestamp).toLocaleString([], {month:'short', day:'numeric', hour:'2-digit', minute:'2-digit'});
            const depDate = item.departureTime ? new Date(item.departureTime).toLocaleString([], {month:'short', day:'numeric', hour:'2-digit', minute:'2-digit'}) : 'Now';
            
            tr.innerHTML = `
                <td>${searchDate}</td>
                <td>${item.startLocation}</td>
                <td>${item.destination}</td>
                <td>${depDate}</td>
                <td>${item.distanceKm} km</td>
                <td>${item.travelTimeMin} mins</td>
                <td style="font-size: 13px;">${item.weatherData || 'N/A'}</td>
            `;
            historyTbody.appendChild(tr);
        });
    } catch (error) {
        console.error("Error fetching database", error);
        historyTbody.innerHTML = '<tr><td colspan="7" style="text-align:center;color:#ef4444;">Error connecting to database. Is the server running?</td></tr>';
    }
}

if (viewDbBtn) {
    viewDbBtn.addEventListener('click', () => {
        const token = localStorage.getItem('token');
        if (token) {
            // Already logged in, open DB panel directly
            openDatabasePanel();
        } else {
            // Need to login
            loginModal.classList.remove('hidden');
            loginError.style.display = 'none';
            loginUsernameInput.value = '';
            loginPasswordInput.value = '';
            loginCaptchaInput.value = '';
            loadCaptcha();
        }
    });
}

if (closeLoginBtn) {
    closeLoginBtn.addEventListener('click', () => loginModal.classList.add('hidden'));
}

if (refreshCaptchaBtn) {
    refreshCaptchaBtn.addEventListener('click', loadCaptcha);
}

if (submitLoginBtn) {
    submitLoginBtn.addEventListener('click', async () => {
        const username = loginUsernameInput.value.trim();
        const password = loginPasswordInput.value.trim();
        const captchaAnswer = loginCaptchaInput.value.trim();
        
        if (!username || !password || !captchaAnswer) return;
        
        submitLoginBtn.textContent = 'Logging in...';
        try {
            const res = await fetch('http://localhost:3000/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password, captchaId: currentCaptchaId, captchaAnswer })
            });
            const data = await res.json();
            if (data.success) {
                localStorage.setItem('token', data.token); // Store token
                loginModal.classList.add('hidden');
                openDatabasePanel();
            } else {
                loginError.style.display = 'block';
                loginError.textContent = data.message;
                loginCaptchaInput.value = '';
                loadCaptcha();
            }
        } catch (error) {
            loginError.style.display = 'block';
            loginError.textContent = 'Server error. Is the backend running?';
        }
        submitLoginBtn.textContent = 'Login';
    });
}

// Registration Toggle
if (toggleRegisterBtn) {
    toggleRegisterBtn.addEventListener('click', () => {
        registrationPortal.classList.toggle('hidden');
    });
}

// Password Strength
function checkPasswordStrength(pwd) {
    const minLen = pwd.length >= 8;
    const hasUpper = /[A-Z]/.test(pwd);
    const hasLower = /[a-z]/.test(pwd);
    const hasNum = /[0-9]/.test(pwd);
    const hasSpec = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(pwd);

    pwdReqLen.innerHTML = minLen ? '✓ 8+ Chars' : '✗ 8+ Chars';
    pwdReqLen.style.color = minLen ? '#22c55e' : '#ef4444';

    pwdReqUpper.innerHTML = hasUpper ? '✓ Uppercase' : '✗ Uppercase';
    pwdReqUpper.style.color = hasUpper ? '#22c55e' : '#ef4444';

    pwdReqLower.innerHTML = hasLower ? '✓ Lowercase' : '✗ Lowercase';
    pwdReqLower.style.color = hasLower ? '#22c55e' : '#ef4444';

    pwdReqNum.innerHTML = hasNum ? '✓ Number' : '✗ Number';
    pwdReqNum.style.color = hasNum ? '#22c55e' : '#ef4444';

    pwdReqSpec.innerHTML = hasSpec ? '✓ Special Char' : '✗ Special Char';
    pwdReqSpec.style.color = hasSpec ? '#22c55e' : '#ef4444';

    return minLen && hasUpper && hasLower && hasNum && hasSpec;
}

if (regPassword) {
    regPassword.addEventListener('input', (e) => {
        const isStrong = checkPasswordStrength(e.target.value);
        submitRegBtn.disabled = !isStrong || regUsername.value.trim().length === 0;
    });
}
if (regUsername) {
    regUsername.addEventListener('input', (e) => {
        const isStrong = checkPasswordStrength(regPassword.value);
        submitRegBtn.disabled = !isStrong || e.target.value.trim().length === 0;
    });
}

if (submitRegBtn) {
    submitRegBtn.addEventListener('click', async () => {
        const username = regUsername.value.trim();
        const password = regPassword.value;
        
        submitRegBtn.textContent = 'Registering...';
        try {
            const res = await fetch('http://localhost:3000/api/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });
            const data = await res.json();
            regMsg.textContent = data.message;
            regMsg.style.color = data.success ? '#22c55e' : '#ef4444';
            if (data.success) {
                regUsername.value = '';
                regPassword.value = '';
                checkPasswordStrength('');
            }
        } catch (error) {
            regMsg.textContent = 'Server error. Is the backend running?';
            regMsg.style.color = '#ef4444';
        }
        submitRegBtn.textContent = 'Register';
    });
}

if (closeDbBtn) {
    closeDbBtn.addEventListener('click', () => {
        dbModal.classList.add('hidden');
    });
}

if (clearDbBtn) {
    clearDbBtn.addEventListener('click', async () => {
        if (!confirm("Are you sure you want to clear all history? This cannot be undone.")) return;
        
        clearDbBtn.textContent = 'Clearing...';
        try {
            const token = localStorage.getItem('token');
            const response = await fetch('http://localhost:3000/api/history', { 
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (!response.ok) throw new Error("Failed to clear");
            historyTbody.innerHTML = '<tr><td colspan="7" style="text-align:center;">No routes searched yet.</td></tr>';
        } catch (error) {
            console.error("Failed to clear database", error);
            alert("Failed to clear the database.");
        }
        clearDbBtn.textContent = 'Clear All';
    });
}

if (setTimeBtn) {
    setTimeBtn.addEventListener('click', () => {
        setTimeBtn.textContent = '✓ Set';
        setTimeBtn.style.background = 'rgba(34, 197, 94, 0.5)';
        setTimeout(() => {
            setTimeBtn.textContent = 'OK';
            setTimeBtn.style.background = '';
        }, 2000);
    });
}

calculateBtn.addEventListener('click', async () => {
    const startText = startInput.value.trim();
    const destText = destInput.value.trim();
    const depTimeVal = departureTimeInput.value;

    if (!startText || !destText) {
        alert("Please enter both start and destination locations.");
        return;
    }

    currentDepartureTime = depTimeVal ? new Date(depTimeVal).getTime() : Date.now();

    calculateBtn.textContent = "Planning...";
    calculateBtn.disabled = true;

    weatherSection.classList.add('hidden');
    warningsSection.innerHTML = '';
    warningsSection.classList.add('hidden');

    const startLoc = await getCoordinates(startInput);
    const destLoc = await getCoordinates(destInput);

    if (startLoc && destLoc) {
        summaryStart.textContent = startLoc.name;
        summaryDest.textContent = destLoc.name;
        calculateRoute(startLoc, destLoc);
    } else {
        resetRouteButton();
    }
});

let midRouteMarker = null;

function calculateRoute(startLoc, destLoc) {
    if (routingControl) {
        map.removeControl(routingControl);
    }
    if (midRouteMarker) {
        map.removeLayer(midRouteMarker);
    }

    routingControl = L.Routing.control({
        waypoints: [
            L.latLng(startLoc.lat, startLoc.lng),
            L.latLng(destLoc.lat, destLoc.lng)
        ],
        routeWhileDragging: false,
        addWaypoints: false,
        fitSelectedRoutes: true,
        lineOptions: {
            styles: [{ color: '#3b82f6', opacity: 0.9, weight: 6 }]
        }
    }).addTo(map);

    routingControl.on('routesfound', async function (e) {
        const routes = e.routes;
        const summary = routes[0].summary;
        const coordinates = routes[0].coordinates;

        const distanceKm = (summary.totalDistance / 1000).toFixed(1);
        const timeMin = Math.round(summary.totalTime / 60);

        distVal.textContent = `${distanceKm} km`;
        timeVal.textContent = `${timeMin} mins`;
        routeSummary.classList.remove('hidden');

        let totalPathDistance = 0;
        const distances = [0];
        for (let i = 1; i < coordinates.length; i++) {
            const p1 = L.latLng(coordinates[i - 1].lat, coordinates[i - 1].lng);
            const p2 = L.latLng(coordinates[i].lat, coordinates[i].lng);
            totalPathDistance += p1.distanceTo(p2);
            distances.push(totalPathDistance);
        }

        const targetMidDistance = totalPathDistance / 2;
        let midIndex = 0;
        for (let i = 0; i < distances.length; i++) {
            if (distances[i] >= targetMidDistance) {
                midIndex = i;
                break;
            }
        }

        const midLat = coordinates[midIndex].lat;
        const midLng = coordinates[midIndex].lng;

        let midName = "Midpoint";
        try {
            const revRes = await fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${midLat}&lon=${midLng}`);
            const revData = await revRes.json();
            if (revData && revData.address) {
                const addr = revData.address;
                midName = addr.village || addr.suburb || addr.town || addr.municipality || addr.city_district || addr.city || addr.county || "Midpoint";
            }
        } catch (e) { }

        midRouteMarker = L.marker([midLat, midLng]).addTo(map).bindPopup("Midpoint: " + midName);

        routePoints = {
            start: { lat: coordinates[0].lat, lng: coordinates[0].lng, name: startLoc.name },
            mid: { lat: midLat, lng: midLng, name: midName },
            dest: { lat: coordinates[coordinates.length - 1].lat, lng: coordinates[coordinates.length - 1].lng, name: destLoc.name }
        };

        const startMs = currentDepartureTime;
        const midMs = startMs + (summary.totalTime / 2 * 1000);
        const destMs = startMs + (summary.totalTime * 1000);

        const weatherSummary = await triggerWeatherPrediction(startMs, midMs, destMs);
        
        // Save to Database
        saveRouteToDatabase({
            startLocation: startLoc.name,
            destination: destLoc.name,
            departureTime: currentDepartureTime,
            distanceKm: distanceKm,
            travelTimeMin: timeMin,
            weatherData: weatherSummary ? `Start: ${weatherSummary.start}<br>Mid: ${weatherSummary.mid}<br>Dest: ${weatherSummary.dest}` : "N/A"
        });

        resetRouteButton();
    });

    routingControl.on('routingerror', function (e) {
        alert("Could not find a route between these locations.");
        resetRouteButton();
    });
}

function resetRouteButton() {
    calculateBtn.textContent = "Plan Route & Weather";
    calculateBtn.disabled = false;
}

async function triggerWeatherPrediction(startMs, midMs, destMs) {
    if (!routePoints.start || !routePoints.mid || !routePoints.dest) return;

    calculateBtn.textContent = "Fetching Weather...";

    const formatTime = (ms) => {
        const d = new Date(ms);
        return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + ', ' + d.toLocaleDateString([], { month: 'short', day: 'numeric' });
    };

    document.getElementById('start-loc-name').textContent = `(${routePoints.start.name})`;
    document.getElementById('start-time-label').textContent = `Departs: ${formatTime(startMs)}`;

    document.getElementById('mid-loc-name').textContent = `(${routePoints.mid.name})`;
    document.getElementById('mid-time-label').textContent = `Est. Arrival: ${formatTime(midMs)}`;

    document.getElementById('dest-loc-name').textContent = `(${routePoints.dest.name})`;
    document.getElementById('dest-time-label').textContent = `Est. Arrival: ${formatTime(destMs)}`;

    weatherSection.classList.remove('hidden');

    try {
        const [startData, midData, destData] = await Promise.all([
            fetchForecast(routePoints.start.lat, routePoints.start.lng),
            fetchForecast(routePoints.mid.lat, routePoints.mid.lng),
            fetchForecast(routePoints.dest.lat, routePoints.dest.lng)
        ]);

        const startWeather = getClosestForecast(startData, startMs);
        const midWeather = getClosestForecast(midData, midMs);
        const destWeather = getClosestForecast(destData, destMs);

        renderWeather('weather-start', startWeather);
        renderWeather('weather-mid', midWeather);
        renderWeather('weather-dest', destWeather);

        generateWarnings([startWeather, midWeather, destWeather]);

        return {
            start: startWeather && startWeather.weather ? `${Math.round(startWeather.main.temp)}°C, ${startWeather.weather[0].main}` : "N/A",
            mid: midWeather && midWeather.weather ? `${Math.round(midWeather.main.temp)}°C, ${midWeather.weather[0].main}` : "N/A",
            dest: destWeather && destWeather.weather ? `${Math.round(destWeather.main.temp)}°C, ${destWeather.weather[0].main}` : "N/A"
        };

    } catch (error) {
        console.error("Weather fetching error:", error);
        alert("Failed to fetch weather data. Please make sure your OpenWeather API key is set correctly.");
        return null;
    }
}

async function fetchForecast(lat, lng) {
    // Fetch from our local backend proxy instead of exposing API key
    const url = `http://localhost:3000/api/weather?lat=${lat}&lon=${lng}`;
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error("Weather API Error");
    }
    return await response.json();
}

function getClosestForecast(forecastData, targetTimeMs) {
    if (!forecastData || !forecastData.list || forecastData.list.length === 0) return null;

    const targetSec = targetTimeMs / 1000;

    return forecastData.list.reduce((prev, curr) => {
        return (Math.abs(curr.dt - targetSec) < Math.abs(prev.dt - targetSec) ? curr : prev);
    });
}

function renderWeather(elementId, weatherData) {
    const container = document.getElementById(elementId).querySelector('.weather-info');

    if (!weatherData || !weatherData.weather) {
        container.innerHTML = "Data unavailable";
        return;
    }

    const temp = Math.round(weatherData.main.temp);
    const desc = weatherData.weather[0].description;
    const iconCode = weatherData.weather[0].icon;
    const windSpeed = weatherData.wind.speed.toFixed(1);
    const humidity = weatherData.main.humidity;

    const forecastTimeStr = new Date(weatherData.dt * 1000).toLocaleString([], { weekday: 'short', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });

    container.innerHTML = `
        <div style="font-size: 11px; color: #64748b; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px;">Forecast for: ${forecastTimeStr}</div>
        <div class="weather-data-row">
            <div class="weather-main">
                <img src="https://openweathermap.org/img/wn/${iconCode}.png" alt="icon" width="40" height="40">
                <div>
                    <div class="weather-temp">${temp}°C</div>
                    <div class="weather-desc">${desc}</div>
                </div>
            </div>
            <div class="weather-details">
                <div>💨 ${windSpeed} m/s</div>
                <div>💧 ${humidity}%</div>
            </div>
        </div>
    `;
}

function generateWarnings(weatherArray) {
    const warnings = new Set();

    weatherArray.forEach(data => {
        if (!data || !data.weather) return;

        const weatherId = data.weather[0].id;
        const mainCond = data.weather[0].main;
        const windSpeed = data.wind.speed;

        if (weatherId >= 200 && weatherId < 300) {
            warnings.add("⛈️ Thunderstorm conditions detected on route. Drive with extreme caution.");
        }

        if ((weatherId >= 500 && weatherId < 600) || mainCond === "Rain") {
            warnings.add("🌧️ Rain expected on this part of the route. Roads may be slippery.");
        }

        if (weatherId >= 700 && weatherId < 800) {
            warnings.add("🌫️ Reduced visibility due to fog, mist, or haze. Use headlights.");
        }

        if (windSpeed > 10) {
            warnings.add("💨 Strong wind conditions detected. Maintain safe speeds.");
        }
    });

    if (warnings.size > 0) {
        warningsSection.classList.remove('hidden');
        warnings.forEach(msg => {
            const alertDiv = document.createElement('div');
            alertDiv.className = 'warning-alert';
            alertDiv.innerHTML = `<span class="warning-icon">⚠️</span> <span>${msg}</span>`;
            warningsSection.appendChild(alertDiv);
        });
    }
}
