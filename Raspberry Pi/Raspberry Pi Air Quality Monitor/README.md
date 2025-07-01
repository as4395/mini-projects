# Raspberry Pi Air Quality Monitor

This project allows you to measure and log air quality data using a Raspberry Pi connected to an MQ-135 gas sensor (or equivalent). Data is logged locally and optionally displayed on a web interface.

## Features

- Read data from MQ-135 (or similar air quality sensor)
- Store historical readings
- Optional lightweight Flask web interface
- Supports Celsius or Fahrenheit (auto-detects region)

## Hardware Requirements

- MQ-135 gas sensor or compatible analog air sensor
- MCP3008 ADC (for analog sensors)
- Raspberry Pi (any model with GPIO)

## Installation

```bash
sudo apt update
sudo apt install python3-gpiozero python3-flask
```

## Setup

```bash
git clone https://github.com/as4395/Mini-Projects.git
cd Mini-Projects/RaspberryPi/air-quality-monitor
python3 src/air_quality_monitor.py
```
To run the web interface:
```bash
python3 src/web_interface.py
```

## Output

- Air quality data logs saved to `logs/data.csv`
- Web interface available at `http://<Raspberry_Pi_IP>:5000`

## Notes

- System auto-detects imperial vs metric units based on locale.
