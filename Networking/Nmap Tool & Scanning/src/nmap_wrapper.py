import argparse
import nmap

def parse_arguments():
    parser = argparse.ArgumentParser(description="Nmap wrapper in Python")
    parser.add_argument("-t", "--target", required=True, help="Target IP or subnet (e.g., 192.168.1.1 or 192.168.1.0/24)")
    return parser.parse_args()

def run_scan(target):
    scanner = nmap.PortScanner()
    try:
        # Run Nmap scan with service/version detection
        scanner.scan(hosts=target, arguments="-sV")

        for host in scanner.all_hosts():
            print(f"\nHost: {host} ({scanner[host].hostname()})")
            print(f"State: {scanner[host].state()}")

            for proto in scanner[host].all_protocols():
                print(f"\nProtocol: {proto.upper()}")
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    port_data = scanner[host][proto][port]
                    state = port_data.get('state', 'unknown')
                    name = port_data.get('name', 'unknown')
                    product = port_data.get('product', '')
                    version = port_data.get('version', '')
                    extra = f"{product} {version}".strip()
                    print(f"  Port {port}: {state} - {name} {extra}")
    except Exception as e:
        print(f"[!] Error running scan: {e}")

def main():
    args = parse_arguments()
    run_scan(args.target)

if __name__ == "__main__":
    main()
