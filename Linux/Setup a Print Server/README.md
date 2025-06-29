# Linux Print Server Setup

This project sets up a Linux print server using CUPS (Common Unix Printing System). It allows devices on your network to send print jobs to a centralized printer.

## Features

- CUPS-based print server
- Web-based interface (port 631)
- Printer sharing on LAN
- Optional configuration via CLI

## Requirements

- Linux (Debian-based preferred)
- CUPS
- Printer connected via USB or network

## Installation

```bash
sudo apt update
sudo apt install -y cups
sudo usermod -aG lpadmin $USER
```

## Configuration

```bash
sudo systemctl enable cups
sudo systemctl start cups
sudo cupsctl --remote-any
sudo systemctl restart cups
```

## Access Web Interface

Navigate to:  
[http://localhost:631](http://localhost:631)

## Adding Printers

Use the web interface or run:

```bash
lpadmin -p MyPrinter -E -v usb://Printer/Model -m everywhere
```

## Notes

- Ensure `cupsd.conf` allows access from your LAN.
- Configure firewall to allow TCP port 631.
