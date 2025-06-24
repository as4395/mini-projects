# Port Sweep Tool

## Description

A fast and lightweight CLI utility that performs port sweeping — checking whether a specific port is open across a range or list of IP addresses. This is particularly useful for identifying hosts running a known service (e.g., SSH on port 22, HTTP on port 80).

## Features

- Supports both CIDR and start–end IP range formats
- Accepts input from a file containing IP addresses
- Concurrent scanning using a thread pool for speed
- Customizable socket timeout and thread count
- Clear and minimal output of reachable hosts

## Usage

Run the tool using the following syntax:

```bash
python port_sweep.py --port <PORT> [--ip-range <RANGE> | --ip-file <FILE>] [--timeout <SECONDS>] [--threads <N>]
```

### Examples

Sweep port **22** across a **CIDR range**:
```bash
python port_sweep.py --port 22 --ip-range 192.168.1.0/24
```

Sweep port **80** using a **list of IPs from a file**:
```bash
python port_sweep.py --port 80 --ip-file ips.txt
```

Sweep port **80** across a **start–end IP range**:
```bash
python port_sweep.py --port 80 --ip-range 10.0.0.1-10.0.0.50
```

## Arguments

| Argument        | Description                                              | Required | Default |
|-----------------|----------------------------------------------------------|----------|---------|
| `--port`        | Target port to scan                                      | Yes      | —       |
| `--ip-range`    | IP range in CIDR (e.g. `192.168.0.0/24`) or start–end    | No*      | —       |
| `--ip-file`     | Path to a file with one IP per line                      | No*      | —       |
| `--timeout`     | Socket timeout in seconds                                | No       | `1`     |
| `--threads`     | Number of concurrent threads                             | No       | `100`   |

\* Either `--ip-range` or `--ip-file` must be provided.

## Output

Only hosts with the specified port open will be printed:

```
[OPEN] 192.168.1.10:22
[OPEN] 192.168.1.45:22
[OPEN] 10.0.0.3:80
```

No output means no hosts responded on that port within the timeout window.
