import serial
import time
import requests
from flask import Flask, render_template_string

app = Flask(__name__)

# Detect if the user is in a country using imperial units
def detect_unit_system():
    try:
        response = requests.get("https://ipapi.co/country/", timeout=2)
        country = response.text.strip()
        if country in ["US", "MM", "LR"]:
            return "imperial"
    except requests.RequestException:
        pass
    return "metric"

UNIT_SYSTEM = detect_unit_system()

# Read PM2.5 and PM10 from a USB/UART-connected sensor (e.g., SDS011, PMS5003)
def read_pm_sensor():
    try:
        with serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=2) as ser:
            while True:
                data = ser.read(10)
                if len(data) >= 10 and data[0] == 0xAA and data[1] == 0xC0:
                    pm25 = (data[2] + data[3] * 256) / 10.0
                    pm10 = (data[4] + data[5] * 256) / 10.0
                    return round(pm25, 1), round(pm10, 1)
    except Exception:
        pass
    return None, None

@app.route("/")
def index():
    pm25, pm10 = read_pm_sensor()

    html = """
    <html>
    <head><title>Air Quality Monitor</title></head>
    <body>
        <h1>Raspberry Pi Air Quality Monitor</h1>
        <p><b>PM2.5:</b> {{ pm25 }} µg/m³</p>
        <p><b>PM10:</b> {{ pm10 }} µg/m³</p>
        <p><b>Units:</b> {{ unit }}</p>
        <p><i>Auto-refreshes every 30 seconds</i></p>
        <meta http-equiv="refresh" content="30">
    </body>
    </html>
    """
    return render_template_string(html,
                                  pm25=pm25 or "N/A",
                                  pm10=pm10 or "N/A",
                                  unit="Imperial" if UNIT_SYSTEM == "imperial" else "Metric")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
