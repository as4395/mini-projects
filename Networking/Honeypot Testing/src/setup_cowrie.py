import os
import subprocess
import sys

COWRIE_DIR = "cowrie"

def run_command(cmd, cwd=None):
    # Executes a shell command and returns output or exits on failure.
    print(f"[+] Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"[!] Command failed: {' '.join(cmd)}")
        print(result.stderr)
        sys.exit(1)
    return result.stdout

def install_dependencies():
    # Install system dependencies required for Cowrie honeypot.
    print("[*] Installing dependencies (Ubuntu)...")
    deps = [
        "git", "python3", "python3-virtualenv", "python3-pip",
        "libssl-dev", "libffi-dev", "build-essential", "authbind"
    ]
    run_command(["sudo", "apt", "update"])
    run_command(["sudo", "apt", "install", "-y"] + deps)

def clone_cowrie():
    # Clones the Cowrie honeypot repository if not already present.
    if os.path.exists(COWRIE_DIR):
        print(f"[!] Directory '{COWRIE_DIR}' already exists. Skipping clone.")
        return
    run_command(["git", "clone", "https://github.com/cowrie/cowrie.git"])

def setup_virtualenv():
    # "Creates and sets up Cowrie's Python virtual environment.
    print("[*] Setting up Python virtual environment...")
    run_command(["python3", "-m", "virtualenv", "cowrie-env"], cwd=COWRIE_DIR)
    pip_path = os.path.join(COWRIE_DIR, "cowrie-env", "bin", "pip")
    run_command([pip_path, "install", "--upgrade", "pip"], cwd=COWRIE_DIR)
    run_command([pip_path, "install", "-r", "requirements.txt"], cwd=COWRIE_DIR)

def enable_authbind():
    # Allows non-root users to bind Cowrie to port 2222 via authbind.
    print("[*] Setting up authbind to allow non-root binding to port 2222...")
    run_command(["sudo", "touch", "/etc/authbind/byport/2222"])
    run_command(["sudo", "chmod", "500", "/etc/authbind/byport/2222"])

def main():
    install_dependencies()
    clone_cowrie()
    setup_virtualenv()
    enable_authbind()
    print("\n[+] Cowrie setup complete!")
    print("Run the honeypot with:\n  cd cowrie\n  bin/cowrie start\n")
    print("Use ctrl+c to stop the honeypot.")

if __name__ == "__main__":
    main()
