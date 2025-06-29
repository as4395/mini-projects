import os
import subprocess

SHARE_NAME = "Share"
SHARE_PATH = f"/srv/samba/{SHARE_NAME}"
USERNAME = "nasuser"
PASSWORD = "raspberry"

def install_samba():
    print("[+] Installing Samba...")
    subprocess.run(["apt", "update"])
    subprocess.run(["apt", "install", "-y", "samba"])

def create_user():
    print("[+] Creating NAS user...")
    subprocess.run(["useradd", "-M", "-s", "/sbin/nologin", USERNAME])
    p = subprocess.Popen(["smbpasswd", "-a", USERNAME], stdin=subprocess.PIPE)
    p.communicate(input=f"{PASSWORD}\n{PASSWORD}\n".encode())

def configure_share():
    print("[+] Setting up shared folder...")
    os.makedirs(SHARE_PATH, exist_ok=True)
    subprocess.run(["chown", "-R", f"{USERNAME}:{USERNAME}", SHARE_PATH])
    with open("/etc/samba/smb.conf", "a") as f:
        f.write(f"""

[{SHARE_NAME}]
   path = {SHARE_PATH}
   browseable = yes
   read only = no
   guest ok = no
   valid users = {USERNAME}
""")

def restart_samba():
    print("[+] Restarting Samba service...")
    subprocess.run(["systemctl", "restart", "smbd"])

if __name__ == "__main__":
    install_samba()
    create_user()
    configure_share()
    restart_samba()
    print(f"[+] NAS setup complete! You can access it at smb://<your-ip>/{SHARE_NAME}")
