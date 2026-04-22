import os
from dotenv import load_dotenv
from hubspot import HubSpot
from hubspot.crm.contacts import (
    SimplePublicObjectInputForCreate,
    SimplePublicObjectInput,
)

load_dotenv()

client = HubSpot(access_token=os.environ["HUBSPOT_ACCESS_TOKEN"])


def create_contact(email: str, firstname: str, lastname: str, company: str):
    contact = SimplePublicObjectInputForCreate(
        properties={
            "email": email,
            "firstname": firstname,
            "lastname": lastname,
            "company": company,
        }
    )
    return client.crm.contacts.basic_api.create(
        simple_public_object_input_for_create=contact
    )


def update_contact(contact_id: str, properties: dict):
    update = SimplePublicObjectInput(properties=properties)
    return client.crm.contacts.basic_api.update(
        contact_id=contact_id,
        simple_public_object_input=update,
    )