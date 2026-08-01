import pytest


@pytest.mark.smoke
def test_get_all_users(base_url, api_session):
    response = api_session.get(f"{base_url}/users")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, dict)
    assert len(body) > 0


@pytest.mark.positive
@pytest.mark.parametrize("user_id", [1, 15, 30]) # BVA
def test_get_user_by_valid_id(base_url,api_session,user_id):
    response = api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == user_id


@pytest.mark.negative
@pytest.mark.parametrize("user_id, description",
                        [(0, "IDs starts from 1"), (-1, "Negative IDs are invalid"), (209, "ID above valid range")]) # BVA
def test_get_user_by_invalid_id(base_url,api_session,user_id, description):
    response = api_session.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404, f"{description}" # User doesn't exist