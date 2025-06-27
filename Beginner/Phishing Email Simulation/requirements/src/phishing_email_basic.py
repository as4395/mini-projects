import random

SUBJECTS = [
    "Urgent: Account Verification Required",
    "Your Package is on Hold",
    "Important Security Alert",
    "Confirm Your Payment Details",
    "You Have a New Voicemail",
]

BODY_TEMPLATES = [
    "Dear user, we noticed unusual activity in your account. Please login immediately to verify your identity.",
    "Your recent package delivery could not be completed. Click here to reschedule.",
    "We've detected suspicious login attempts. Please update your password using the link below.",
    "Your payment could not be processed. Provide your payment information to avoid suspension.",
    "You have a new voicemail waiting. Click to listen.",
]

def generate_phishing_email():
    subject = random.choice(SUBJECTS)
    body = random.choice(BODY_TEMPLATES)
    email = f"Subject: {subject}\n\n{body}\n\n--\nSupport Team"
    return email

if __name__ == "__main__":
    print(generate_phishing_email())
