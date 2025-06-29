# Raspberry Pi Weather Station

## Overview
This project builds a smart weather station using a Raspberry Pi. It reads sensor data (temperature, humidity, pressure) and **automatically switches between Imperial or Metric units** based on the user’s geographical location.

## Features
- Reads from DHT22 (temperature & humidity) and BMP280 (pressure)
- Uses IP-based geolocation to detect region
- Displays temperature in **Fahrenheit** or **Celsius**
- Displays pressure in **inHg** or **hPa** accordingly
- Logs data into CSV with units
- Real-time CLI output

## Hardware Requirements
- Raspberry Pi with GPIO
- DHT22 sensor
- BMP280 sensor (I2C)
- Jumper wires + breadboard

## Wiring

### DHT22
- VCC → 3.3V (Pin 1)
- DATA → GPIO4 (Pin 7)
- GND → GND (Pin 6)

### BMP280 (I2C)
- VCC → 3.3V (Pin 1)
- SDA → SDA (Pin 3)
- SCL → SCL (Pin 5)
- GND → GND (Pin 9)

## Setup

### 1. Enable I2C
```bash
sudo raspi-config
```
#### Interface Options > I2C > Enable
### 2. Install Required Packages
```bash
sudo apt update
sudo apt install -y python3-pip python3-smbus i2c-tools
pip3 install -r requirements.txt
```
### 3. Clone and Run
```bash
git clone https://github.com/as4395/Mini-Projects/RaspberryPi/weather-station.git
cd weather-station
python3 src/weather_station.py
```

## Output Example
```bash
[2025-06-29 15:20:00] Temp: 76.3°F | Humidity: 58.1% | Pressure: 29.88 inHg
```
or
```bash
[2025-06-29 15:20:00] Temp: 24.6°C | Humidity: 58.1% | Pressure: 1011.2 hPa
```

## Notes

- Uses [ipinfo.io](`ipinfo.io`)  to determine location
- Countries using imperial: US, Myanmar, Liberia
- All other countries default to metric units
- Data is logged with units in `weather_data.csv`
