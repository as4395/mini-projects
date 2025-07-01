# Raspberry Pi Retro Gaming Console

Transform your Raspberry Pi into a full-fledged retro gaming console using RetroPie. This setup enables users to play classic games from consoles like NES, SNES, Sega Genesis, Game Boy, and more using emulation software.

## Features

- RetroPie installation and configuration
- USB or network-based ROM transfer support
- Controller setup automation
- Custom startup script to auto-launch the gaming interface

## Requirements

- Raspberry Pi 3/4 (with microSD card)
- Gamepad/Controller (USB or Bluetooth)
- HDMI display
- USB keyboard (for setup)
- ROM files (must be legally owned)

## Installation Steps

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install RetroPie setup script
sudo apt install -y git
git clone --depth=1 https://github.com/RetroPie/RetroPie-Setup.git
cd RetroPie-Setup
chmod +x retropie_setup.sh
sudo ./retropie_setup.sh
```

Follow the menu to install RetroPie packages.

## Optional: Enable SSH ROM Transfers

```bash
sudo raspi-config
# Enable SSH under "Interfacing Options"
```

## Controller Setup

After reboot, connect your controller and follow the on-screen instructions to map buttons.

## Startup Configuration

```bash
sudo cp config/startup.sh /etc/profile.d/retropie-launch.sh
```

This will automatically launch EmulationStation on boot.

## Legal Notice

You are responsible for obtaining and using ROMs legally. Only use backups of games you personally own.
