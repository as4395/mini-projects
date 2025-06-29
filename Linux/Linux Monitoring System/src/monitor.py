#!/usr/bin/env python3

import time
import psutil
from rich.console import Console
from rich.table import Table

console = Console()

def display_stats():
    while True:
        table = Table(title="Linux System Monitor")

        table.add_column("Metric", justify="left", style="cyan")
        table.add_column("Value", justify="right", style="green")

        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        table.add_row("CPU Usage", f"{cpu}%")
        table.add_row("Memory Usage", f"{memory}%")
        table.add_row("Disk Usage", f"{disk}%")

        console.clear()
        console.print(table)
        time.sleep(2)

if __name__ == "__main__":
    try:
        display_stats()
    except KeyboardInterrupt:
        console.print("\n[bold red]Monitoring stopped by user.[/bold red]")
