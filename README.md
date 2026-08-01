# pytest-api-project

A small pytest-based API test suite for the Users endpoints of the DummyJSON API (https://dummyjson.com). The suite exercises list, read, create, update and delete behaviors and generates an HTML report.

## What this repo is for
Automated API tests that validate the Users-related endpoints of the DummyJSON example API. Useful as a learning/demo project for writing pytest HTTP tests with requests and for producing HTML test reports.

## Stack
- Language: Python 3.11 (tested)
- Test framework: pytest (with pytest-html for reports)
- HTTP client: requests

## Contents
- conftest.py — test fixtures (base_url and a session fixture)
- tests/test_users.py — test cases that exercise the Users endpoints
- pytest.ini — pytest configuration and custom markers
- requirements.txt — Python dependencies
- report.html — generated pytest-html report

## What the tests cover (summary of test cases)
All tests use the base URL configured in conftest.py (BASE_URL = https://dummyjson.com) and a session fixture that sets Content-Type: application/json.

- test_get_all_users (marker: smoke)
  - Verifies GET /users responds with HTTP 200 and returns a non-empty JSON dict.

- test_get_user_by_valid_id (marker: positive, param: [1, 15, 30])
  - Verifies GET /users/{id} returns HTTP 200 for valid IDs and the returned `id` matches the requested one.
  - Uses basic boundary-value sampling (1, 15, 30).

- test_get_user_by_invalid_id (marker: negative, param: [(0, ...), (-1, ...), (209, ...)])
  - Verifies out-of-range or non-existent numeric IDs return HTTP 404.

- test_get_user_by_non_integer_id (marker: negative)
  - Verifies GET /users/abc (non-integer ID) returns HTTP 400.

- test_get_user_schema (marker: positive)
  - Verifies the response JSON for a user contains expected keys:
    id, firstName, lastName, username, email, address, phone, image, company
  - Verifies types for some fields (id int, firstName str, email contains "@").

- test_create_user (marker: positive)
  - Verifies POST /users/add with a JSON payload returns HTTP 201 and that the response body contains the submitted fields (firstName, lastName, age).

- test_put_update_user_by_id (marker: positive, xfail)
  - Attempts to update a user via PUT /users/1 and expects updated fields; marked xfail because the API behavior may differ (suite expects some fields to become None except updated one).

- test_delete_user_by_id (marker: positive, xfail)
  - Attempts to delete a user via DELETE /users/1 and expects HTTP 204; marked xfail as a conservative expectation.

Notes on special cases:
- Some tests are marked xfail (expected failure) because the target API may not strictly follow the assumed behavior for PUT/DELETE in this demo environment.
- Tests are grouped with custom markers in pytest.ini:
  - smoke, positive, negative

## How to run the tests locally
1. Create a virtual environment (recommended)
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows

2. Install dependencies
   pip install -r requirements.txt

3. Run the full test suite and generate HTML report (pytest.ini addopts already configures the HTML report):
   pytest

4. Run only smoke tests:
   pytest -m smoke

5. Run only negative tests:
   pytest -m negative

6. Run a single test by name:
   pytest tests/test_users.py::test_create_user -q

7. Generate a self-contained HTML report (same as default `pytest` here):
   pytest --html=report.html --self-contained-html -v

## Fixtures & configuration
- conftest.py
  - base_url fixture returns the base API URL (currently "https://dummyjson.com")
  - api_session fixture creates a requests.Session, sets `Content-Type: application/json`, yields it for the session scope, and closes it when tests complete.

- pytest.ini
  - Declares markers:
    - smoke: Quick check for critical functions
    - positive: Valid input test case
    - negative: Invalid input test case
  - addopts configured to `--html=report.html --self-contained-html -v`

## Dependencies
See requirements.txt — notable packages:
- pytest
- requests
- pytest-html (implicit via report.html generation in addopts)

## Test report
A report.html file is included in the repository. This is the pytest-html output from a prior run and summarizes results (passed, xfailed, etc.).

## Contact / Author
Repository owner: @Khaled3ly00
