import os
from dotenv import load_dotenv
import resend

load_dotenv()

api_key = os.getenv("RESEND_API_KEY")
from_email = os.getenv("FROM_EMAIL", "onboarding@resend.dev")

if not api_key:
    raise ValueError("RESEND_API_KEY is missing from .env")

resend.api_key = api_key

response = resend.Emails.send({
    "from": from_email,
    "to": ["addtaye@gmail.com"],
    "subject": "Day 0 Email Test",
    "html": "<p>Resend is working and webhook base URL is ready.</p>",
})

print(response)