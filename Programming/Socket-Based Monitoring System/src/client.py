import socket
import time
import platform
import os
import shutil

SERVER_HOST = "127.0.0.1"  # Change this to the server's IP if remote
SERVER_PORT = 9999         # Must match server port
INTERVAL_SECONDS = 5       # Time between sending metrics

def collect_system_metrics():
    """
    Gathers basic system metrics and returns them as a formatted string.
    """
    metrics = {
        "platform": platform.system(),
        "hostname": platform.node(),
        "cpu_count": os.cpu_count(),
        "disk_usage": shutil.disk_usage("/"),
        "load_avg": os.getloadavg() if hasattr(os, "getloadavg") else (0, 0, 0),
    }

    used_percent = (metrics["disk_usage"].used / metrics["disk_usage"].total) * 100

    return (
        f"System: {metrics['platform']} | "
        f"Host: {metrics['hostname']} | "
        f"CPU Cores: {metrics['cpu_count']} | "
        f"Load Avg: {metrics['load_avg']} | "
        f"Disk Usage: {used_percent:.2f}%"
    )

def start_client():
    """
    Connects to the server and sends system metrics at fixed intervals.
    Automatically retries if the server is unreachable.
    """
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((SERVER_HOST, SERVER_PORT))
                while True:
                    metrics = collect_system_metrics()
                    s.sendall(metrics.encode("utf-8"))
                    time.sleep(INTERVAL_SECONDS)
        except ConnectionRefusedError:
            print("Server not available. Retrying in 5 seconds...")
            time.sleep(5)
        except Exception as e:
            print(f"Client error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    start_client()
