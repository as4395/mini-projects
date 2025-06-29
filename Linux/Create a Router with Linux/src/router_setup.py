#!/usr/bin/env python3

import subprocess
import argparse
from rich.console import Console

console = Console()

def run(cmd):
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        console.print(f"[green]OK[/green] {' '.join(cmd)}")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]ERROR[/red] {' '.join(cmd)}\n{e.stderr.strip()}")
        exit(1)

def enable_routing(lan, wan):
    console.print("Enabling IP forwarding and NAT...")
    run(["sysctl", "-w", "net.ipv4.ip_forward=1"])
    run(["iptables", "-t", "nat", "-A", "POSTROUTING", "-o", wan, "-j", "MASQUERADE"])
    run(["iptables", "-A", "FORWARD", "-i", wan, "-o", lan, "-m", "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"])
    run(["iptables", "-A", "FORWARD", "-i", lan, "-o", wan, "-j", "ACCEPT"])
    console.print("[bold green]Router enabled.[/bold green]")

def disable_routing(lan, wan):
    console.print("Disabling routing and clearing rules...")
    run(["sysctl", "-w", "net.ipv4.ip_forward=0"])
    run(["iptables", "-t", "nat", "-D", "POSTROUTING", "-o", wan, "-j", "MASQUERADE"])
    run(["iptables", "-D", "FORWARD", "-i", wan, "-o", lan, "-m", "state", "--state", "RELATED,ESTABLISHED", "-j", "ACCEPT"])
    run(["iptables", "-D", "FORWARD", "-i", lan, "-o", wan, "-j", "ACCEPT"])
    console.print("[bold yellow]Router disabled.[/bold yellow]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux router script")
    parser.add_argument("--lan", required=True, help="LAN interface name")
    parser.add_argument("--wan", required=True, help="WAN interface name")
    parser.add_argument("--action", choices=["enable","disable"], required=True)
    args = parser.parse_args()

    if args.action == "enable":
        enable_routing(args.lan, args.wan)
    else:
        disable_routing(args.lan, args.wan)
