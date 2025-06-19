import socket
import threading
import datetime

LOG_FILE = "metrics.log"
HOST = "0.0.0.0"  # Listen on all available interfaces
PORT = 9999       # Port to listen on

def log_message(message):
    """
    Prints the message with a timestamp and writes it to the log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open(LOG_FILE, "a") as f:
        f.write(full_message + "\n")

def handle_client(conn, addr):
    """
    Handles communication with a connected client.
    Receives data and logs it until the client disconnects.
    """
    log_message(f"New connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break  # Client disconnected
            decoded = data.decode("utf-8").strip()
            log_message(f"{addr} - {decoded}")
    except Exception as e:
        log_message(f"Error with {addr}: {e}")
    finally:
        log_message(f"Connection closed for {addr}")
        conn.close()

def start_server():
    """
    Starts the TCP socket server and accepts client connections.
    Each connection is handled in a separate thread.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        log_message(f"Monitoring server started on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

if __name__ == "__main__":
    start_server()
