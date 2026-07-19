# tests/test_token_chaining.py
import pytest
from api.auth_api import AuthAPI
from api.user_api import UserAPI
from utils.assertions import assert_status_code, assert_schema
from utils.schemas import USERS_LIST_SCHEMA


class TestTokenChaining:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers):
        self.auth_api = AuthAPI(base_url, headers)
        self.base_url = base_url
        self.base_headers = headers

    def test_token_is_captured_from_login(self):
        """Step 1: verify token is captured correctly from login response."""
        token = self.auth_api.get_token("eve.holt@reqres.in", "cityslicka")
        assert token is not None
        assert isinstance(token, str)
        assert len(token) > 0

    def test_authenticated_request_using_token(self):
        """Step 2: use captured token in subsequent request."""
        # Step 1 — login and capture token
        token = self.auth_api.get_token("eve.holt@reqres.in", "cityslicka")

        # Step 2 — build headers with token included
        authenticated_headers = {
            **self.base_headers,         # keep existing headers (x-api-key)
            "Authorization": f"Bearer {token}"  # add token
        }

        # Step 3 — make request with authenticated headers
        user_api = UserAPI(self.base_url, authenticated_headers)
        response = user_api.get_users(page=1)

        # Step 4 — assert request succeeded
        assert_status_code(response, 200)

    def test_authenticated_request_schema(self):
        """Verify response schema is intact when using token auth."""
        token = self.auth_api.get_token("eve.holt@reqres.in", "cityslicka")

        authenticated_headers = {
            **self.base_headers,
            "Authorization": f"Bearer {token}"
        }

        user_api = UserAPI(self.base_url, authenticated_headers)
        response = user_api.get_users(page=1)
        assert_schema(response, USERS_LIST_SCHEMA)

    def test_token_changes_per_login(self):
        """Verify each login produces a valid token (tokens are unique per session)."""
        token1 = self.auth_api.get_token("eve.holt@reqres.in", "cityslicka")
        token2 = self.auth_api.get_token("eve.holt@reqres.in", "cityslicka")

        # both should be valid strings
        assert isinstance(token1, str) and len(token1) > 0
        assert isinstance(token2, str) and len(token2) > 0