"""
Tests for /posts endpoint
"""

import pytest


# Testing the posts endpoint is reachable and returns a dict.
@pytest.mark.smoke
def test_get_all_posts(base_url, api_session):
    response = api_session.get(f"{base_url}/posts")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, dict)
    assert len(body) > 0


# Retrieve user posts should return 200 and dict containing list holding posts data
@pytest.mark.positive
def test_get_posts_by_user_id(base_url, api_session):
    response = api_session.get(f"{base_url}/posts/user/1")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body["posts"], list)


# Retrieve post comments should return 200 and dict containing comments
@pytest.mark.positive
def test_get_comments_by_post_id(base_url, api_session):
    response = api_session.get(f"{base_url}/posts/1/comments")
    assert response.status_code == 200
    body = response.json()
    # Validate that comments are for postID 1 and comment is not empty
    assert body["comments"][0]["postId"] == 1
    assert body["comments"][0]["body"] != ""


# Retrieve non-existing post should return 404
@pytest.mark.negative
@pytest.mark.parametrize("post_id", [0, -1, 252])  # BVA
def test_get_post_by_invalid_id(base_url, api_session, post_id):
    response = api_session.get(f"{base_url}/users/{post_id}")
    assert response.status_code == 404


# Post should be created with given payload and code 201 is returned with post id
@pytest.mark.positive
def test_create_post_valid_payload(api_session, base_url):
    payload = {
        "title": "QA Automation Practice",
        "body": "Testing the create-post endpoint.",
        "userId": 1
    }
    response = api_session.post(f"{base_url}/posts/add", json=payload)
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == payload["title"]
    assert "id" in body


# Creating post should fail as there is an error in payload and should return status code 400
@pytest.mark.negative
@pytest.mark.parametrize(
    "payload, description",
    [
        ({}, "completely empty payload"),
        ({"title": "", "userId": 2}, "empty title field"),
        ({"title": "Test", "userId": "not_a_number"}, "wrong data type for userId"),
    ],
)
def test_create_post_invalid_payloads(api_session, base_url, payload, description):
    response = api_session.post(f"{base_url}/posts/add", json=payload)
    assert response.status_code == 400, f"Unexpected status for: {description}"


# Update an existing post and return status code 200 and the new values.
@pytest.mark.positive
def test_update_patch(api_session, base_url):
    payload = {"title": "Updated Title", "body": "Updated body."}
    response = api_session.patch(f"{base_url}/posts/1", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Updated Title"
    assert body["body"] == "Updated body."


# Deleting user should return 204 and empty body
@pytest.mark.positive
def test_delete_post(api_session, base_url):
    response = api_session.delete(f"{base_url}/posts/1")
    assert response.status_code == 204