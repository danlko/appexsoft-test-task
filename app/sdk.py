import requests

class HunterClient:
    BASE_URL = "https://api.hunter.io/v2"

    def __init__(self, api_key):
        self._api_key = api_key

    def email_verify(self, email):
        url = f"{self.BASE_URL}/email-verifier"
        params = {
            "email": email,
            "api_key": self._api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def domain_search(self, domain):
        url = f"{self.BASE_URL}/domain-search"
        params = {
            "domain": domain,
            "api_key": self._api_key
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()
