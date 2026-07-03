Project Name - SauceDemo E-commerce Website

* Project Overview
This project contains:
- Exploratory Testing Report
- Manual Test Cases
- Selenium Automation Test Scripts using Python and PyTest
- Page Object Model (POM) Implementation

Application Tested:
https://www.saucedemo.com/

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Tools & Technologies
- Python
- Selenium WebDriver
- PyTest
- Chrome Browser
- GitHub Actions (CI/CD)

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Wait Strategy Used
- Implicit Wait (Global) → Set once in conftest.py, applies to all tests
- Explicit Wait → Used at page transitions in each test script
  - After login → waits for inventory page to load
  - After checkout click → waits for checkout form to load
  - After continue click → waits for order summary to load
  - After finish click → waits for order complete page to load

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Design Pattern
- Page Object Model (POM) → Separate class created per page
  - LoginPage    → login locators and actions
  - ProductPage  → product and cart locators and actions
  - CheckoutPage → complete checkout flow locators and actions

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Project Structure

Selenium TestScripts using python and Pytest/
│
├── pages/
│   ├── login_page.py
│   ├── product_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── conftest.py
│   ├── test_pom_login.py
│   ├── test_pom_cart.py
│   ├── test_pom_checkout.py
│   ├── test_pom_invalid_login.py
│   ├── test_pom_logout.py
│   ├── test_valid_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_invalid_login.py
│   └── test_logout.py

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Setup Instructions

1. Install Python
2. Install required packages:

pip install -r requirements.txt

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Run Automation Scripts

*** Run normal Selenium scripts:
1] python valid_login.py
2] python cart_verify.py
3] python verify_checkout.py

*** Run PyTest scripts - POM Based Tests:
1] py -m pytest tests/test_pom_login.py
2] py -m pytest tests/test_pom_cart.py
3] py -m pytest tests/test_pom_checkout.py
4] py -m pytest tests/test_pom_invalid_login.py
5] py -m pytest tests/test_pom_logout.py

*** Run PyTest scripts - Original Tests:
1] py -m pytest tests/test_valid_login.py
2] py -m pytest tests/test_cart.py
3] py -m pytest tests/test_checkout.py
4] py -m pytest tests/test_invalid_login.py
5] py -m pytest tests/test_logout.py

OR

* To run all Pytest test scripts together:

py -m pytest -v

------------------------------------------------------------------------------------------------------------------------------------------------------------

** Automated Test Scenarios

*** POM Based Tests (Current)
- Valid Login
- Add Product to Cart
- Complete Checkout Flow
- Invalid Login Error Message
- Logout Successfully

*** Original Tests (Pre-POM)
- Valid Login
- Add Product to Cart
- Complete Checkout Flow
- Invalid Login Error Message
- Logout Successfully

------------------------------------------------------------------------------------------------------------------------------------------------------------

* CI/CD
- GitHub Actions workflow runs all 10 tests automatically on every push
- Headless Chrome auto-detected via CI environment variable
- No manual configuration needed between local and CI environments

------------------------------------------------------------------------------------------------------------------------------------------------------------

** Test Results
All 10 test cases passed successfully!

![All Tests Passed](screenshots/All_Test_Passed_Result.png)
