import subprocess
import argparse
from rich import print

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"[green]Executed:[/green] {command}")
    except subprocess.CalledProcessError:
        print(f"[red]Failed:[/red] {command}")

def configure_iptables(args):
    if args.block_port:
        run_command(f"iptables -A INPUT -p tcp --dport {args.block_port} -j DROP")
    if args.allow_port:
        run_command(f"iptables -A INPUT -p tcp --dport {args.allow_port} -j ACCEPT")
    if args.flush:
        run_command("iptables -F")
    if args.list:
        run_command("iptables -L")

def configure_ufw(args):
    if args.block_port:
        run_command(f"ufw deny {args.block_port}")
    if args.allow_port:
        run_command(f"ufw allow {args.allow_port}")
    if args.enable:
        run_command("ufw enable")
    if args.status:
        run_command("ufw status verbose")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux Firewall Configurator")
    parser.add_argument("--mode", choices=["iptables", "ufw"], required=True)
    parser.add_argument("--allow-port", type=int, help="Allow specific port")
    parser.add_argument("--block-port", type=int, help="Block specific port")
    parser.add_argument("--flush", action="store_true", help="Flush rules (iptables only)")
    parser.add_argument("--list", action="store_true", help="List rules (iptables only)")
    parser.add_argument("--enable", action="store_true", help="Enable UFW (ufw only)")
    parser.add_argument("--status", action="store_true", help="UFW status (ufw only)")
    args = parser.parse_args()

    if args.mode == "iptables":
        configure_iptables(args)
    elif args.mode == "ufw":
        configure_ufw(args)
