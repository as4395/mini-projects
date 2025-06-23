import sys
from collections import Counter
from scapy.all import rdpcap, TCP, UDP, ICMP, DNS, DNSQR, Raw, IP

def extract_protocol_counts(packets):
    # Count the number of packets per protocol type (TCP, UDP, ICMP).
    protocol_counts = Counter()
    for pkt in packets:
        if pkt.haslayer(TCP):
            protocol_counts['TCP'] += 1
        elif pkt.haslayer(UDP):
            protocol_counts['UDP'] += 1
        elif pkt.haslayer(ICMP):
            protocol_counts['ICMP'] += 1
        else:
            protocol_counts['Other'] += 1
    return protocol_counts

def extract_dns_queries(packets):
    # Extract unique DNS queries from packets.
    queries = set()
    for pkt in packets:
        if pkt.haslayer(DNS) and pkt.haslayer(DNSQR):
            try:
                queries.add(pkt[DNSQR].qname.decode())
            except Exception:
                continue
    return queries

def extract_basic_auth(packets):
    # Look for HTTP Basic Authentication headers in raw payloads.
    creds = []
    for pkt in packets:
        if pkt.haslayer(Raw):
            payload = pkt[Raw].load
            if b"Authorization: Basic " in payload:
                try:
                    line = payload.split(b"Authorization: Basic ")[1].split(b"\r\n")[0]
                    creds.append(line.decode())
                except Exception:
                    continue
    return creds

def extract_http_files(packets):
    # Identify HTTP GET requests and extract requested file paths.
    downloads = []
    for pkt in packets:
        if pkt.haslayer(Raw):
            payload = pkt[Raw].load
            if b"GET " in payload and b" HTTP/" in payload:
                try:
                    line = payload.split(b"GET ")[1].split(b" HTTP/")[0]
                    downloads.append(line.decode())
                except Exception:
                    continue
    return downloads

def extract_cleartext_passwords(packets):
    # Detect cleartext password leaks in payloads based on common parameter names.
    leaks = []
    for pkt in packets:
        if pkt.haslayer(Raw):
            payload = pkt[Raw].load.lower()
            for keyword in [b"password=", b"passwd=", b"pwd="]:
                if keyword in payload:
                    leaks.append(payload.decode(errors='ignore'))
    return leaks

def extract_top_ips(packets):
    # Identify the most frequent source IP addresses.
    ip_counts = Counter()
    for pkt in packets:
        if pkt.haslayer(IP):
            ip_counts[pkt[IP].src] += 1
    return ip_counts.most_common(5)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pcap_extract.py <file.pcap>")
        sys.exit(1)

    path = sys.argv[1]
    try:
        packets = rdpcap(path)
    except Exception as e:
        print(f"[!] Failed to read PCAP file: {e}")
        sys.exit(1)

    print("[+] Total packets:", len(packets))

    print("\n[+] Protocol Breakdown:")
    proto_counts = extract_protocol_counts(packets)
    for proto, count in proto_counts.items():
        print(f"  - {proto}: {count} packets")

    print("\n[+] Top Talkers:")
    for ip, count in extract_top_ips(packets):
        print(f"  - {ip}: {count} packets")

    print("\n[+] DNS Queries Found:")
    for domain in extract_dns_queries(packets):
        print(f"  - {domain}")

    print("\n[+] HTTP Basic Auth Credentials Found:")
    for cred in extract_basic_auth(packets):
        print(f"  - {cred}")

    print("\n[+] HTTP File Download Attempts:")
    for path in extract_http_files(packets):
        print(f"  - {path}")

    print("\n[+] Cleartext Password Indicators:")
    for leak in extract_cleartext_passwords(packets):
        print(f"  - {leak}")

if __name__ == "__main__":
    main()
