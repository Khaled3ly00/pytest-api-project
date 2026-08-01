# DummyJSON API Test Automation

A Python-based API test automation framework for the **DummyJSON REST API** built with **pytest** and **requests**.

The project demonstrates API testing best practices including positive and negative test scenarios, smoke testing, boundary value analysis (BVA), and response validation.

---

## Technologies Used

* Python 3.11
* pytest
* requests
* pytest-html (for HTML reports)

---

## Project Structure

```text
.
├── tests/
│   ├── test_users.py
│   └── test_posts.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Features

* Automated REST API testing
* CRUD operation testing
* Positive and negative test scenarios
* Smoke tests
* Boundary Value Analysis (BVA)
* Response status code validation
* JSON response body validation
* Basic schema verification
* Parameterized test cases using pytest

---

## Endpoints Covered

### Users

| Method | Endpoint      | Description         |
| ------ | ------------- | ------------------- |
| GET    | `/users`      | Retrieve all users  |
| GET    | `/users/{id}` | Retrieve user by ID |
| POST   | `/users/add`  | Create a new user   |
| PUT    | `/users/{id}` | Update a user       |
| DELETE | `/users/{id}` | Delete a user       |

### Posts

| Method | Endpoint               | Description                  |
| ------ | ---------------------- | ---------------------------- |
| GET    | `/posts`               | Retrieve all posts           |
| GET    | `/posts/user/{id}`     | Retrieve posts by user       |
| GET    | `/posts/{id}/comments` | Retrieve comments for a post |
| POST   | `/posts/add`           | Create a new post            |
| PATCH  | `/posts/{id}`          | Partially update a post      |
| DELETE | `/posts/{id}`          | Delete a post                |

---

## Test Coverage

### Positive Tests

* Retrieve valid users
* Retrieve user posts
* Retrieve post comments
* Create users
* Create posts
* Update users
* Update posts
* Delete users
* Delete posts

### Negative Tests

* Invalid user IDs
* Invalid post IDs
* Non-integer IDs
* Invalid request payloads
* Missing required fields
* Invalid data types

### Smoke Tests

Basic endpoint availability verification for:

* Users endpoint
* Posts endpoint

---

## Validation Performed

* HTTP status codes
* Response body structure
* Required JSON fields
* Data type validation
* Schema key validation
* Response payload correctness

---

## How to run the tests

### Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run all tests

```bash
pytest
```

### Run with verbose output

```bash
pytest -v
```

### Run only smoke tests

```bash
pytest -m smoke
```

### Run only positive tests

```bash
pytest -m positive
```

### Run only negative tests

```bash
pytest -m negative
```

### Run a single test

```bash
pytest tests/test_users.py::test_create_user -q
```

---

## Fixtures & configuration

- conftest.py
  - base_url fixture returns the base API URL (currently `https://dummyjson.com`)
  - api_session fixture creates a `requests.Session`, sets `Content-Type: application/json`, yields it for the session scope, and closes it when tests complete.

- pytest.ini
  - Declares markers:
    - `smoke`: Quick check for critical functions
    - `positive`: Valid input test case
    - `negative`: Invalid input test case
  - `addopts` configured to `--html=report.html --self-contained-html -v`

---


## Future Improvements

* JSON Schema validation using `jsonschema` for strict contract tests
* CI/CD integration using GitHub Actions
* Code coverage reporting using `pytest-cov`
* Authentication and authorization testing
* Performance and load testing
* Data-driven testing using external JSON/CSV files

---


## Author / Contact

**Khaled Ali** (@Khaled3ly00)

Project: Python API Test Automation using `pytest` and `requests`.

---
