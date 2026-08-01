# DummyJSON API Test Automation

A Python-based API test automation framework for the **DummyJSON REST API** built with **pytest** and **requests**.

The project demonstrates API testing best practices including positive and negative test scenarios, smoke testing, boundary value analysis (BVA), and response validation.

---

## Technologies Used

* Python 3.x (tested on 3.11)
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

## Additional / Missing Features Added

These items were added to this README to improve usability, test quality, and project maturity:

- JSON Schema validation recommendation
  - Consider adding the `jsonschema` package and writing schema files (JSON) for strict payload validation in tests.

- Example GitHub Actions CI workflow (minimal)
  - Add the following file to `.github/workflows/pytest.yml` to run the test suite on pushes and pull requests:

```yaml
name: pytest

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest --maxfail=1 --disable-warnings -q
      - name: Upload pytest HTML report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: report.html
```

- Code coverage (future)
  - Add `pytest-cov` to `requirements.txt` and enable coverage reporting in CI.

- Logging
  - Integrate basic logging in tests or fixtures for easier debugging (use Python's `logging` module).

- Data-driven testing
  - Keep example payloads in `tests/data/` (JSON files) and load them in parameterized tests.

- Example request snippets
  - Add a short `examples/` folder or a `USAGE.md` with sample curl/HTTP requests used by tests.

- Contribution and issue reporting guidance
  - See the CONTRIBUTING.md suggestion below.

---

## Future Improvements (non-exhaustive)

* JSON Schema validation using `jsonschema` for strict contract tests
* HTML test reports with `pytest-html` (already configured in `pytest.ini` addopts)
* Logging for easier troubleshooting
* CI/CD integration using GitHub Actions (example above)
* Code coverage reporting using `pytest-cov`
* Authentication and authorization testing
* Performance and load testing
* Data-driven testing using external JSON/CSV files

---

## Contributing

Contributions are welcome. Suggested process:

1. Fork the repository and create a feature branch (feature/my-feature).
2. Add tests and code changes with clear commit messages.
3. Update or add documentation if needed.
4. Open a pull request describing your changes.

When reporting issues, please include:

* Steps to reproduce
* Expected vs actual behavior
* Relevant logs or test output

---

## License

This project is provided under the MIT License. See `LICENSE` for details. (If no LICENSE file exists, add one with MIT content.)

---

## Author / Contact

**Khaled Ali** (@Khaled3ly00)

Project: Python API Test Automation using `pytest` and `requests`.

---

## Notes

- This README replaces the prior README.md and includes additional guidance for CI, schema validation, contribution, and future improvements. If you want further changes (for example, a full JSON Schema file, example payloads, or a CONTRIBUTING.md / LICENSE file added automatically), tell me which ones and I can add them in follow-up commits.
