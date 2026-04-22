import time
from agent.observability.langfuse_client import langfuse
from agent.email_handler import send_email
from agent.hubspot_client import create_contact, update_contact


def main():
    prospect_email = f"synthetic.flow.{int(time.time())}@example.com"
    firstname = "Synthetic"
    lastname = "Prospect"
    company = "Day0 Flow Co"

    start = time.time()

    with langfuse.start_as_current_observation(
        as_type="span",
        name="email_interaction",
        input={
            "prospect_email": prospect_email,
            "company": company,
            "stage": "initial_outreach",
        },
    ) as obs:
        contact = create_contact(
            email=prospect_email,
            firstname=firstname,
            lastname=lastname,
            company=company,
        )

        email_response = send_email(
            to_email="addtaye@gmail.com",
            subject="Day 0 Flow Test",
            html=f"<p>Hello from the traced flow for {company}.</p>",
        )

        update_contact(
            contact_id=contact.id,
            properties={
                "jobtitle": "Synthetic prospect",
            }
        )

        obs.update(
            output={
                "hubspot_contact_id": contact.id,
                "email_response": str(email_response),
                "status": "success",
            },
            metadata={
                "latency_ms": int((time.time() - start) * 1000),
                "channel": "email",
                "company": company,
                "component": "day0_email_flow",
            },
        )

    print("Email flow test completed")
    print("HubSpot contact ID:", contact.id)
    print("Prospect email:", prospect_email)


if __name__ == "__main__":
    main()