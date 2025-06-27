#!/usr/bin/env python3

import argparse
from scapy.all import sniff, TCP, Raw, IP
from scapy.layers.http import HTTPRequest, HTTPResponse
from scapy.layers.dns import DNS, DNSQR

# Protocol matchers and handlers for application layer inspection
def handle_http(packet):
    try:
        if packet.haslayer(HTTPRequest):
            host = packet[HTTPRequest].Host.decode()
            path = packet[HTTPRequest].Path.decode()
            print(f"[HTTP REQUEST] {host}{path}")
        elif packet.haslayer(HTTPResponse):
            print("[HTTP RESPONSE] Detected")
    except Exception:
        pass

def handle_dns(packet):
    if packet.haslayer(DNS) and packet.haslayer(DNSQR):
        query = packet[DNSQR].qname.decode()
        print(f"[DNS QUERY] {query}")

def handle_ftp(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")
        if any(cmd in payload.upper() for cmd in ["USER", "PASS", "STOR", "RETR"]):
            print(f"[FTP] {payload.strip()}")

# Packet inspection logic
def inspect_packet(packet):
    if not packet.haslayer(IP):
        return  # Skip non-IP packets

    ip_src = packet[IP].src
    ip_dst = packet[IP].dst
    proto = packet[IP].proto

    if packet.haslayer(TCP):
        dport = packet[TCP].dport
        sport = packet[TCP].sport

        print(f"\n[+] TCP Packet: {ip_src}:{sport} -> {ip_dst}:{dport}")
        
        # Application layer detection
        handle_http(packet)
        handle_dns(packet)
        handle_ftp(packet)

# CLI setup
def main():
    parser = argparse.ArgumentParser(description="Deep Packet Inspection Tool")
    parser.add_argument("-i", "--interface", required=True, help="Interface to sniff on")
    args = parser.parse_args()

    print(f"[*] Starting DPI on interface: {args.interface}")
    sniff(iface=args.interface, prn=inspect_packet, store=False)

if __name__ == "__main__":
    main()
