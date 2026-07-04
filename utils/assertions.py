

def assert_status_code(response, expected_code):
    """Assert response status code matches expected."""
    assert response.status_code == expected_code, (
        f"Expected status {expected_code}, got {response.status_code}. "
        f"Response body: {response.text}"
    )


def assert_response_time(response, max_seconds=3):
    """Assert response time is within acceptable threshold."""
    actual = response.elapsed.total_seconds()
    assert actual < max_seconds, (
        f"Response too slow: {actual:.2f}s (max allowed: {max_seconds}s)"
    )


def assert_has_keys(response, keys):
    """Assert response body contains all expected keys."""
    data = response.json()
    for key in keys:
        assert key in data, (
            f"Expected key '{key}' not found in response. "
            f"Available keys: {list(data.keys())}"
        )


def assert_field_equals(response, field, expected_value):
    """Assert a specific field in response body equals expected value."""
    data = response.json()
    actual = data.get(field)
    assert actual == expected_value, (
        f"Expected '{field}' to be '{expected_value}', got '{actual}'"
    )


def assert_field_is_not_none(response, field):
    """Assert a specific field exists and is not None."""
    data = response.json()
    assert field in data and data[field] is not None, (
        f"Expected '{field}' to exist and be non-null in response"
    )


def assert_is_list(response, key):
    """Assert a specific key in response body is a list."""
    data = response.json()
    assert isinstance(data[key], list), (
        f"Expected '{key}' to be a list, got {type(data[key]).__name__}"
    )