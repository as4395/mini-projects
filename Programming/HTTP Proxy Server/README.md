# HTTP Proxy Server (Python & Go)

## Description
This project provides two implementations of a simple HTTP proxy server that intercepts and forwards web traffic.  
The proxy inspects HTTP requests and responses to identify predefined suspicious keywords.

## Features
- Intercept and forward HTTP requests and responses.
- Detect suspicious content such as "password", "credit card", "login", "attack", and "malware".
- Support for HTTP/1.0 and HTTP/1.1.
- Multi-threaded in Python and concurrent in Go.
- Basic logging of detected suspicious content.

## Requirements

### Python Version
- Python 3

### Go Version
- Go 1.16 or newer

## Usage

### Python Proxy
```bash
cd src/python/
python3 http_proxy.py
# Configure your browser or system to use the proxy at localhost port 8888
```

### Go Proxy
```bash
cd src/go/
go build -o http_proxy
./http_proxy
# Configure your browser or system to use the proxy at localhost port 8888
```

### Notes
- This proxy handles HTTP traffic only (no HTTPS/TLS support).
- For educational and testing purposes only.
- Suspicious keywords can be customized in the code.
