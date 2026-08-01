import pytest
import requests


def test_get_all_users(base_url, api_session):
    response = api_session.get(f"{base_url}/users")
    assert response.status_code == 200

