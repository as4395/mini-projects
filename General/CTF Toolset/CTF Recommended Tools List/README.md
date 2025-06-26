# CTF Tools & Environment

This repository documents a categorized and linked list of tools commonly used in Capture The Flag (CTF) challenges. 

---

## Nix Shell Environment Setup

This `nix` environment defines common tools for quick setup in a reproducible dev shell:

```nix
devShells.default = pkgs.mkShell {
  buildInputs = with pkgs; [
    exiftool
    ffmpeg
    mediainfo
    python3
    python3Packages.scipy
    python3Packages.numpy
    python3Packages.pip
    audacity
    multimon-ng
    sox
    tshark
    pwntools
    ropgadget
    tor
    radare2
  ];
};
```

To use:
```bash
nix develop
```

---

## Web Exploitation

| Tool           | Description                                    | Link |
|----------------|------------------------------------------------|------|
| Burp Suite     | Intercepting proxy & web vulnerability scanner | [Download](https://portswigger.net/burp/releases/professional-community-2025-5-4?requestededition=community&requestedplatform=) |
| CyberChef      | Online encoding/decoding & transformation tool | [Use Online](https://gchq.github.io/CyberChef/) |
| OWASP Juice Shop | Vulnerable web app for practice              | [Get Started](https://owasp.org/www-project-juice-shop/) |
| robots.txt     | File that may expose hidden web paths          | (Manually inspected) |
| Web Browser    | Used for exploring web challenges              | (Any browser) |

---

## Cryptography & Cracking

| Tool                    | Description                            | Link |
|-------------------------|----------------------------------------|------|
| John the Ripper         | Password hash cracker                  | [Download](https://www.openwall.com/john/) |
| OpenSSL                 | Toolkit for encryption, certs, hashing | [Source](https://openssl-library.org/source/) |
| Berlekamp-Massey Python | Python script for solving LFSRs        | [GitHub](https://github.com/thewhiteninja/lfsr-berlekamp-massey) |
| CyberChef               | Versatile encoding, decoding, hashing  | [Use Online](https://gchq.github.io/CyberChef/) |
| Pwntools                | Python CTF exploit development library | [Docs](https://docs.pwntools.com/en/stable/) |

---

## Binary Exploitation & Reverse Engineering

| Tool      | Description                      | Link |
|-----------|----------------------------------|------|
| radare2   | Reverse engineering framework    | [Download](https://rada.re/n/) |
| ROPgadget | ROP chain gadget finder          | [GitHub](https://github.com/JonathanSalwan/ROPgadget) |
| Pwntools  | Exploitation scripting           | [Docs](https://docs.pwntools.com/en/stable/) |
| Terminal  | Used for GDB, objdump, r2, etc.  | (Preinstalled) |

---

## Forensics & File Analysis

| Tool        | Description                                 | Link |
|-------------|---------------------------------------------|------|
| ExifTool    | File metadata extraction                    | [Install](https://exiftool.org/install.html) |
| FFmpeg      | Multimedia conversion                       | [Download](https://ffmpeg.org/download.html) |
| MediaInfo   | Stream metadata viewer                      | [Download](https://mediaarea.net/en/MediaInfo) |
| Audacity    | Audio waveform analysis                     | [Download](https://www.audacityteam.org/download/) |
| Volatility 3| Memory dump analysis                        | [GitHub](https://github.com/volatilityfoundation/volatility3) |
| 7-Zip       | Archive extraction                          | [Download](https://www.7-zip.org/download.html) |
| multimon-ng | Radio signal decoding (APRS, AX.25, etc)    | [GitHub](https://github.com/EliasOenal/multimon-ng) |
| Sox         | Audio manipulation CLI                      | [SourceForge](http://sox.sourceforge.net/) |

---

## Networking

| Tool       | Description                          | Link |
|------------|--------------------------------------|------|
| Nmap       | Port scanning & network mapping      | [Download](https://nmap.org/download) |
| Netcat / nc| TCP/UDP socket tool                  | [Download](https://netcat.sourceforge.net/download.php) |
| Wireshark  | Network protocol analyzer            | [Download](https://www.wireshark.org/download.html) |
| TShark     | CLI version of Wireshark             | [Man Page](https://www.wireshark.org/docs/man-pages/tshark.html) |
| OpenSSL    | Crypto + TLS toolkit                 | [Source](https://openssl-library.org/source/) |
| SSH        | Secure remote shell                  | [OpenSSH](https://www.openssh.com/) |
| Tor        | Onion routing and deep web access    | [Download](https://www.torproject.org/download/) |

---

## OSINT

| Tool         | Description                        | Link |
|--------------|------------------------------------|------|
| Google       | General purpose search             | [Google](https://www.google.com/) |
| Google Maps  | Geolocation lookup                 | [Maps](https://www.google.com/maps) |
| Google Lens  | Reverse image search               | [Lens](https://lens.google) |
| Tor Browser  | Browse .onion and stay anonymous   | [Download](https://www.torproject.org/download/) |

---

## CTF Platforms

| Tool         | Description                        | Link |
|--------------|------------------------------------|------|
| TryHackMe    | Training platform with guided labs | [TryHackMe](https://tryhackme.com) |
| HackTheBox   | Hacking labs and challenges        | [HackTheBox](https://www.hackthebox.com/) |

---

## Workflow & Best Practices

- Start with easy challenges to build momentum.
- Take notes on every challenge — especially ones you don’t solve.
- Collaborate by sharing partial progress so teammates can build on it.
- Write detailed writeups after the CTF to post on:
  - Personal blogs
  - GitHub repositories
  - Team documentation
- Use this repo or [SecurityMarks](https://github.com/Moorpark-College-Cyber-Sec/SecurityMarks) for tracking progress collaboratively.

---

## Local Tools Checklist

Make sure these are installed on your local system (or covered via Nix/VM):

- nmap
- netcat / nc
- openssl
- tor
- python3, pip
- terminal

---

## Online-Only Tools

These tools are browser-based and don’t require installation:

- [CyberChef](https://gchq.github.io/CyberChef/)
- [Google](https://www.google.com/)
- [Google Maps](https://www.google.com/maps)
- [Google Lens](https://lens.google)
- [TryHackMe](https://tryhackme.com)
- [HackTheBox](https://www.hackthebox.com/)

---

## References

- [CTF101: What is a CTF?](https://ctf101.org/intro/what-is-a-ctf/)
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [HackTricks](https://book.hacktricks.xyz/)
- [SecurityMarks](https://github.com/Moorpark-College-Cyber-Sec/SecurityMarks)
