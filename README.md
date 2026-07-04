# Reqres API Automation Framework

API test automation framework built with Python and pytest targeting the [Reqres.in](https://reqres.in) REST API.


---

## Tech Stack
Python 3.12 | requests | pytest | Allure | Faker | GitHub Actions

---

## Test Coverage
| Module | Scenarios |
|---|---|
| GET Users | List users, single user, required fields, 404 handling |
| POST User | Create user, response schema, response time |
| PUT / PATCH | Full and partial update |
| DELETE | 204 status, empty response body |
| Auth | Valid login, token validation, missing password error |

---
```
Add a `.env` file at project root with `REQRES_API_KEY=your_key_here`, then:
```bash
python -m pytest tests/ -v
```