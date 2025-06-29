#!/usr/bin/env python3

import os
import argparse
import stat

def is_world_writable(mode):
    return bool(mode & stat.S_IWOTH)

def audit_permissions(target_dir, fix=False, dry_run=False):
    print(f"[+] Scanning directory: {target_dir}")
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            path = os.path.join(root, name)
            try:
                st = os.stat(path)
                if is_world_writable(st.st_mode):
                    print(f"[!] World-writable: {path}")
                    if fix and not dry_run:
                        new_mode = st.st_mode & ~stat.S_IWOTH
                        os.chmod(path, new_mode)
                        print(f"[-] Fixed: {path}")
            except Exception as e:
                print(f"[x] Error checking {path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required=True, help="Target directory to scan")
    parser.add_argument('--fix', action='store_true', help="Fix insecure permissions")
    parser.add_argument('--dry', action='store_true', help="Dry run (no changes)")

    args = parser.parse_args()
    audit_permissions(args.path, fix=args.fix, dry_run=args.dry)
