# Web Security Attacks Project

## Overview
This project explores common web application attacks such as Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), and Local File Inclusion (LFI). You will build small demo vulnerable web apps and scripts to test these attacks in a controlled environment to better understand how attackers exploit web vulnerabilities.

## Objectives
- Set up vulnerable web applications for testing
- Demonstrate and exploit XSS, CSRF, and LFI attacks
- Write Python scripts to automate testing of these vulnerabilities
- Understand mitigation techniques for each vulnerability

## Prerequisites
- Basic knowledge of web technologies (HTTP, HTML, JavaScript)
- Python 3 installed
- Flask web framework basics
- Familiarity with command line and virtual environments

## Usage

**1.** Clone the repo:
```bash
git clone https://github.com/as4395/Mini-Projects/WebSecurity/web-security-attacks.git
cd web-security-attacks
```
**2.** Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
**3.** Install dependencies:
```bash
pip install -r requirements.txt
```
**4.** Run the vulnerable app:
```bash
python src/app.py
```
The app will run on [http://127.0.0.1:5000](http://127.0.0.1:5000)

**5.** Use the attack scripts to test vulnerabilities:
```bash
python src/xss_attack.py
python src/csrf_attack.py
python src/lfi_attack.py
```
