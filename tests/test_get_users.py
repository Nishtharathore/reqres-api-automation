# tests/test_get_users.py
import pytest
from api.user_api import UserAPI
from utils.assertions import (
    assert_status_code,
    assert_response_time,
    assert_has_keys,
    assert_is_list,
    assert_field_equals
)


class TestGetUsers:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers):
        self.user_api = UserAPI(base_url, headers)

    def test_get_users_status_code(self):
        response = self.user_api.get_users(page=1)
        assert_status_code(response, 200)

    def test_get_users_returns_list(self):
        response = self.user_api.get_users(page=1)
        assert_is_list(response, "data")

    def test_get_users_correct_page(self):
        response = self.user_api.get_users(page=2)
        assert_field_equals(response, "page", 2)

    def test_get_users_not_empty(self):
        response = self.user_api.get_users(page=1)
        data = response.json()
        assert len(data["data"]) > 0

    def test_get_single_user_status_code(self):
        response = self.user_api.get_single_user(2)
        assert_status_code(response, 200)

    def test_get_single_user_correct_id(self):
        response = self.user_api.get_single_user(2)
        assert_field_equals(response, "data", response.json()["data"])

    def test_get_single_user_has_required_fields(self):
        response = self.user_api.get_single_user(2)
        data = response.json()["data"]
        for key in ["id", "email", "first_name", "last_name"]:
            assert key in data

    def test_get_nonexistent_user_returns_404(self):
        response = self.user_api.get_single_user(999)
        assert_status_code(response, 404)