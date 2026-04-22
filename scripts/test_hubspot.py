import os
import time
from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate

load_dotenv()

token = os.getenv("HUBSPOT_ACCESS_TOKEN")
client = HubSpot(access_token=token)

test_email = f"synthetic.day0.{int(time.time())}@example.com"

contact = SimplePublicObjectInputForCreate(
    properties={
        "email": test_email,
        "firstname": "Synthetic",
        "lastname": "Prospect",
        "company": "Day0 Test Co",
    }
)

created = client.crm.contacts.basic_api.create(
    simple_public_object_input_for_create=contact
)

print(f"Created contact ID: {created.id}")
print(f"Email: {test_email}")