#!/usr/bin/env python3

import os
import subprocess

# Interfaces
WAN_IFACE = "eth0"
LAN_IFACE = "eth1"
LAN_SUBNET = "192.168.100.0/24"
LAN_IP = "192.168.100.1"

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

def enable_ip_forwarding():
    with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
        f.write("1")
    run_cmd("sysctl -w net.ipv4.ip_forward=1")

def configure_iptables():
    run_cmd(f"iptables -t nat -A POSTROUTING -o {WAN_IFACE} -j MASQUERADE")
    run_cmd(f"iptables -A FORWARD -i {WAN_IFACE} -o {LAN_IFACE} -m state --state RELATED,ESTABLISHED -j ACCEPT")
    run_cmd(f"iptables -A FORWARD -i {LAN_IFACE} -o {WAN_IFACE} -j ACCEPT")

def configure_lan_interface():
    run_cmd(f"ip addr add {LAN_IP}/24 dev {LAN_IFACE}")
    run_cmd(f"ip link set dev {LAN_IFACE} up")

def configure_dnsmasq():
    dnsmasq_conf = f"""
interface={LAN_IFACE}
dhcp-range=192.168.100.10,192.168.100.100,12h
domain-needed
bogus-priv
    """.strip()

    with open("/etc/dnsmasq.d/router.conf", "w") as f:
        f.write(dnsmasq_conf)

    run_cmd("systemctl restart dnsmasq")

def main():
    enable_ip_forwarding()
    configure_lan_interface()
    configure_iptables()
    configure_dnsmasq()
    print("[+] Router setup complete.")

if __name__ == "__main__":
    main()
