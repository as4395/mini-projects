# Command and Control (C2) Server

## Description
This project involves building a basic Command and Control (C2) server used by attackers to maintain communication with compromised machines in a network. The server accepts connections from client agents (bots), sends commands to them, and receives responses. This simplified implementation helps understand client-server communication, networking, and concurrency in a controlled environment.

## Features
- TCP-based server that listens for incoming client connections
- Handles multiple clients concurrently
- Send commands from server to connected clients
- Receives and displays responses from clients
- Basic client program to simulate compromised machines
- Simple command line interface on the server side

## Installation
Install the required Python packages by running:

```bash
pip install -r requirements/requirements.txt
```

## Usage

### Running the Server
From the src/python/ directory, run:

```bash
python c2_server.py
```
The server will start listening for incoming client connections.

### Running the Client
From the ```src/python/``` directory, run:

```bash
python c2_client.py
```
When connected, the client waits for commands from the server and executes them locally, returning the output.

## Notes

- This is a learning tool and should only be run in a controlled, authorized environment.
- No encryption or authentication is implemented; do not use in production or real networks.
- Commands executed on the client machine are run with the permissions of the user running the client.
- The server can handle multiple clients concurrently using threading.
= Communication between client and server uses TCP sockets.
