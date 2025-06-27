# Wireless Attack Automation Toolkit

This project automates wireless network attack operations using Python wrappers for tools like `aircrack-ng`, `airodump-ng`, and `aireplay-ng`. It provides a simple CLI to perform scanning, monitoring, deauthentication, and cracking WPA/WPA2 passwords.

## Features

- Discover nearby wireless networks and clients
- Enable monitor mode on a wireless interface
- Capture handshakes using `airodump-ng`
- Send deauthentication packets using `aireplay-ng`
- Crack captured handshakes using `aircrack-ng` and a wordlist

## Usage

### 1. Install dependencies
```bash
sudo apt update
sudo apt install aircrack-ng
```
### 2. Run the tool
```bash
sudo python3 src/wireless_attack.py
```
### 3. Follow CLI menu options to:
- Enable monitor mode
- Scan for targets
- Capture WPA handshakes
- Launch deauth attack
- Crack captured handshake file

## Requirements
- Python 3.8+
- Linux with `aircrack-ng` tools
- Wireless adapter supporting monitor mode
  
**Note:** Use this tool only in controlled, legal environments like your own test lab.
