# Pi Hole

## Overview

Pi Hole is a local DNS server designed to block advertisements by blocking DNS queries to known ad-serving domains. It works by intercepting DNS queries and responding with a null IP for domains on a blocklist, effectively preventing ads from loading on all devices using this DNS.

This project uses a Raspberry Pi (or any Linux system) to run the DNS server, which downloads and aggregates multiple trusted blocklists automatically. It periodically updates the blocklist to keep blocking new ad domains.

## Features

- Lightweight DNS server implemented in Python
- Aggregates multiple public adblock lists into a single blocklist
- Blocks DNS queries to known ad/tracking/malware domains by returning 0.0.0.0
- Periodic update of blocklists (default: every 24 hours)
- Logs blocked queries and allowed queries
- Easy to configure for use as DNS on your network

## Requirements

- Python 3.9+ (tested with 3.9 and 3.10)
- Internet access for blocklist updates
- Raspberry Pi or any Linux machine for hosting

## Installation

**1.** Clone the repo:  
   ```bash
   git clone https://github.com/as4395/pi-hole-python.git
   cd pi-hole-python
   ```
**2.** Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
**3.** Run the DNS server:
   ```bash
   python3 src/pi_hole_dns.py
   ```
**4.** Configure your router or device to use your Raspberry Pi’s IP as DNS.

## Usage

- On first run, the program will download and aggregate multiple blocklists and store them in `dblock_domains.txt`.
- The DNS server will listen on UDP port 53 and respond to queries.
- It will block any domain in the blocklist by responding with IP `0.0.0.0`.
- Logs are printed to the console showing blocked and allowed requests.

## Customize
- Add/remove blocklist URLs in `src/blocklist_updater.py`
- Adjust update interval or DNS server port in s`rc/pi_hole_dns.py`
