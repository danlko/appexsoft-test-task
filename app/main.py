from dotenv import load_dotenv
import os

from storage import MemoryStorage
from sdk import HunterClient
from service import ReportService, EmailVerifierService, DomainSearchService

def main():
    load_dotenv()

    api_key = os.getenv("API_KEY")

    storage = MemoryStorage()
    client = HunterClient(api_key=api_key)
    email_service = EmailVerifierService(api_client=client, storage=storage)
    domain_service = DomainSearchService(api_client=client, storage=storage)

    reporter = ReportService(storage=storage)

    emails_to_test = [
        "patrick@stripe.com",
    ]

    domain_to_test = [
        "stripe.com"
    ]

    for email in emails_to_test:
        email_service.process_and_save(email)

    for domain in domain_to_test:
        domain_service.process_and_save(domain)

    reporter.print_summary()

if __name__ == "__main__":
    main()


