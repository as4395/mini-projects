# Open Source Firewall Setup (Simulated pfSense)

This project sets up a basic open-source firewall using `iptables` on Linux. It includes a simple web interface for configuring common firewall rules. It simulates the behavior of a basic pfSense setup for educational purposes.

## Features

- Setup and flush iptables rules
- Allow/deny ports via a local Flask web UI
- Save and restore rule presets
- Basic logging of firewall events

## Requirements

- Python 3.8+
- Flask
- `iptables` (must be installed and run with sudo privileges)

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/as4395/Mini-Projects/Networking/Open-Source-Firewall/open-source-firewall.git
cd open-source-firewall
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Start the web UI (run as sudo for iptables access)
```bash
sudo python3 src/firewall_ui.py
```

Visit `http://localhost:5000` in your browser to manage firewall rules.

## Notes

- This is for local experimentation and learning. 
- Tested on Ubuntu and Debian-based systems.
