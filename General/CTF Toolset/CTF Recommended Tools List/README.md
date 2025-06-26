# CTF Tools & Environment

This repository documents a categorized and linked list of tools commonly used in [Capture The Flag (CTF)](https://ctf101.org/intro/what-is-a-ctf/) challenges. 

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
