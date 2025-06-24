import argparse
import dns.resolver
import smtplib
import socket

def check_domain_mx(domain):
    # Check if the domain has MX (mail exchange) DNS records.
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return [r.exchange.to_text() for r in answers]
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        return []

def verify_smtp_server(mx_hosts, from_email, to_email):
    # Attempt to verify the email address by connecting to the SMTP server and issue VRFY or RCPT TO commands.
    for mx in mx_hosts:
        try:
            # Establish SMTP connection
            server = smtplib.SMTP(timeout=10)
            server.connect(mx)
            server.helo(server.local_hostname)  # Introduce ourselves
            server.mail(from_email)
            code, message = server.rcpt(to_email)
            server.quit()
            # SMTP 250 or 251 response indicates acceptance
            if code in [250, 251]:
                return True
        except (smtplib.SMTPServerDisconnected, smtplib.SMTPConnectError,
                smtplib.SMTPHeloError, smtplib.SMTPRecipientsRefused,
                smtplib.SMTPDataError, socket.error):
            continue
    return False

def is_valid_email(email):
    # Basic email format check.
    if '@' not in email:
        return False
    local, domain = email.rsplit('@', 1)
    if not local or not domain:
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description="Verify email existence and domain.")
    parser.add_argument("email", help="Email address to verify")
    parser.add_argument("--from-email", default="test@example.com", help="Sender email for SMTP verification")

    args = parser.parse_args()
    email = args.email.strip()

    if not is_valid_email(email):
        print(f"Invalid email format: {email}")
        return

    domain = email.split('@')[1]
    mx_hosts = check_domain_mx(domain)

    if not mx_hosts:
        print(f"No MX records found for domain: {domain}")
        return

    print(f"Found MX records for {domain}: {mx_hosts}")

    if verify_smtp_server(mx_hosts, args.from_email, email):
        print(f"The email address '{email}' appears to be valid.")
    else:
        print(f"The email address '{email}' does not appear to be valid or cannot be verified.")

if __name__ == "__main__":
    main()
