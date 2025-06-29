import socketserver
import os
from datetime import datetime

LOG_DIR = "logs"

class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip().decode("utf-8", errors="replace")
        socket_used = self.request[1]
        hostname = self.client_address[0]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create log directory
        os.makedirs(LOG_DIR, exist_ok=True)
        log_filename = os.path.join(LOG_DIR, f"{hostname}.log")

        with open(log_filename, "a") as log_file:
            log_file.write(f"[{timestamp}] {data}\n")

        print(f"Log received from {hostname}: {data}")

if __name__ == "__main__":
    print("Starting Syslog server on UDP/514...")
    server = socketserver.UDPServer(("0.0.0.0", 514), SyslogUDPHandler)
    server.serve_forever()
