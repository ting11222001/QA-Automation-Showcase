# Exploratory Testing Session

## Charter

| Field       | Detail                                                                 |
|-------------|------------------------------------------------------------------------|
| Session ID  | EX-01                                                                  |
| Tester      | Li-Ting                                                          |
| Date        | Apr 26 2026                                                                |
| Duration    | 30 minutes                                                             |
| Target      | SauceDemo checkout and cart flows                                      |
| Mission     | Explore the cart and checkout flow to find defects outside the scripted test cases |
| Approach    | Time-boxed session, 30 minutes, no scripted steps |

---

## Areas Explored

- Adding multiple items to the cart
- Removing items from the cart
- Navigating back and forward during checkout
- Submitting the checkout form with missing fields
- Behaviour after completing an order

---

## Session Notes

| Time  | Action                                                                 | Observation                                                                 |
|-------|------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 0:00  | Added 3 items to cart                                                  | Cart badge updated correctly each time                                      |
| 0:05  | Removed 1 item from cart page                                          | Item removed, badge count decreased correctly                               |
| 0:08  | Clicked browser back button during checkout information step           | Returned to cart page, items still present                                  |
| 0:12  | Submitted checkout form with all fields empty                          | Error message displayed: "First Name is required"                           |
| 0:15  | Submitted checkout form with first name and last name only, no postcode| Error message displayed: "Postal Code is required"                          |
| 0:20  | Completed full checkout, then clicked browser back button              | Returned to checkout complete page, no error shown but order was already placed. No confirmation that a second order was not submitted. |
| 0:25  | Logged in as `problem_user` and added item to cart                     | Product image on cart page was different from the product image on the inventory page |
| 0:30  | Session ended                                                          |                                                                             |

---

## Findings

| ID    | Summary                                                                 | Severity | Filed As     |
|-------|-------------------------------------------------------------------------|----------|--------------|
| BUG-01 | Product image mismatch between inventory and cart for `problem_user`  | Medium   | [DEFECT-REPORT.md](DEFECT-REPORT.md) |

---

## Areas Not Covered

- Behaviour with a locked-out user during checkout
- Sorting products while items are in the cart
- Session timeout behaviour

---

## Follow-up Items

- Consider adding a test case for form validation to the automated suite
- BUG-01 written as a formal defect report with reproduction steps, expected vs actual results, and severity rating (see [DEFECT-REPORT.md](DEFECT-REPORT.md))