import os
import socket
import threading
import paramiko
import sys
import logging
from paramiko import SFTPServerInterface, SFTPServer, SFTPAttributes, SFTP_OK, SFTP_PERMISSION_DENIED
from paramiko.py3compat import b, u

# Configuration
HOST_KEY = paramiko.RSAKey.generate(2048)
USERNAME = "testuser"
PASSWORD = "password123"
UPLOAD_DIR = "uploads"
PORT = 2222

# Setup logging
logging.basicConfig(filename="sftp_server.log", level=logging.INFO, format="%(asctime)s - %(message)s")

class StubSFTPHandle(paramiko.SFTPHandle):
    def write(self, data):
        self.file.write(data)
        return len(data)

class SFTPHandler(SFTPServerInterface):
    def __init__(self, server, *largs, **kwargs):
        super().__init__(server)
        self.readonly = False

    def list_folder(self, path):
        attrs = []
        for filename in os.listdir(UPLOAD_DIR):
            filepath = os.path.join(UPLOAD_DIR, filename)
            attr = SFTPAttributes.from_stat(os.stat(filepath))
            attr.filename = filename
            attrs.append(attr)
        return attrs

    def open(self, path, flags, attr):
        filename = os.path.basename(path)
        filepath = os.path.join(UPLOAD_DIR, filename)

        # Ensure uploads directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        try:
            mode = 'wb' if os.O_WRONLY & flags else 'rb'
            f = open(filepath, mode)
            logging.info(f"File upload started: {filename}")
            return StubSFTPHandle(flags=flags, file=f)
        except IOError:
            return paramiko.SFTPServer.convert_errno(errno.EACCES)

    def stat(self, path):
        return SFTPAttributes.from_stat(os.stat(UPLOAD_DIR))

class SFTPServerSession(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_request(self, kind, chanid):
        return paramiko.OPEN_SUCCEEDED if kind == "session" else paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_subsystem_request(self, channel, name):
        return name == 'sftp'

def start_server():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', PORT))
        sock.listen(100)
        print(f"[*] SFTP server running on port {PORT}...")

        while True:
            client, addr = sock.accept()
            transport = paramiko.Transport(client)
            transport.add_server_key(HOST_KEY)
            server = SFTPServerSession()

            try:
                transport.start_server(server=server)
                channel = transport.accept(20)
                if channel is None:
                    continue
                transport.set_subsystem_handler("sftp", SFTPServer, SFTPHandler)
                logging.info(f"Connection established from {addr[0]}")
            except Exception as e:
                logging.error(f"Server error: {str(e)}")

    except KeyboardInterrupt:
        print("\n[!] Server shutting down.")
        sys.exit(0)

if __name__ == "__main__":
    start_server()
