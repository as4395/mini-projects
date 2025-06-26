#!/usr/bin/env python3
import subprocess
import sys
import os
import argparse

BASE_DIR = "/etc/openvpn"
EASYRSA_DIR = "/etc/openvpn/easy-rsa"
PKI_DIR = os.path.join(EASYRSA_DIR, "pki")
CLIENT_CONFIGS_DIR = "/etc/openvpn/client-configs"

def run(cmd, shell=False):
    # Run a command, exit on failure.
    print(f"[+] Executing: {cmd if isinstance(cmd, str) else ' '.join(cmd)}")
    result = subprocess.run(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"[!] Error:\n{result.stderr}")
        sys.exit(1)
    return result.stdout.strip()

def install_openvpn():
    print("[*] Installing OpenVPN and easy-rsa...")
    run(["apt-get", "update"])
    run(["apt-get", "install", "-y", "openvpn", "easy-rsa"])

def setup_easy_rsa():
    print("[*] Setting up Easy-RSA environment...")
    if not os.path.exists(EASYRSA_DIR):
        run(["make-cadir", EASYRSA_DIR])

    # Initialize PKI
    os.chdir(EASYRSA_DIR)
    run(["./easyrsa", "init-pki"])
    run(["./easyrsa", "--batch", "build-ca", "nopass"])

    # Generate server certificate and key
    run(["./easyrsa", "gen-req", "server", "nopass"])
    run(["./easyrsa", "sign-req", "server", "server"])

    # Generate Diffie-Hellman params
    run(["./easyrsa", "gen-dh"])

    # Generate TLS auth key
    if not os.path.exists(f"{BASE_DIR}/ta.key"):
        run(["openvpn", "--genkey", "--secret", f"{BASE_DIR}/ta.key"])

def generate_server_conf():
    print("[*] Generating server.conf...")
    server_conf = f"""
port 1194
proto udp
dev tun
ca {PKI_DIR}/ca.crt
cert {PKI_DIR}/issued/server.crt
key {PKI_DIR}/private/server.key
dh {PKI_DIR}/dh.pem
tls-auth {BASE_DIR}/ta.key 0
topology subnet
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status {BASE_DIR}/server/status.log
verb 3
    """.strip()

    conf_path = f"{BASE_DIR}/server.conf"
    with open(conf_path, "w") as f:
        f.write(server_conf)
    print(f"[+] Wrote OpenVPN server config to {conf_path}")

def generate_client_cert(client_name):
    print(f"[*] Generating certificate for client '{client_name}'...")
    os.chdir(EASYRSA_DIR)
    run(["./easyrsa", "gen-req", client_name, "nopass"])
    run(["./easyrsa", "sign-req", "client", client_name])

def create_client_ovpn(client_name):
    print(f"[*] Creating .ovpn client configuration for '{client_name}'...")
    ovpn_dir = os.path.join(CLIENT_CONFIGS_DIR, client_name)
    os.makedirs(ovpn_dir, exist_ok=True)

    base_ovpn = f"""
client
dev tun
proto udp
remote YOUR_VPN_SERVER_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
cipher AES-256-CBC
verb 3
<ca>
{open(os.path.join(PKI_DIR, "ca.crt")).read()}
</ca>
<cert>
{open(os.path.join(PKI_DIR, "issued", client_name + ".crt")).read()}
</cert>
<key>
{open(os.path.join(PKI_DIR, "private", client_name + ".key")).read()}
</key>
<tls-auth>
{open(os.path.join(BASE_DIR, "ta.key")).read()}
</tls-auth>
key-direction 1
    """.strip()

    ovpn_path = os.path.join(ovpn_dir, f"{client_name}.ovpn")
    with open(ovpn_path, "w") as f:
        f.write(base_ovpn)

    print(f"[+] Client config created: {ovpn_path}")

def enable_ip_forwarding():
    print("[*] Enabling IP forwarding...")
    run(["sysctl", "-w", "net.ipv4.ip_forward=1"])
    with open("/etc/sysctl.conf", "a") as sysctl:
        sysctl.write("\nnet.ipv4.ip_forward=1\n")

def start_openvpn_service():
    print("[*] Starting OpenVPN service...")
    run(["systemctl", "enable", "openvpn@server"])
    run(["systemctl", "start", "openvpn@server"])

def main():
    parser = argparse.ArgumentParser(description="OpenVPN Setup & Client Manager")
    parser.add_argument("--add-client", type=str, help="Add a new client certificate and config")
    args = parser.parse_args()

    if os.geteuid() != 0:
        print("[!] This script must be run as root.")
        sys.exit(1)

    if args.add_client:
        client_name = args.add_client
        generate_client_cert(client_name)
        create_client_ovpn(client_name)
        return

    # Initial full setup
    install_openvpn()
    setup_easy_rsa()
    generate_server_conf()
    enable_ip_forwarding()
    start_openvpn_service()
    print("[+] OpenVPN server setup completed successfully.")

if __name__ == "__main__":
    main()
