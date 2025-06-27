# Raspberry Pi Homelab with Docker

## Overview
This project guides you through setting up a lightweight homelab environment on a Raspberry Pi using Docker containers. You will install Docker, deploy multiple containerized services, and automate container management with a Python script.

## Features
- Install and configure Docker on Raspberry Pi OS.
- Deploy sample services such as:
  - Nginx web server
  - MariaDB database
  - Portainer for Docker container management UI
- Python script to automate starting, stopping, and checking the status of containers.
- Simple service health checks via the Python script.
- Basic instructions to extend and customize your homelab.

## Requirements
- Raspberry Pi 3 or newer (Pi OS installed)
- Internet connection
- Docker and Docker Compose installed (installation steps included)
- Python 3.8+ for automation script

## Installation and Setup

# 1. Update the system:
```bash
sudo apt update && sudo apt upgrade -y
```

# 2. Install Docker:
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

# 3. Log out and log back in to apply Docker group permissions.

# 4. Install Docker Compose (optional but recommended):
```bash
sudo apt-get install -y libffi-dev libssl-dev python3 python3-pip
sudo pip3 install docker-compose
```

# 5. Clone this repository and run the automation script:
```bash
git clone <your-repo-url>
cd <repo-folder>
python3 src/homelab_manager.py
```

## Usage

- Run the Python automation script to start, stop, or check the status of your homelab containers.
- Modify the `docker-compose.yml` to add/remove services.
- Access Portainer UI at  `http://<pi-ip>:9000` to manage containers visually.
- Access Nginx default page at `http://<pi-ip>:8080`

## Notes
- This is a basic homelab setup designed for learning container orchestration on Raspberry Pi.
- Extend this project by adding additional services or integrating Kubernetes for advanced orchestration.
