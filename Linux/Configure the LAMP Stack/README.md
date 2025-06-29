# Configure the LAMP Stack

## Overview
The LAMP stack (Linux, Apache, MySQL, PHP) is a popular open-source web development platform. This project sets up and configures a basic LAMP stack on a Linux system (Debian/Ubuntu-based), allowing you to host a simple PHP-based website and interact with a MySQL database.

## Features
- Installs and configures Apache2 web server
- Installs and secures MySQL
- Installs PHP with common modules
- Tests LAMP functionality using a sample `index.php` page

## Requirements
- Linux system (Debian/Ubuntu preferred)
- Internet connection for package installation
- Python 3.7+

## Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/as4395/Mini-Projects/Linux/LAMP-Stack/lamp-stack-setup.git
   cd lamp-stack-setup
   ```

2. Run the setup script:
   ```bash
   sudo python3 src/setup_lamp.py
   ```

3. Visit `http://localhost` on your machine to verify Apache and PHP setup.

## Notes
- Default MySQL root password is prompted securely during installation.
- You can place your own website files in `/var/www/html`.

## Author
Abhiram S.
