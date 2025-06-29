#!/usr/bin/env python3

import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def setup_cups():
    print("[+] Installing CUPS...")
    run("sudo apt update && sudo apt install -y cups")
    run("sudo usermod -aG lpadmin $USER")
    run("sudo systemctl enable cups")
    run("sudo systemctl start cups")
    run("sudo cupsctl --remote-any")
    run("sudo systemctl restart cups")
    print("[+] CUPS server is ready. Visit http://localhost:631")

if __name__ == "__main__":
    setup_cups()
