import socketserver
import threading
import time
from dnslib import DNSRecord, DNSHeader, DNSQuestion, RR, QTYPE, A
import os

BLOCKLIST_FILE = "adblock_domains.txt"
BLOCKLIST_UPDATE_INTERVAL = 24 * 60 * 60  # 24 hours in seconds
DNS_PORT = 53
BLOCKED_IP = "0.0.0.0"

class PiHoleDNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        request = DNSRecord.parse(data)
        qname = str(request.q.qname).rstrip(".")
        qtype = QTYPE[request.q.qtype]

        if qname in self.server.blocklist:
            # Build a DNS response with IP 0.0.0.0 to block
            reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=1), q=request.q)
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(BLOCKED_IP), ttl=60))
            socket.sendto(reply.pack(), self.client_address)
            print(f"[BLOCKED] {qname}")
        else:
            # Forward the query to upstream DNS server (e.g., 8.8.8.8)
            try:
                upstream_ip = "8.8.8.8"
                upstream_port = 53
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(5)
                sock.sendto(data, (upstream_ip, upstream_port))
                response, _ = sock.recvfrom(4096)
                socket.sendto(response, self.client_address)
                print(f"[ALLOWED] {qname}")
            except Exception as e:
                print(f"Upstream DNS query failed: {e}")
                # Respond with SERVFAIL
                reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, ra=1, rcode=2), q=request.q)
                socket.sendto(reply.pack(), self.client_address)


class PiHoleDNSServer(socketserver.ThreadingUDPServer):
    def __init__(self, server_address, handler_class):
        super().__init__(server_address, handler_class)
        self.blocklist = set()
        self.load_blocklist()

    def load_blocklist(self):
        if not os.path.exists(BLOCKLIST_FILE):
            print(f"Blocklist file {BLOCKLIST_FILE} not found. Run blocklist updater first.")
            self.blocklist = set()
            return
        with open(BLOCKLIST_FILE, "r") as f:
            self.blocklist = set(line.strip().lower() for line in f if line.strip())
        print(f"Loaded {len(self.blocklist)} domains from blocklist.")


def periodic_blocklist_update(server: PiHoleDNSServer, updater_module, interval: int):
    while True:
        print("Updating blocklist...")
        updater_module.update_blocklist()
        server.load_blocklist()
        time.sleep(interval)


def main():
    server = PiHoleDNSServer(("0.0.0.0", DNS_PORT), PiHoleDNSHandler)
    print(f"Starting Pi Hole DNS server on port {DNS_PORT}...")

    import blocklist_updater

    # Start blocklist updater thread
    updater_thread = threading.Thread(target=periodic_blocklist_update, args=(server, blocklist_updater, BLOCKLIST_UPDATE_INTERVAL), daemon=True)
    updater_thread.start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down DNS server.")


if __name__ == "__main__":
    main()
