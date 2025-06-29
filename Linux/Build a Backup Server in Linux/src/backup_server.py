#!/usr/bin/env python3

import argparse
import os
import shutil
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import paramiko

def timestamp():
    return datetime.now().strftime("%Y%m%d-%H%M%S")

class BackupHandler(FileSystemEventHandler):
    def __init__(self, src, dest, remote=None):
        self.src = src
        self.dest = dest
        self.remote = remote

    def on_modified(self, event):
        self.backup()

    def on_created(self, event):
        self.backup()

    def backup(self):
        ts = timestamp()
        dest_path = os.path.join(self.dest, ts)
        shutil.copytree(self.src, dest_path)
        print(f"Backed up to {dest_path}")
        if self.remote:
            self.push_remote(dest_path)

    def push_remote(self, path):
        user, host_path = self.remote.split("@")
        host, remote_path = host_path.split(":",1)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user)
        sftp = ssh.open_sftp()
        for root, dirs, files in os.walk(path):
            for f in files:
                local = os.path.join(root, f)
                rel = os.path.relpath(local, path)
                remote_file = os.path.join(remote_path, os.path.basename(path), rel)
                remote_dir = os.path.dirname(remote_file)
                try:
                    sftp.stat(remote_dir)
                except IOError:
                    sftp.mkdir(remote_dir)
                sftp.put(local, remote_file)
        sftp.close()
        ssh.close()
        print("Remote backup complete")

def main():
    parser = argparse.ArgumentParser(description="Backup Server Tool")
    parser.add_argument("--source", required=True)
    parser.add_argument("--dest", help="Local backup directory")
    parser.add_argument("--dest-server", help="Remote backup target: user@host:/path")
    args = parser.parse_args()

    if not os.path.isdir(args.source):
        print("Source path invalid")
        return

    if args.dest:
        os.makedirs(args.dest, exist_ok=True)
    elif args.dest_server:
        args.dest = "/tmp/backup_local"
        os.makedirs(args.dest, exist_ok=True)
    else:
        print("Specify --dest or --dest-server")
        return

    event_handler = BackupHandler(args.source, args.dest, args.dest_server)
    observer = Observer()
    observer.schedule(event_handler, args.source, recursive=True)
    observer.start()
    print(f"Watching {args.source} for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
