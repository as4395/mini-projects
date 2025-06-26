import argparse
import paramiko
import os

def upload_file(host, port, username, password, filepath):
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    filename = os.path.basename(filepath)
    remote_path = f"./{filename}"

    try:
        sftp.put(filepath, remote_path)
        print(f"[+] Uploaded '{filename}' successfully.")
    except Exception as e:
        print(f"[!] Upload failed: {e}")
    finally:
        sftp.close()
        transport.close()

def main():
    parser = argparse.ArgumentParser(description="SFTP Client Uploader")
    parser.add_argument("-f", "--file", required=True, help="Path to the file to upload")
    parser.add_argument("--host", default="127.0.0.1", help="SFTP server address")
    parser.add_argument("--port", type=int, default=2222, help="SFTP server port")
    parser.add_argument("--user", default="testuser", help="Username")
    parser.add_argument("--password", default="password123", help="Password")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print("[!] File does not exist.")
        return

    upload_file(args.host, args.port, args.user, args.password, args.file)

if __name__ == "__main__":
    main()
