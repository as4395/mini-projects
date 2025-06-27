#!/usr/bin/env python3

import subprocess
import os
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def run_command(command, shell=False):
    # Run a system command with subprocess and handle errors.
    try:
        subprocess.run(command, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error running command:[/red] {e}")
        exit(1)

def install_pivpn():
    # Install PiVPN using the official curl command.
    console.print("[bold cyan]Installing PiVPN...[/bold cyan]")
    run_command("curl -L https://install.pivpn.io | bash", shell=True)

def add_vpn_user():
    # Add a new VPN client user using pivpn add.
    username = Prompt.ask("[bold green]Enter a name for the VPN client[/bold green]")
    console.print(f"[yellow]Adding user:[/yellow] {username}")
    run_command(["pivpn", "add", "-n", username])
    return username

def export_conf(username):
    # Export the .conf file to a known location for the user.
    source_path = f"/home/pi/configs/{username}.conf"
    output_dir = "client_configs"
    os.makedirs(output_dir, exist_ok=True)
    dest_path = os.path.join(output_dir, f"{username}.conf")
    
    if os.path.exists(source_path):
        run_command(["cp", source_path, dest_path])
        console.print(f"[green]Client configuration saved to:[/green] {dest_path}")
    else:
        console.print(f"[red]Could not find config file at {source_path}[/red]")

def main():
    console.print("[bold blue]=== Raspberry Pi VPN Setup ===[/bold blue]")
    install_pivpn()
    username = add_vpn_user()
    export_conf(username)
    console.print("[bold green]VPN setup complete![/bold green]")

if __name__ == "__main__":
    if os.geteuid() != 0:
        console.print("[red]Please run this script with sudo.[/red]")
        exit(1)
    main()
