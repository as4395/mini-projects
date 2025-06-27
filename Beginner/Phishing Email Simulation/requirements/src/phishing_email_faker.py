from faker import Faker
import random

fake = Faker()

SUBJECTS = [
    "Urgent: Account Suspension Notice",
    "Action Required: Update Your Billing Info",
    "Security Alert: Unauthorized Access Detected",
    "Your Subscription is Expiring Soon",
    "Verify Your Account Information",
]

BODY_TEMPLATES = [
    "Dear {name},\n\nWe detected suspicious activity on your account from {location}. Please verify your information here: {url}",
    "Hello {name},\n\nYour payment method was declined. Update your billing information immediately: {url}",
    "Hi {name},\n\nWe have locked your account due to multiple failed login attempts from {ip_address}. Unlock it now: {url}",
    "Dear {name},\n\nYour subscription expires on {date}. Renew now to avoid interruption: {url}",
    "Hello {name},\n\nPlease confirm your email address to keep your account active: {url}",
]

def generate_phishing_email():
    subject = random.choice(SUBJECTS)
    name = fake.name()
    location = fake.city()
    url = fake.url()
    ip_address = fake.ipv4()
    date = fake.date_this_year().strftime("%B %d, %Y")

    body_template = random.choice(BODY_TEMPLATES)
    body = body_template.format(name=name, location=location, url=url, ip_address=ip_address, date=date)
    email = f"Subject: {subject}\n\n{body}\n\n--\nCustomer Support"
    return email

if __name__ == "__main__":
    print(generate_phishing_email())
