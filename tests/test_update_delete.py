import pytest
from api.user_api import UserAPI
from utils.assertions import (
    assert_status_code,
    assert_response_time,
    assert_field_equals,
    assert_has_keys
)


class TestUpdateUser:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers, faker):
        self.user_api = UserAPI(base_url, headers)
        self.user_id = 2
        self.name = faker.name()
        self.job = faker.job()

    def test_put_user_status_code(self):
        response = self.user_api.update_user(self.user_id, self.name, self.job)
        assert_status_code(response, 200)

    def test_put_user_returns_updated_name(self):
        response = self.user_api.update_user(self.user_id, self.name, self.job)
        assert_field_equals(response, "name", self.name)

    def test_put_user_returns_updated_job(self):
        response = self.user_api.update_user(self.user_id, self.name, self.job)
        assert_field_equals(response, "job", self.job)

    def test_put_user_returns_updated_at(self):
        response = self.user_api.update_user(self.user_id, self.name, self.job)
        assert_has_keys(response, ["updatedAt"])

    def test_put_user_response_time(self):
        response = self.user_api.update_user(self.user_id, self.name, self.job)
        assert_response_time(response, 3)


class TestPatchUser:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers, faker):
        self.user_api = UserAPI(base_url, headers)
        self.user_id = 2
        self.new_job = faker.job()

    def test_patch_user_status_code(self):
        response = self.user_api.patch_user(self.user_id, {"job": self.new_job})
        assert_status_code(response, 200)

    def test_patch_user_returns_updated_job(self):
        response = self.user_api.patch_user(self.user_id, {"job": self.new_job})
        assert_field_equals(response, "job", self.new_job)

    def test_patch_user_returns_updated_at(self):
        response = self.user_api.patch_user(self.user_id, {"job": self.new_job})
        assert_has_keys(response, ["updatedAt"])

    def test_patch_user_response_time(self):
        response = self.user_api.patch_user(self.user_id, {"job": self.new_job})
        assert_response_time(response, 3)


class TestDeleteUser:

    @pytest.fixture(autouse=True)
    def setup(self, base_url, headers):
        self.user_api = UserAPI(base_url, headers)
        self.user_id = 2

    def test_delete_user_status_code(self):
        response = self.user_api.delete_user(self.user_id)
        assert_status_code(response, 204)

    def test_delete_user_empty_response_body(self):
        response = self.user_api.delete_user(self.user_id)
        assert response.text == ""

    def test_delete_user_response_time(self):
        response = self.user_api.delete_user(self.user_id)
        assert_response_time(response, 3)