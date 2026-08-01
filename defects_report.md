# Defect Report — API Test Automation Suite

**Project:** API Test Automation Suite (Pytest)
**API Under Test:** DummyJSON ("https://dummyjson.com")
**Endpoints Covered:** /users, /posts

---

## DEF-001: PUT request on /users endpoint does not clear unmodified fields

**Priority:** Medium

**Description:**
When sending a `PUT` request to update a user, only the fields included in the request payload are updated. Fields that are omitted from the payload retain their original values instead of being cleared/reset, which does not match standard `PUT` semantics.

**Steps to Reproduce:**
1. Send `GET /users/1` and note the full user object (all fields populated).
2. Send `PUT /users/1` with a partial payload, e.g. `{"name": "Updated Name"}`.
3. Inspect the response body.

**Expected Result:**
Per standard REST conventions, `PUT` should perform a **full replacement** of the resource. Fields not included in the request body should be cleared or reset (i.e., the response should only reflect the fields sent, with the rest empty/null) — this is the behavior that distinguishes `PUT` from `PATCH`.

**Actual Result:**
Only the `name` field is updated in the response. All other fields (`username`, `email`, `address`, `phone`, etc.) remain unchanged and fully populated, as if a `PATCH` request had been sent instead.

**Notes:**
This may not be a genuine defect — it is likely a limitation/design choice of DummyJSON.

---

## DEF-002: DELETE request on /users endpoint returns 200 with a body instead of 204 with an empty body

**Priority:** Low

**Description:**
Sending a `DELETE` request to a user resource returns HTTP `200 OK` along with a response body, rather than the conventional `204 No Content` with an empty body.

**Steps to Reproduce:**
1. Send `DELETE /users/1`.
2. Inspect the status code and response body.

**Expected Result:**
Per REST conventions, a successful `DELETE` should return `204 No Content` with an empty response body, since there is no resource left to return.

**Actual Result:**
Response returns `200 OK` with a response body (`{}`).

**Notes:**
Likely due to the fake/mock nature of the REST API being tested (DummyJSON), rather than a true defect. Since the API does not persist deletions, it may default to a generic `200` response instead of implementing the stricter `204` convention.

---

## DEF-003: PUT request on /posts endpoint with empty title field succeeds instead of returning a validation error

**Priority:** Medium

**Description:**
Sending a `PUT` request to create/update a post with an empty `title` field is accepted and returns a success response, instead of being rejected for failing field validation.

**Steps to Reproduce:**
1. Send `PUT /posts/1` with payload: `{"title": "", "body": "Some content", "userId": 1}`.
2. Inspect the status code and response body.

**Expected Result:**
An empty `title` field should fail server-side validation and return `400 Bad Request` with an appropriate error message, since `title` is expected to be a required, non-empty field.

**Actual Result:**
Request returns `201`, and the post is "updated" with an empty title with no validation error raised.

**Notes:**
This is consistent with DummyJSON being a mock API that does not implement real input validation. On a real backend, this would be a genuine and reportable defect, since accepting empty required fields could lead to data integrity issues downstream.

---

## DEF-004: DELETE request on /posts endpoint returns 200 with a body instead of 204 with an empty body

**Priority:** Low

**Description:**
Sending a `DELETE` request to a post resource returns HTTP `200 OK` along with a response body, rather than the conventional `204 No Content` with an empty body.

**Steps to Reproduce:**
1. Send `DELETE /posts/1`.
2. Inspect the status code and response body.

**Expected Result:**
Per REST conventions, a successful `DELETE` should return `204 No Content` with an empty response body.

**Actual Result:**
Response returns `200 OK` with a response body (`{}`).

**Notes:**
Same root cause as DEF-002 — likely a limitation of the fake REST API rather than a true defect. Documenting for consistency, since both `/users` and `/posts` DELETE endpoints exhibit identical behavior.

---

## Summary

| ID | Endpoint | Priority | Status |
|---|---|---|---|
| DEF-001 | PUT /users | Medium | Documented — likely mock API limitation |
| DEF-002 | DELETE /users | Low | Documented — likely mock API limitation |
| DEF-003 | PUT /posts | Medium | Documented — likely mock API limitation |
| DEF-004 | DELETE /posts | Low | Documented — likely mock API limitation |

