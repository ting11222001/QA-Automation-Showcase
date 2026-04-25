# Test Plan: SauceDemo Web Application

## 1. Scope

This test plan covers manual and automated testing of the [SauceDemo](https://www.saucedemo.com) demo e-commerce web application.

**In scope:**
- User login (valid and invalid credentials)
- Add to cart
- Checkout flow
- Logout
- Error handling and validation messages

**Out of scope:**
- Performance testing
- Mobile or responsive testing
- API testing

---

## 2. Approach

This plan follows a shift-left approach. Test cases were written before automation was built, mirroring how a QA engineer would work inside a sprint.

| Layer                | Tool                  | Purpose                                      |
|---------------------|-----------------------|----------------------------------------------|
| Manual test cases   | TestRail              | Author, execute, and track test run results  |
| Automated tests     | Python + Selenium     | Regression coverage on every push            |
| CI                  | GitHub Actions        | Run automated tests on every push            |
| Exploratory testing | Charter-based session | Discover defects outside scripted coverage   |
| Defect tracking     | JIRA format           | Document and track bugs found                |

---

## 3. Test Cases

Each test case below was authored in TestRail before automation was written. See `/testrail-evidence/` for screenshots of the test run results.

---

### TC01: Valid Login

**Precondition:** User is on the SauceDemo login page.

| Step | Action                                              | Expected Result                        |
|------|-----------------------------------------------------|----------------------------------------|
| 1    | Go to https://www.saucedemo.com                     | Login page is displayed                |
| 2    | Enter username: `standard_user`                     | Username field accepts input           |
| 3    | Enter password: `secret_sauce`                      | Password field accepts input           |
| 4    | Click the Login button                              | User is redirected to the products page|

**Status:** Pass

---

### TC02: Invalid Login

**Precondition:** User is on the SauceDemo login page.

| Step | Action                                              | Expected Result                                      |
|------|-----------------------------------------------------|------------------------------------------------------|
| 1    | Go to https://www.saucedemo.com                     | Login page is displayed                              |
| 2    | Enter username: `standard_user`                     | Username field accepts input                         |
| 3    | Enter password: `wrong_password`                    | Password field accepts input                         |
| 4    | Click the Login button                              | Error message is displayed: "Username and password do not match" |

**Status:** Pass

---

### TC03: Add Item to Cart

**Precondition:** User is logged in as `standard_user`.

| Step | Action                                              | Expected Result                        |
|------|-----------------------------------------------------|----------------------------------------|
| 1    | On the products page, locate any product            | Product is visible                     |
| 2    | Click the "Add to cart" button on that product      | Button label changes to "Remove"       |
| 3    | Check the cart icon in the top right                | Cart icon shows a count of 1           |

**Status:** Pass

---

### TC04: Complete Checkout

**Precondition:** User is logged in and has 1 item in the cart.

| Step | Action                                              | Expected Result                        |
|------|-----------------------------------------------------|----------------------------------------|
| 1    | Click the cart icon                                 | Cart page is displayed with 1 item     |
| 2    | Click "Checkout"                                    | Checkout information form is displayed |
| 3    | Enter first name, last name, and postal code        | Fields accept input                    |
| 4    | Click "Continue"                                    | Order summary page is displayed        |
| 5    | Click "Finish"                                      | Order confirmation page is shown       |

**Status:** Pass

---

### TC05: Logout

**Precondition:** User is logged in as `standard_user`.

| Step | Action                                              | Expected Result                        |
|------|-----------------------------------------------------|----------------------------------------|
| 1    | Click the hamburger menu in the top left            | Side menu opens                        |
| 2    | Click "Logout"                                      | User is returned to the login page     |

**Status:** Pass

---

## 4. TestRail Evidence

Test cases were authored and executed in TestRail. Screenshots of the test run are in `/testrail-evidence/`.

---

## 5. Exploratory Testing

A separate exploratory session was conducted outside scripted coverage. See:

- [EXPLORATORY-SESSION.md](exploratory/EXPLORATORY-SESSION.md)
- [DEFECT-REPORT.md](exploratory/DEFECT-REPORT.md)

---

## 6. Test Environment

| Item       | Detail                      |
|------------|-----------------------------|
| Site       | https://www.saucedemo.com   |
| Browser    | Chrome (latest)             |
| Framework  | Python 3.x + Selenium 4.x   |
| CI         | GitHub Actions              |
| Test tool  | TestRail                    |