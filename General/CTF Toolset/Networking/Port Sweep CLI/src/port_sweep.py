import socket
import argparse
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# Attempt a TCP connection to the given IP and port
def check_port(ip, port, timeout):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            print(f"[OPEN] {ip}:{port}")
    except:
        pass  # Ignore closed or unreachable IPs

# Parse IP range in CIDR or start-end format
def parse_ip_range(ip_range):
    if '/' in ip_range:
        # CIDR notation, e.g., 192.168.1.0/24
        return [str(ip) for ip in ipaddress.ip_network(ip_range, strict=False)]
    elif '-' in ip_range:
        # Start-end format, e.g., 10.0.0.1-10.0.0.50
        start_ip, end_ip = ip_range.split('-')
        start = ipaddress.IPv4Address(start_ip.strip())
        end = ipaddress.IPv4Address(end_ip.strip())
        return [str(ipaddress.IPv4Address(ip)) for ip in range(int(start), int(end) + 1)]
    else:
        return [ip_range.strip()]  # Single IP fallback

# Load IPs from a text file, one per line
def load_ips_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="Port Sweep Tool")
    parser.add_argument('--port', type=int, required=True, help='Target port to scan')
    parser.add_argument('--ip-range', help='CIDR or start-end IP range (e.g. 192.168.1.0/24 or 10.0.0.1-10.0.0.50)')
    parser.add_argument('--ip-file', help='Path to file containing IPs (one per line)')
    parser.add_argument('--timeout', type=float, default=1, help='Connection timeout in seconds (default: 1)')
    parser.add_argument('--threads', type=int, default=100, help='Number of concurrent threads (default: 100)')
    args = parser.parse_args()

    # Validate target IP list
    if args.ip_range:
        targets = parse_ip_range(args.ip_range)
    elif args.ip_file:
        targets = load_ips_from_file(args.ip_file)
    else:
        print("Error: Must provide either --ip-range or --ip-file")
        return

    # Start scanning using thread pool
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for ip in targets:
            executor.submit(check_port, ip, args.port, args.timeout)

if __name__ == "__main__":
    main()
