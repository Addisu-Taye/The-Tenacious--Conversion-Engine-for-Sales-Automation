from fastapi import FastAPI, Request, Form
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/webhooks/email/reply")
async def email_reply(request: Request):
    payload = await request.json()
    print("\n=== EMAIL WEBHOOK RECEIVED ===")
    print(payload)
    print("================================\n")
    return {"status": "received"}

@app.post("/webhooks/sms")
async def sms_webhook(
    from_: str = Form(alias="from"),
    text: str = Form(alias="text"),
    to: str = Form(alias="to"),
):
    print("\n=== SMS WEBHOOK RECEIVED ===")
    print({"from": from_, "to": to, "text": text})
    print("================================\n")
    return {"status": "received"}