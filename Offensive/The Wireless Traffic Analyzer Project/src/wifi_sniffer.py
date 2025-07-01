import argparse
from scapy.all import sniff, Dot11
from datetime import datetime

access_points = {}
clients = {}

def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        mac_addr = pkt.addr2
        bssid = pkt.addr3

        if pkt.type == 0 and pkt.subtype == 8:  # Beacon frame (AP)
            ssid = pkt.info.decode(errors='ignore')
            if mac_addr not in access_points:
                access_points[mac_addr] = ssid
                print(f"[AP] {ssid} - {mac_addr}")

        elif pkt.type == 0 and pkt.subtype == 4:  # Probe Request (Client)
            if mac_addr and bssid:
                if mac_addr not in clients:
                    clients[mac_addr] = bssid
                    print(f"[Client] {mac_addr} --> {bssid}")

def main(interface, output):
    print(f"[+] Starting wireless sniffing on interface: {interface}")
    try:
        sniff(iface=interface, prn=packet_handler, store=0)
    except KeyboardInterrupt:
        print("\n[+] Stopping sniffing...")
        if output:
            with open(output, "w") as f:
                f.write("Access Points:\n")
                for mac, ssid in access_points.items():
                    f.write(f"{ssid} - {mac}\n")
                f.write("\nClients:\n")
                for client, bssid in clients.items():
                    f.write(f"{client} --> {bssid}\n")
            print(f"[+] Results saved to {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wireless Traffic Analyzer")
    parser.add_argument("--interface", required=True, help="Monitor-mode wireless interface (e.g., wlan0mon)")
    parser.add_argument("--output", help="Optional output file to save results")
    args = parser.parse_args()

    main(args.interface, args.output)
