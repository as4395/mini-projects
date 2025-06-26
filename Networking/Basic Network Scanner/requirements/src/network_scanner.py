import argparse
from scapy.all import ARP, Ether, srp

def parse_arguments():
    parser = argparse.ArgumentParser(description="Basic Network Scanner using ARP")
    parser.add_argument("-t", "--target", required=True, help="Target IP range (e.g., 192.168.1.0/24)")
    return parser.parse_args()

def scan(target):
    # Build ARP request wrapped in Ethernet frame (broadcast)
    arp_request = ARP(pdst=target)
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether_frame / arp_request

    # Send packet and receive responses
    result = srp(packet, timeout=2, verbose=0)[0]

    hosts = []
    for sent, received in result:
        hosts.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return hosts

def display_results(hosts):
    print("IP Address\t\tMAC Address")
    print("-" * 40)
    for host in hosts:
        print(f"{host['ip']}\t\t{host['mac']}")

def main():
    args = parse_arguments()
    try:
        print(f"[*] Scanning network: {args.target}")
        hosts = scan(args.target)
        if hosts:
            display_results(hosts)
        else:
            print("[!] No hosts found.")
    except PermissionError:
        print("[!] Run this script with sudo or as root.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
