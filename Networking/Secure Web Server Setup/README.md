# Secure Web Server Setup

This project builds a secure web server using Python's Flask framework. It includes HTTPS support using self-signed SSL certificates, logging, and basic security best practices.

## Features

- HTTPS via self-signed certificate
- Simple static file serving
- Access logs
- Configurable via `config.yaml`

## Requirements

- Python 3.8+
- Flask
- OpenSSL (to generate certs)

## Setup Instructions

```bash
# Clone repository
git clone https://github.com/as4395/Mini-Projects/Networking/Web-Server/web-server.git
cd web-server
```

# Install dependencies
```bash
pip install -r requirements.txt
```

# Generate self-signed certs (only once)
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
```

# Start the server
```bash
python3 src/server.py
```

Visit `https://localhost:4443` in your browser.

## Note

This server is for local or lab use only.
