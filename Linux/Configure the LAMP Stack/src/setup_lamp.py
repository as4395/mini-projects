#!/usr/bin/env python3

import subprocess
import os
import getpass
from colorama import Fore, Style, init

init(autoreset=True)

def run_command(command, sudo=False):
    try:
        if sudo:
            command = ['sudo'] + command
        print(f"{Fore.CYAN}Running: {' '.join(command)}")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Failed to run: {' '.join(command)}")
        exit(1)

def install_apache():
    print(f"{Fore.GREEN}[+] Installing Apache2...")
    run_command(['apt-get', 'update'], sudo=True)
    run_command(['apt-get', 'install', '-y', 'apache2'], sudo=True)

def install_mysql():
    print(f"{Fore.GREEN}[+] Installing MySQL Server...")
    run_command(['apt-get', 'install', '-y', 'mysql-server'], sudo=True)

def secure_mysql():
    print(f"{Fore.GREEN}[+] Securing MySQL...")
    root_pass = getpass.getpass("Enter MySQL root password to secure it: ")
    commands = [
        f"ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '{root_pass}';",
        "DELETE FROM mysql.user WHERE User='';",
        "DROP DATABASE IF EXISTS test;",
        "DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';",
        "FLUSH PRIVILEGES;"
    ]
    for cmd in commands:
        run_command(['mysql', '-u', 'root', '-e', cmd], sudo=True)

def install_php():
    print(f"{Fore.GREEN}[+] Installing PHP and modules...")
    run_command(['apt-get', 'install', '-y', 'php', 'libapache2-mod-php', 'php-mysql'], sudo=True)

def create_test_page():
    print(f"{Fore.GREEN}[+] Creating test PHP page...")
    test_php = "<?php phpinfo(); ?>"
    with open('/tmp/index.php', 'w') as f:
        f.write(test_php)
    run_command(['mv', '/tmp/index.php', '/var/www/html/'], sudo=True)
    run_command(['chown', 'www-data:www-data', '/var/www/html/index.php'], sudo=True)

def main():
    print(f"{Style.BRIGHT}--- LAMP Stack Setup Script ---")
    install_apache()
    install_mysql()
    secure_mysql()
    install_php()
    create_test_page()
    print(f"{Fore.GREEN}\n[+] LAMP Stack configured successfully!")
    print(f"{Fore.YELLOW}Visit http://localhost to verify.")

if __name__ == "__main__":
    main()
