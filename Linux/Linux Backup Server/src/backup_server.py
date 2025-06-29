#!/usr/bin/env python3

import os
import subprocess
import argparse
from datetime import datetime
from rich.console import Console

console = Console()

def run_backup(source, destination, log_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cmd = ["rsync", "-avh", "--delete", source, destination]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        console.print(f"[green]Backup succeeded at {timestamp}[/green]")
        log_entry = f"{timestamp} SUCCESS: {result.stdout}\n"
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Backup failed at {timestamp}[/red]")
        log_entry = f"{timestamp} ERROR: {e.stderr}\n"

    with open(log_file, "a") as f:
        f.write(log_entry)

def main():
    parser = argparse.ArgumentParser(description="Simple Backup Server using rsync")
    parser.add_argument("--source", required=True, help="Source directory to backup")
    parser.add_argument("--destination", required=True, help="Destination backup directory")
    parser.add_argument("--log", default="backup.log", help="Log file path")

    args = parser.parse_args()
    run_backup(args.source, args.destination, args.log)

if __name__ == "__main__":
    main()
