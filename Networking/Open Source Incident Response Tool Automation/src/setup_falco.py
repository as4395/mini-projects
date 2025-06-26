#!/usr/bin/env python3
import subprocess
import sys
import os

def run(cmd, shell=False):
    # Run a system command and exit if it fails.
    print(f"[+] Executing: {cmd if isinstance(cmd, str) else ' '.join(cmd)}")
    result = subprocess.run(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"[!] Error:\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def install_falco():
    print("[*] Installing Falco on Ubuntu/Debian-based system...")

    # Add Falco GPG key
    run("curl -s https://falco.org/repo/falcosecurity-packages.asc | sudo apt-key add -", shell=True)

    # Add Falco apt repository
    falco_repo = "deb https://download.falco.org/packages/deb stable main"
    repo_file = "/etc/apt/sources.list.d/falcosecurity.list"
    if not os.path.exists(repo_file):
        run(f'echo "{falco_repo}" | sudo tee {repo_file}', shell=True)

    # Update apt and install
    run(["sudo", "apt", "update"])
    run(["sudo", "apt", "install", "-y", "falco"])

    # Enable and start Falco service
    run(["sudo", "systemctl", "enable", "falco"])
    run(["sudo", "systemctl", "start", "falco"])

    print("[+] Falco installed and running.")
    print("[+] Logs can be found at: /var/log/falco.log")

if __name__ == "__main__":
    install_falco()
