# api/user_api.py
import requests


class UserAPI:

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.endpoint = f"{base_url}/users"
        self.headers = headers

    def get_users(self, page=1):
        return requests.get(self.endpoint, params={"page": page}, headers=self.headers)

    def get_single_user(self, user_id):
        return requests.get(f"{self.endpoint}/{user_id}", headers=self.headers)

    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return requests.post(self.endpoint, json=payload, headers=self.headers)

    def update_user(self, user_id, name, job):
        payload = {"name": name, "job": job}
        return requests.put(f"{self.endpoint}/{user_id}", json=payload, headers=self.headers)

    def patch_user(self, user_id, data):
        return requests.patch(f"{self.endpoint}/{user_id}", json=data, headers=self.headers)

    def delete_user(self, user_id):
        return requests.delete(f"{self.endpoint}/{user_id}", headers=self.headers)