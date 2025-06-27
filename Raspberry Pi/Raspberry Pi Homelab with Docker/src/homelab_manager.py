#!/usr/bin/env python3

import subprocess
import sys


CONTAINERS = ["nginx_homelab", "mariadb_homelab", "portainer_homelab"]


def run_command(command):
    # Run a shell command and return the output.
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr.strip()}")
        return None


def start_containers():
    print("Starting homelab containers...")
    output = run_command("docker-compose up -d")
    if output is not None:
        print(output)
    else:
        print("Failed to start containers.")


def stop_containers():
    print("Stopping homelab containers...")
    output = run_command("docker-compose down")
    if output is not None:
        print(output)
    else:
        print("Failed to stop containers.")


def status_containers():
    print("Checking container statuses...")
    for container in CONTAINERS:
        output = run_command(f"docker ps --filter 'name={container}' --format '{{{{.Names}}}}: {{{{.Status}}}}'")
        if output:
            print(output)
        else:
            print(f"Container {container} is not running.")


def usage():
    print("Usage: python3 homelab_manager.py [start|stop|status]")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        usage()

    command = sys.argv[1].lower()
    if command == "start":
        start_containers()
    elif command == "stop":
        stop_containers()
    elif command == "status":
        status_containers()
    else:
        usage()


if __name__ == "__main__":
    main()
