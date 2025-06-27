#!/usr/bin/env python3

import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="Raspberry Pi Network Scanner using ARP")
    parser.add_argument("-t", "--target", required=True, help="Target IP range (e.g., 192.168.1.1/24)")
    return parser.parse_args()


def scan(ip_range):
    """
    Send ARP requests to the specified IP range and collect responses.
    Returns a list of dictionaries with IP and MAC addresses.
    """
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast = broadcast / arp_request

    answered_list = scapy.srp(arp_broadcast, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in answered_list:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })
    return devices


def display_result(devices):
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")


if __name__ == "__main__":
    args = get_arguments()
    scanned_devices = scan(args.target)
    display_result(scanned_devices)
