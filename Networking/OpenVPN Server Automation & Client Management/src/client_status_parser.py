#!/usr/bin/env python3
import argparse
import os

def parse_status_log(path):
    if not os.path.exists(path):
        print(f"[!] Status log not found: {path}")
        return

    with open(path, "r") as f:
        lines = f.readlines()

    print("Connected OpenVPN Clients:")
    print("-" * 30)
    clients_section = False

    for line in lines:
        line = line.strip()
        if line.startswith("CLIENT_LIST"):
            clients_section = True
            parts = line.split(",")
            # CLIENT_LIST,CommonName,RealAddress,BytesReceived,BytesSent,ConnectedSince
            cn = parts[1]
            ip = parts[2]
            connected_since = parts[5]
            print(f"{cn:20} {ip:20} Connected since: {connected_since}")

def main():
    parser = argparse.ArgumentParser(description="Parse OpenVPN client status log")
    parser.add_argument("-s", "--status", required=True, help="Path to OpenVPN status log file")
    args = parser.parse_args()
    parse_status_log(args.status)

if __name__ == "__main__":
    main()
