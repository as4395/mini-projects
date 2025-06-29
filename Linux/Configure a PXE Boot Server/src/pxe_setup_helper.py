#!/usr/bin/env python3

import os
import shutil
import subprocess

DNSMASQ_CONF = "/etc/dnsmasq.conf"
BACKUP_CONF = "/etc/dnsmasq.conf.bak"
TFTP_ROOT = "/srv/tftp"
PXELINUX_SRC = "/usr/lib/PXELINUX/pxelinux.0"
SYSLINUX_MODULES_SRC = "/usr/lib/syslinux/modules/bios/"

def backup_dnsmasq_conf():
    if os.path.exists(DNSMASQ_CONF):
        print(f"Backing up {DNSMASQ_CONF} to {BACKUP_CONF}...")
        shutil.copy2(DNSMASQ_CONF, BACKUP_CONF)

def append_dnsmasq_config():
    config_lines = [
        "interface=eth0",
        "dhcp-range=192.168.1.100,192.168.1.200,12h",
        "dhcp-boot=pxelinux.0",
        "enable-tftp",
        f"tftp-root={TFTP_ROOT}"
    ]
    print(f"Appending PXE config to {DNSMASQ_CONF}...")
    with open(DNSMASQ_CONF, "a") as f:
        f.write("\n# PXE Boot Server Configuration\n")
        for line in config_lines:
            f.write(line + "\n")

def setup_tftp_root():
    print(f"Creating TFTP root directory at {TFTP_ROOT}...")
    os.makedirs(TFTP_ROOT, exist_ok=True)

    print(f"Copying PXELINUX bootloader from {PXELINUX_SRC}...")
    shutil.copy2(PXELINUX_SRC, TFTP_ROOT)

    print(f"Copying syslinux BIOS modules from {SYSLINUX_MODULES_SRC}...")
    for filename in os.listdir(SYSLINUX_MODULES_SRC):
        src_file = os.path.join(SYSLINUX_MODULES_SRC, filename)
        dst_file = os.path.join(TFTP_ROOT, filename)
        shutil.copy2(src_file, dst_file)

def restart_services():
    print("Restarting dnsmasq, tftpd-hpa, and nfs-kernel-server services...")
    subprocess.run(["sudo", "systemctl", "restart", "dnsmasq"], check=True)
    subprocess.run(["sudo", "systemctl", "restart", "tftpd-hpa"], check=True)
    subprocess.run(["sudo", "systemctl", "restart", "nfs-kernel-server"], check=True)
    print("Services restarted successfully.")

def main():
    backup_dnsmasq_conf()
    append_dnsmasq_config()
    setup_tftp_root()
    restart_services()
    print("PXE Boot Server setup automation complete.")

if __name__ == "__main__":
    main()
