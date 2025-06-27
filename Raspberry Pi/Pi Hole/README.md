# Pi Hole

Pi Hole is a Raspberry Pi-based DNS sinkhole that blocks advertisements by filtering DNS queries. It acts as a network-wide ad blocker by redirecting DNS requests for ad and tracker domains to a null IP address, effectively preventing ads from loading.

## Features

- Local DNS server running on Raspberry Pi
- Filters DNS queries using popular ad/tracking blocklists
- Customizable blocklist support
- Forwards allowed DNS requests to upstream DNS servers
- Lightweight and easy to run on low-power devices like Raspberry Pi

## Requirements

- Raspberry Pi running Raspberry Pi OS or any Debian-based Linux
- Python 3.8+
- Root privileges to bind DNS port 53 (run with `sudo`)
- Python packages: `dnslib`, `requests`

## Installation

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install dnslib requests
```
Clone the repository and run:
```bash
sudo python3 src/pi_hole_dns.py
```
Set your router or device DNS server to your Raspberry Pi IP to activate ad blocking.

## Updating Blocklists

Blocklists are automatically downloaded and cached on startup and refreshed every 24 hours.

## Usage

- Runs a DNS server on port 53 (UDP)
- Intercepts DNS queries for blocked domains and replies with 0.0.0.0
- Forwards other queries to upstream DNS server (default 8.8.8.8)

## Notes

- Requires running with elevated privileges ( `sudo`) to bind port 53
- Intended for local network use as a DNS ad blocker
- Inspired by the official Pi Hole project but implemented for educational purposes
