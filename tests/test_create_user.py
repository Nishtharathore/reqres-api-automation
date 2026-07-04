# tests/test_create_user.py
import pytest
from api.user_api import UserAPI
from utils.assertions import (
    assert_status_code,
    assert_response_time,
    assert_has_keys,
    assert_field_equals,
    assert_field_is_not_none
)


class TestCreateUser:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers, faker):
        self.user_api = UserAPI(base_url, headers)
        self.name = faker.name()
        self.job = faker.job()

    def test_create_user_status_code(self):
        response = self.user_api.create_user(self.name, self.job)
        assert_status_code(response, 201)

    def test_create_user_returns_name(self):
        response = self.user_api.create_user(self.name, self.job)
        assert_field_equals(response, "name", self.name)

    def test_create_user_returns_job(self):
        response = self.user_api.create_user(self.name, self.job)
        assert_field_equals(response, "job", self.job)

    def test_create_user_returns_id(self):
        response = self.user_api.create_user(self.name, self.job)
        assert_field_is_not_none(response, "id")

    def test_create_user_returns_created_at(self):
        response = self.user_api.create_user(self.name, self.job)
        assert_has_keys(response, ["createdAt"])

    def test_create_user_response_time(self):
        response = self.user_api.create_user(self.name, self.job)
        assert_response_time(response, 3)