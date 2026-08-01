"""
Tests for /users endpoint
"""

import pytest

USER_SCHEMA_KEYS = {'id', 'firstName', 'lastName', 'maidenName', 'age', 'gender', 'email', 'phone', 'username',
                    'password', 'birthDate', 'image', 'bloodGroup', 'height', 'weight', 'eyeColor', 'hair', 'ip',
                    'address', 'macAddress', 'university', 'bank', 'company', 'ein', 'ssn', 'userAgent', 'crypto',
                    'role'}


# Testing the users list endpoint is reachable and returns a dict.
@pytest.mark.smoke
def test_get_all_users(base_url, api_session):
    response = api_session.get(f"{base_url}/users")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, dict)
    assert len(body) > 0


# Valid user IDs should return 200 and the correct user object.
@pytest.mark.positive
@pytest.mark.parametrize("user_id", [1, 15, 30])  # BVA
def test_get_user_by_valid_id(base_url, api_session, user_id):
    response = api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == user_id


# Out-of-range / non-existent user IDs should return 404.
@pytest.mark.negative
@pytest.mark.parametrize("user_id, description",
                         [(0, "IDs starts from 1"), (-1, "Negative IDs are invalid"),
                          (209, "ID above valid range")])  # BVA
def test_get_user_by_invalid_id(base_url, api_session, user_id, description):
    response = api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404, f"{description}"


# Wrong format IDs should return 400.
@pytest.mark.negative
def test_get_user_by_non_integer_id(base_url, api_session):
    response = api_session.get(f"{base_url}/users/abc")
    assert response.status_code == 400


# Response body should contain all expected fields with correct types.
@pytest.mark.positive
def test_get_user_schema(base_url, api_session):
    response = api_session.get(f"{base_url}/users/1")
    body = response.json()
    # Every expected key is present
    assert USER_SCHEMA_KEYS.issubset(body.keys())
    # Check for some fields types
    assert isinstance(body["id"], int)
    assert isinstance(body["firstName"], str)
    assert isinstance(body["email"], str)
    assert "@" in body["email"]


# Creating user should return 201 and the created user object.
@pytest.mark.positive
def test_create_user(base_url, api_session):
    payload = {
        "firstName": "Muhammad",
        "lastName": "Ali",
        "age": 25
    }
    response = api_session.post(f"{base_url}/users/add", json=payload)
    # Check if user created successfully
    assert response.status_code == 201
    # Check response body
    body = response.json()
    assert body["firstName"] == "Muhammad"
    assert body["lastName"] == "Ali"
    assert body["age"] == 25


# Updating (PUT) user should return 200 and the updated user object should contain only updated fields.
@pytest.mark.positive
def test_put_update_user_by_id(base_url, api_session):
    payload = {
        "lastName": "Ali",
    }
    response = api_session.put(f"{base_url}/users/1", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["lastName"] == "Ali"
    for schema in USER_SCHEMA_KEYS:
        if schema == "lastName": continue
        assert body[schema] is None


# Deleting user should return 204 and empty body
@pytest.mark.positive
def test_delete_user_by_id(base_url, api_session):
    response = api_session.delete(f"{base_url}/users/1")
    assert response.status_code == 204