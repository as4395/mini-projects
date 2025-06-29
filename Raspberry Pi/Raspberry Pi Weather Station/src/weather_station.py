import Adafruit_DHT
import smbus2
import bme280
import time
import csv
import requests
from datetime import datetime

# Sensor Setup
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

PORT = 1
ADDRESS = 0x76
bus = smbus2.SMBus(PORT)
calibration_params = bme280.load_calibration_params(bus, ADDRESS)

# Countries that primarily use Imperial units
IMPERIAL_COUNTRIES = {"US", "MM", "LR"}

def detect_units():
    try:
        response = requests.get("https://ipinfo.io", timeout=5)
        country_code = response.json().get("country", "US").upper()
        return "imperial" if country_code in IMPERIAL_COUNTRIES else "metric"
    except:
        return "metric"  # Fallback default

def c_to_f(celsius):
    return round((celsius * 9 / 5) + 32, 2)

def hpa_to_inhg(hpa):
    return round(hpa * 0.02953, 2)

def read_sensors():
    humidity, temp_c = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    bme280_data = bme280.sample(bus, ADDRESS, calibration_params)
    pressure_hpa = bme280_data.pressure
    return temp_c, humidity, pressure_hpa

def log_data(timestamp, temp, humidity, pressure, temp_unit, pressure_unit):
    with open('weather_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, f"{temp} {temp_unit}", f"{humidity:.1f} %", f"{pressure} {pressure_unit}"])

def main():
    unit_system = detect_units()
    temp_unit = "°F" if unit_system == "imperial" else "°C"
    pressure_unit = "inHg" if unit_system == "imperial" else "hPa"

    print(f"Weather Station Started - Using {unit_system.title()} Units")

    while True:
        temp_c, humidity, pressure_hpa = read_sensors()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if temp_c is not None and humidity is not None:
            if unit_system == "imperial":
                temp = c_to_f(temp_c)
                pressure = hpa_to_inhg(pressure_hpa)
            else:
                temp = round(temp_c, 2)
                pressure = round(pressure_hpa, 2)

            print(f"[{timestamp}] Temp: {temp} {temp_unit} | Humidity: {humidity:.1f}% | Pressure: {pressure} {pressure_unit}")
            log_data(timestamp, temp, humidity, pressure, temp_unit, pressure_unit)
        else:
            print(f"[{timestamp}] Sensor read error.")

        time.sleep(10)

if __name__ == "__main__":
    main()
