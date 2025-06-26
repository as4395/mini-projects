import argparse
from scapy.all import sniff, IP, TCP, UDP, ICMP

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Packet Sniffer using Scapy")
    parser.add_argument("-i", "--interface", required=True, help="Network interface to sniff on (e.g., eth0)")
    return parser.parse_args()

def packet_callback(packet):
    # Process only IPv4 packets
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        # Identify protocol and extract relevant port info
        if TCP in packet:
            proto_name = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif UDP in packet:
            proto_name = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        elif ICMP in packet:
            proto_name = "ICMP"
            sport = "-"
            dport = "-"
        else:
            proto_name = f"Proto-{proto}"
            sport = "-"
            dport = "-"

        print(f"[{proto_name}] {src}:{sport} --> {dst}:{dport}")

def main():
    args = parse_arguments()
    try:
        print(f"[*] Sniffing on interface: {args.interface}")
        sniff(iface=args.interface, prn=packet_callback, store=False)
    except PermissionError:
        print("[!] Permission denied: run this script with sudo or as root.")
    except KeyboardInterrupt:
        print("\n[!] Packet sniffing stopped.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
