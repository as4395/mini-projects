import socket
import time
import os
import sys
import struct

MAX_HOPS = 30
TIMEOUT = 2.0
DEST_PORT = 33434

def build_icmp_packet():
    # Build a simple ICMP echo request packet.
    icmp_type = 8  # Echo Request
    code = 0
    checksum = 0
    identifier = os.getpid() & 0xFFFF
    sequence = 1
    header = struct.pack('!BBHHH', icmp_type, code, checksum, identifier, sequence)
    payload = b'CTFTraceroute'
    checksum = calc_checksum(header + payload)
    header = struct.pack('!BBHHH', icmp_type, code, checksum, identifier, sequence)
    return header + payload

def calc_checksum(data):
    # Compute checksum for ICMP packet.
    if len(data) % 2:
        data += b'\x00'
    res = sum(struct.unpack('!%dH' % (len(data) // 2), data))
    res = (res >> 16) + (res & 0xFFFF)
    res += res >> 16
    return ~res & 0xFFFF

def traceroute(dest_name):
    # Perform the traceroute logic.
    try:
        dest_ip = socket.gethostbyname(dest_name)
    except socket.gaierror:
        print(f"Error: Cannot resolve {dest_name}")
        sys.exit(1)

    print(f"Tracing route to {dest_name} [{dest_ip}] with max {MAX_HOPS} hops:\n")

    for ttl in range(1, MAX_HOPS + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as recv_socket, \
             socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) as send_socket:

            recv_socket.settimeout(TIMEOUT)
            recv_socket.bind(("", DEST_PORT))
            send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

            packet = build_icmp_packet()
            start_time = time.time()
            try:
                send_socket.sendto(packet, (dest_ip, DEST_PORT))
                _, curr_addr = recv_socket.recvfrom(512)
                end_time = time.time()
                rtt = (end_time - start_time) * 1000
                try:
                    host = socket.gethostbyaddr(curr_addr[0])[0]
                except socket.herror:
                    host = curr_addr[0]
                print(f"{ttl:2}  {host:<40}  {rtt:.2f} ms")
                if curr_addr[0] == dest_ip:
                    break
            except socket.timeout:
                print(f"{ttl:2}  * * * Request timed out.")
            except PermissionError:
                print("Error: Must run as root to use raw sockets.")
                sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: sudo python traceroute.py <hostname>")
        sys.exit(1)

    traceroute(sys.argv[1])

if __name__ == "__main__":
    main()
