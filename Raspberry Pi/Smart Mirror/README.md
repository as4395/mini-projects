# Raspberry Pi Smart Mirror

## Overview
Build a modular Smart Mirror using a Raspberry Pi and an HDMI monitor. The mirror displays real-time information like time, date, weather, and news in a full-screen kiosk interface. A two-way acrylic mirror can be placed over the screen to reflect your image while displaying the data.

## Features

- Time and date display
- Live weather data with automatic unit detection (Imperial or Metric based on location)
- News headlines via RSS feed
- Kiosk mode for fullscreen display
- Clean and customizable HTML interface

## Hardware Requirements

- Raspberry Pi 3 or newer
- HDMI display
- Two-way mirror acrylic sheet (optional)
- Internet connection (Wi-Fi or Ethernet)

## Setup Instructions

### 1. Update System
```bash
sudo apt update && sudo apt upgrade -y
```
### 2. Install Dependencies
```bash
sudo apt install -y python3-pip unclutter chromium-browser
pip3 install -r requirements.txt
```
### 3. Enable Kiosk Mode (Autostart)
Create or edit the autostart file:
```bash
mkdir -p ~/.config/lxsession/LXDE-pi
nano ~/.config/lxsession/LXDE-pi/autostart
```
Add the following:
```bash
@xset s off
@xset -dpms
@xset s noblank
@unclutter -idle 0
@chromium-browser --noerrdialogs --kiosk file:///home/pi/Mini-Projects/RaspberryPi/smart-mirror/src/index.html
```
### 4. Clone and Run
```bash
git clone https://github.com/as4395/Mini-Projects.git
cd Mini-Projects/RaspberryPi/smart-mirror
python3 src/update_weather.py
```

# Notes

- Weather units auto-adjust: US, Myanmar, Liberia → Imperial; others → Metric
- Requires free API key from OpenWeatherMap
- You can extend functionality with calendar integration or voice controls
