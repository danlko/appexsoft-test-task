from dotenv import load_dotenv
import os

from storage import MemoryStorage
from sdk import HunterClient
from service import EmailVerifierService, DomainSearchService

def main():
    load_dotenv()

    api_key = os.getenv("API_KEY")

    storage = MemoryStorage()
    client = HunterClient(api_key=api_key)
    email_service = EmailVerifierService(api_client=client, storage=storage)
    domain_service = DomainSearchService(api_client=client, storage=storage)

    emails_to_test = [
        "patrick@stripe.com",
    ]

    domain_to_test = [
        "stripe.com"
    ]

    for email in emails_to_test:
        email_service.process_and_save_email(email)

    for domain in domain_to_test:
        domain_service.process_and_save_domain(domain)

    all_saved_data = storage.read_all()

    for key, data in all_saved_data.items():
        if "@" in key:
            status = data.get("status", "unknown")
            score = data.get("score", 0)
            print(f"Email: {key} \nstatus: {status} \nscore: {score}")
        else:
            organization = data.get("organization", "unknown")
            print(f"\nDomain: {key} \norganization: {organization}")

if __name__ == "__main__":
    main()


