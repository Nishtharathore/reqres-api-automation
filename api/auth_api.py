# api/auth_api.py
import requests


class AuthAPI:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.endpoint = f"{base_url}/login"
        self.headers = headers

    def login(self, email, password):
        payload = {"email": email, "password": password}
        return requests.post(self.endpoint, json=payload, headers=self.headers)

    def login_missing_password(self, email):
        payload = {"email": email}
        return requests.post(self.endpoint, json=payload, headers=self.headers)