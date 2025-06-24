import socket
import struct
import argparse
import sys
import os

# Return readable hex + ASCII dump of data
def hexdump(data):
    result = []
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        hex_str = ' '.join(f'{b:02x}' for b in chunk)
        ascii_str = ''.join((chr(b) if 32 <= b <= 126 else '.') for b in chunk)
        result.append(f'{i:04x}  {hex_str:<48}  {ascii_str}')
    return '\n'.join(result)

# Parse Ethernet + IP + TCP/UDP/ICMP headers
def parse_packet(packet, proto_filter, show_hexdump):
    eth_proto = struct.unpack('!H', packet[12:14])[0]
    if eth_proto != 0x0800:
        return  # Only IPv4

    ip_header = packet[14:34]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    proto = iph[6]
    src_ip = socket.inet_ntoa(iph[8])
    dst_ip = socket.inet_ntoa(iph[9])
    proto_str = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}.get(proto, str(proto))

    if proto_filter and proto_str.lower() != proto_filter:
        return

    output = f"[{src_ip}] → [{dst_ip}] | {proto_str}"

    if proto == 6:  # TCP
        tcp_header = packet[34:54]
        tcph = struct.unpack('!HHLLBBHHH', tcp_header)
        src_port, dst_port, flags = tcph[0], tcph[1], tcph[5]
        flag_str = ''.join([
            f if flags & b else ''
            for f, b in zip('FSRPAUEC', [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80])
        ])
        output = f"[{src_ip}:{src_port}] → [{dst_ip}:{dst_port}] | TCP | Flags: {flag_str} | Len: {len(packet)}"
    elif proto == 17:  # UDP
        udp_header = packet[34:42]
        udph = struct.unpack('!HHHH', udp_header)
        src_port, dst_port = udph[0], udph[1]
        output = f"[{src_ip}:{src_port}] → [{dst_ip}:{dst_port}] | UDP | Len: {len(packet)}"
    elif proto == 1:  # ICMP
        output = f"[{src_ip}] → [{dst_ip}] | ICMP | Len: {len(packet)}"

    print(output)
    if show_hexdump:
        print(hexdump(packet))
        print()

def main():
    parser = argparse.ArgumentParser(description="Packet Sniffer CLI")
    parser.add_argument('--iface', help='Interface to sniff on (e.g. eth0)')
    parser.add_argument('--proto', choices=['tcp', 'udp', 'icmp', 'all'], default='all', help='Protocol filter')
    parser.add_argument('--hexdump', action='store_true', help='Show hex+ASCII payload dump')
    args = parser.parse_args()

    if os.geteuid() != 0:
        print("This tool must be run as root (for raw sockets).")
        sys.exit(1)

    try:
        if args.iface:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
            s.bind((args.iface, 0))
        else:
            s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except Exception as e:
        print(f"Error creating raw socket: {e}")
        sys.exit(1)

    while True:
        packet, _ = s.recvfrom(65565)
        parse_packet(packet, args.proto if args.proto != 'all' else None, args.hexdump)

if __name__ == "__main__":
    main()
