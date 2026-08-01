import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

# Before any tests run, create one reusable HTTP session with a JSON header set up.
# Hand that session to every test that needs it.
# Once every test in the whole run is finished, close the session cleanly


@pytest.fixture(scope="session")  # Set to function incase a new session needed every test
def api_session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()