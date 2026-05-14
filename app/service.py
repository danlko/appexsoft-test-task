from abc import ABC, abstractmethod

class Service(ABC):
    def __init__(self, api_client, storage):
        self.api_client = api_client
        self.storage = storage

    @abstractmethod
    def _fetch_data(self, item):
        pass

    def process_and_save(self, item):
        try:
            raw_response = self._fetch_data(item)
            item_data = raw_response.get('data', {})
            self.storage.create(item, item_data)

            print(item)
            return True

        except Exception as e:
            print(f"Помилка {item}: {e}")
            return False

class EmailVerifierService(Service):
    def _fetch_data(self, email):
        return self.api_client.email_verify(email)

class DomainSearchService(Service):
    def _fetch_data(self, domain):
        return self.api_client.domain_search(domain)

class ReportService:
    def __init__(self, storage):
        self.storage = storage

    def print_summary(self):
        all_saved_data = self.storage.read_all()

        if not all_saved_data:
            print("no data")
            return
        for identifier, data in all_saved_data.items():
            if self._is_email(identifier):
                self._print_email_data(identifier, data)
            else:
                self._print_domain_data(identifier, data)

    def _is_email(self, identifier):
        return "@" in identifier

    def _print_email_data(self, email, data):
        status = data.get("status", "unknown")
        score = data.get("score", 0)

        print(f"\nEmail: {email} \nStatus: {status} \nScore: {score}")

    def _print_domain_data(self, domain, data):
        organization = data.get("organization", "unknown")

        print(f"\nDomain: {domain} \nOrganization: {organization}")


