import socketserver
import socket

# List of keywords considered suspicious if found in HTTP traffic
SUSPICIOUS_KEYWORDS = ['password', 'credit card', 'login', 'attack', 'malware']

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

class ProxyHandler(socketserver.StreamRequestHandler):
    def handle(self):
        try:
            # Read the first line of the HTTP request (e.g., GET / HTTP/1.1)
            request_line = self.rfile.readline().decode('utf-8')
            if not request_line:
                return

            print(f"Request: {request_line.strip()}")

            # Parse the request line into method, path, and protocol
            method, path, protocol = request_line.strip().split()
            headers = {}

            # Read HTTP headers until empty line
            while True:
                line = self.rfile.readline().decode('utf-8').strip()
                if line == '':
                    break
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()

            host = headers.get('Host')
            if not host:
                print("Host header missing; cannot forward request.")
                return

            # Extract hostname and port if specified, default port 80
            if ':' in host:
                hostname, port = host.split(':')
                port = int(port)
            else:
                hostname = host
                port = 80

            # Open connection to destination server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.connect((hostname, port))

                # Rebuild and send the request to the server
                forward_request = f"{method} {path} {protocol}\r\n"
                for header_key, header_val in headers.items():
                    forward_request += f"{header_key}: {header_val}\r\n"
                forward_request += "\r\n"
                server_socket.sendall(forward_request.encode('utf-8'))

                # Receive the response from server
                response = b""
                while True:
                    chunk = server_socket.recv(4096)
                    if not chunk:
                        break
                    response += chunk

                # Separate headers and body to inspect for suspicious keywords
                try:
                    header_end = response.index(b"\r\n\r\n") + 4
                    body = response[header_end:].decode('utf-8', errors='ignore').lower()
                    for keyword in SUSPICIOUS_KEYWORDS:
                        if keyword in body:
                            print(f"Alert: Suspicious keyword detected: {keyword}")
                except ValueError:
                    # No header/body separation found
                    pass

                # Send response back to client
                self.wfile.write(response)

        except Exception as e:
            print(f"Error while handling request: {e}")

def main():
    server_address = ('localhost', 8888)
    print(f"Starting HTTP proxy server on {server_address[0]}:{server_address[1]}")
    with ThreadedTCPServer(server_address, ProxyHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    main()
