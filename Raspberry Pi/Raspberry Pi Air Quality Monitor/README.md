# Raspberry Pi Air Quality Monitor

This project turns your Raspberry Pi into a real-time air quality monitor using a connected sensor (e.g., PMS5003 or SDS011). It reads PM2.5 and PM10 levels and displays them along with temperature and humidity, adjusting units based on your location (imperial for US/Myanmar/Liberia, metric elsewhere).

## Features

- Live particulate data (PM2.5 / PM10)
- Reads temperature and humidity
- Automatically switches between metric and imperial units
- Web dashboard for real-time monitoring
- Auto-refresh every 30 seconds

## Hardware Requirements

- Raspberry Pi (any model with GPIO)
- Air quality sensor (e.g., PMS5003, SDS011 via UART/USB)
- Optional: DHT22 sensor for temperature/humidity

## Installation

```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install -r requirements.txt
```

## Usage

```bash
python3 src/air_quality_monitor.py
```

Then open your browser to: `http://<RaspberryPi-IP>:5000`

## Output (Example)

```
Air Quality: Moderate
PM2.5: 38 µg/m³
PM10: 45 µg/m³
Temperature: 77.9°F
Humidity: 53%
```

## Notes

- The program detects your country via IP and displays units accordingly.
- You may need to enable UART on your Raspberry Pi for some sensors (via `raspi-config`).
