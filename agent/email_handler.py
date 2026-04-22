import os
import resend
from dotenv import load_dotenv

load_dotenv()

resend.api_key = os.environ["RESEND_API_KEY"]
FROM_EMAIL = os.getenv("FROM_EMAIL", "onboarding@resend.dev")


def send_email(to_email: str, subject: str, html: str):
    response = resend.Emails.send({
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": subject,
        "html": html,
    })
    return response