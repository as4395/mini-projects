import socket
import threading

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 9999       # Port to listen on

clients = []

def handle_client(client_socket, address):
    print(f"[+] Connection established from {address}")
    try:
        while True:
            command = input(f"Command to {address}: ")
            if not command.strip():
                continue
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(f"[{address}] Response:\n{response}")
    except (ConnectionResetError, BrokenPipeError):
        print(f"[-] Connection lost from {address}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] Server listening on {HOST}:{PORT}")
    try:
        while True:
            client_socket, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
            client_thread.start()
            clients.append((client_socket, addr))
    except KeyboardInterrupt:
        print("[!] Shutting down server.")
        for client_socket, _ in clients:
            client_socket.close()
        server.close()

if __name__ == "__main__":
    start_server()
