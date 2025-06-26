import logging
from dnslib.server import DNSServer, DNSHandler, BaseResolver
from dnslib import RR, QTYPE, A, DNSHeader, DNSRecord
import datetime

# Define the static DNS zone
RECORDS = {
    "test.local.": "192.168.1.10",
    "example.local.": "192.168.1.11",
}

# Set up basic logging
logging.basicConfig(filename="dns_queries.log", level=logging.INFO, format="%(asctime)s - %(message)s")

class SecureResolver(BaseResolver):
    def resolve(self, request, handler):
        qname = request.q.qname
        qtype = QTYPE[request.q.qtype]
        domain = str(qname).lower()

        logging.info(f"Query received: {domain} ({qtype}) from {handler.client_address[0]}")

        # Reject recursive queries
        if request.header.rd:
            logging.warning(f"Ignored recursive query: {domain}")
            return DNSRecord(DNSHeader(id=request.header.id, qr=1, ra=0, rcode=5))  # Refused

        if qtype == 'A' and domain in RECORDS:
            ip = RECORDS[domain]
            reply = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1, ra=0), q=request.q)
            reply.add_answer(RR(rname=qname, rtype=QTYPE.A, rclass=1, ttl=60, rdata=A(ip)))
            return reply

        logging.warning(f"Domain not found: {domain}")
        return DNSRecord(DNSHeader(id=request.header.id, qr=1, ra=0, rcode=3))  # NXDOMAIN

if __name__ == "__main__":
    resolver = SecureResolver()
    server = DNSServer(resolver, port=53, address="0.0.0.0", tcp=False)
    try:
        print("[*] Starting DNS server on UDP port 53...")
        server.start()
    except PermissionError:
        print("[!] Permission denied: run with sudo or root.")
    except KeyboardInterrupt:
        print("\n[!] Server interrupted and stopped.")
