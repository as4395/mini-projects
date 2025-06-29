# Configure a Proxy in Linux

## Overview
This project sets up a Squid proxy server on a Linux system. Squid can be used to forward or reverse proxy web traffic and apply filtering rules, caching, or authentication.

## Features
- Forward proxy configuration (default)
- Block access to domains or keywords
- Enable caching of web pages
- Enable access control lists (ACLs)

## Setup

### 1. Install Squid
```bash
sudo apt update
sudo apt install squid -y
```

### 2. Clone the repository and apply the configuration
```bash
git clone https://github.com/as4395/Mini-Projects/Linux/squid-proxy.git
cd squid-proxy
sudo cp config/squid.conf /etc/squid/squid.conf
sudo systemctl restart squid
```

### 3. Verify
```bash
curl -x http://localhost:3128 http://example.com
```

## Requirements
- Ubuntu or Debian-based Linux system
- Root privileges

## Notes
This project only configures a forward HTTP proxy on port 3128. Adjust `squid.conf` as needed for advanced filtering, reverse proxying, or HTTPS interception.

## Default Block List
- facebook.com
- tiktok.com
- youtube.com
