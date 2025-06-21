# MAC Flooding Program

## Description
This project demonstrates how MAC flooding can be used to exploit network switches by overwhelming their MAC address tables. It uses crafted Ethernet frames with randomized source MAC addresses to simulate a flooding attack, forcing a switch to behave like a hub and potentially expose sensitive traffic to unintended recipients.

## Features
- Sends a large number of forged Ethernet frames with random MAC addresses
- Customizable packet count and interval
- Targets a specific network interface
- Demonstrates how switch MAC address tables can be exhausted

## Installation
Install the required Python libraries by running:

```bash
pip install -r requirements/requirements.txt
```

Note: This script requires root/admin privileges to run because it sends raw packets.

## Usage

Run the script from the `src` directory:

```bash
cd src/
sudo python mac_flood.py -i eth0 -n 500 -d 0.1
```

Arguments:
- `-i` or `--interface`: Network interface to send packets on (e.g., eth0)
- `-n` or `--num`: Number of packets to send (default: 100)
- `-d` or `--delay`: Delay between packets in seconds (default: 0.05)

## Notes
- For educational and lab testing purposes only. Do not use on unauthorized networks.
- This is a simulation tool to help understand network vulnerabilities.
- Effectiveness depends on the behavior and configuration of the network switch.
