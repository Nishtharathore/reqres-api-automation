# tests/test_auth.py
import pytest
from api.auth_api import AuthAPI
from utils.assertions import (
    assert_status_code,
    assert_response_time,
    assert_has_keys,
    assert_field_is_not_none
)


class TestAuth:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers):
        self.auth_api = AuthAPI(base_url, headers)

    def test_login_status_code(self):
        response = self.auth_api.login("eve.holt@reqres.in", "cityslicka")
        assert_status_code(response, 200)

    def test_login_returns_token(self):
        response = self.auth_api.login("eve.holt@reqres.in", "cityslicka")
        assert_field_is_not_none(response, "token")

    def test_login_token_is_string(self):
        response = self.auth_api.login("eve.holt@reqres.in", "cityslicka")
        assert isinstance(response.json()["token"], str)

    def test_login_missing_password_status_code(self):
        response = self.auth_api.login_missing_password("eve.holt@reqres.in")
        assert_status_code(response, 400)

    def test_login_missing_password_error_message(self):
        response = self.auth_api.login_missing_password("eve.holt@reqres.in")
        assert_has_keys(response, ["error"])

    def test_login_response_time(self):
        response = self.auth_api.login("eve.holt@reqres.in", "cityslicka")
        assert_response_time(response, 3)