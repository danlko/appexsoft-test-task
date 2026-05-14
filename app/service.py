class EmailVerifierService:
    def __init__(self, api_client, storage):
        self.api_client = api_client
        self.storage = storage

    def process_and_save_email(self, email):
        try:
            raw_response = self.api_client.email_verify(email)

            email_data = raw_response.get('data', {})

            self.storage.create(email, email_data)
            print(email)
            return True

        except Exception as e:
            print(f"Помилка {email}: {e}")
            return False

class DomainSearchService:
    def __init__(self, api_client, storage):
        self.api_client = api_client
        self.storage = storage

    def process_and_save_domain(self, domain):
        try:
            raw_response = self.api_client.domain_search(domain)
            domain_data = raw_response.get('data', {})

            self.storage.create(domain, domain_data)
            print(domain)
            return True

        except Exception as e:
            print(f"Помилка {domain}: {e}")
            return False

