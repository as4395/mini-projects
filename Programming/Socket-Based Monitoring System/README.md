# Socket-Based Monitoring System

## Description
This project implements a simple client-server architecture using socket programming to build a real-time monitoring system. The client collects system metrics (such as CPU and memory usage) and sends them to the server at regular intervals. The server receives, logs, and displays the incoming data in real time.

This project demonstrates how two nodes on a network can communicate using TCP sockets, which is foundational for many cybersecurity and networking applications.

## Features

### Client
- Connects to a central monitoring server
- Collects system metrics using Python's standard libraries
- Sends metrics over TCP at regular intervals
- Handles reconnection gracefully

### Server
- Accepts multiple client connections using threading
- Displays incoming metrics with timestamps and client identification
- Logs all received data to a local file
- Thread-safe and efficient under concurrent load

## Getting Started

### 1. Install Requirements
Install Python dependencies (if any) from the requirements file:

```bash
pip install -r requirements/requirements.txt
```

### 2. Start the Server
Run the server from the `src/` directory:

```bash
cd src/
python server.py
```

### 3. Run the Client
In a separate terminal or from another machine:

```bash
cd src/
python client.py
```

Metrics from the client will appear in the server console and be saved to a log file.

## Notes
- The server listens on `localhost:9999` by default. Modify the `HOST` and `PORT` variables in the code to suit your network.
- The client reports data every 5 seconds. You can change the reporting interval as needed.
