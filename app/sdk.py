import requests

class HunterClient:
    BASE_URL = "https://api.hunter.io/v2"

    def __init__(self, api_key):
        self._api_key = api_key

    def _get(self, endpoint, params):
        url = f"{self.BASE_URL}/{endpoint}"

        params["api_key"] = self._api_key

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def email_verify(self, email):
        return self._get("email-verifier", {"email": email})

    def domain_search(self, domain):
        return self._get("domain-search", {"domain": domain})
