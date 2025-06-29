import requests
import json
import os
from datetime import datetime

# Country codes using Imperial by default
IMPERIAL_COUNTRIES = {"US", "MM", "LR"}

# Fetch public IP location to determine country
def detect_units():
    try:
        response = requests.get("https://ipinfo.io", timeout=5)
        country_code = response.json().get("country", "").upper()
        return "imperial" if country_code in IMPERIAL_COUNTRIES else "metric"
    except:
        return "metric"

# Fetch weather from OpenWeatherMap
def fetch_weather(units):
    api_key = "YOUR_API_KEY_HERE"
    city = "New York"  # You can make this dynamic
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)
    return response.json()

# Save to local file
def save_weather(data):
    os.makedirs("src/data", exist_ok=True)
    with open("src/data/weather.json", "w") as f:
        json.dump(data, f, indent=2)

def main():
    units = detect_units()
    data = fetch_weather(units)
    data["units"] = units
    data["fetched_at"] = datetime.utcnow().isoformat()
    save_weather(data)

if __name__ == "__main__":
    main()
