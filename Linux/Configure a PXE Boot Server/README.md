# PXE Boot Server Setup

## Overview
Set up a PXE Boot Server on a Linux machine to enable network booting of client systems. Useful for automated OS deployments or maintenance tasks without physical media.

## Features
- DHCP and TFTP server via dnsmasq  
- Serves PXE boot files (pxelinux.0, config files)  
- Supports NFS/HTTP for installation images  
- Basic security controls to restrict access  

## Prerequisites
- Linux server with sudo/root  
- Network access and static IP recommended  
- Basic networking knowledge  

## Installation and Usage

**1.** Update and upgrade system:
   ```bash
   sudo apt update && sudo apt upgrade -y
  ```
**2.** Install required packages:
```bash
sudo apt install -y dnsmasq tftpd-hpa nfs-kernel-server syslinux pxelinux
```
**3.** Configure dnsmasq by editing `/etc/dnsmasq.conf` with:
```bash
interface=eth0
dhcp-range=192.168.1.100,192.168.1.200,12h
dhcp-boot=pxelinux.0
enable-tftp
tftp-root=/srv/tftp
```
**4.** Prepare TFTP root and boot files:
```bash
sudo mkdir -p /srv/tftp/pxelinux.cfg
sudo cp /usr/lib/PXELINUX/pxelinux.0 /srv/tftp/
sudo cp /usr/lib/syslinux/modules/bios/* /srv/tftp/
```
**5.** Restart and enable services:
```bash
sudo systemctl restart dnsmasq tftpd-hpa nfs-kernel-server
sudo systemctl enable dnsmasq tftpd-hpa nfs-kernel-server
```
**6.** Boot your client machines via network.


## Notes

- Adjust `interface`, IP ranges, and TFTP root as needed.
- Customize PXE menus by adding config files under `/srv/tftp/pxelinux.cfg/`.

## Automation Script

You can use the helper script to automate some setup steps:

```bash
python3 src/pxe_setup_helper.py
```
