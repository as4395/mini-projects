import os

LOG_DIR = "logs"

def list_logs():
    if not os.path.exists(LOG_DIR):
        print("No logs found.")
        return
    for file in os.listdir(LOG_DIR):
        print(f"\n--- {file} ---")
        with open(os.path.join(LOG_DIR, file)) as f:
            lines = f.readlines()
            print("".join(lines[-5:]))

if __name__ == "__main__":
    list_logs()
