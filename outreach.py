import os
from twilio.rest import Client

twilio = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
FROM_NUMBER = os.environ["TWILIO_FROM_NUMBER"]


def send_sms(to: str, body: str) -> bool:
    try:
        msg = twilio.messages.create(body=body, from_=FROM_NUMBER, to=to)
        print(f"  SMS sent: {msg.sid}")
        return True
    except Exception as e:
        print(f"  SMS failed: {e}")
        return False


def send_email(to: str, subject: str, body: str, from_email: str = None) -> bool:
    """Sends via SMTP. Configure SMTP_HOST, SMTP_USER, SMTP_PASS in env."""
    import smtplib
    from email.mime.text import MIMEText
    from_email = from_email or os.environ["SMTP_USER"]
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to
    try:
        with smtplib.SMTP_SSL(os.environ["SMTP_HOST"], 465) as server:
            server.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
            server.sendmail(from_email, to, msg.as_string())
        return True
    except Exception as e:
        print(f"  Email failed: {e}")
        return False
