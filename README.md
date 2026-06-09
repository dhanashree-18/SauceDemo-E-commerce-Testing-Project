Project Name - SauceDemo E-commerce Website

* Project Overview
This project contains:
- Exploratory Testing Report
- Manual Test Cases
- Selenium Automation Test Scripts using Python and PyTest

Application Tested:
https://www.saucedemo.com/

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Tools & Technologies
- Python
- Selenium WebDriver
- PyTest
- Chrome Browser

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Wait Strategy Used
- Implicit Wait (Global) → Set once in conftest.py, applies to all tests
- Explicit Wait → Used at page transitions in each test script
  - After login → waits for inventory page to load
  - After checkout click → waits for checkout form to load
  - After continue click → waits for order summary to load
  - After finish click → waits for order complete page to load

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Setup Instructions

1. Install Python
2. Install required packages:

pip install selenium pytest

------------------------------------------------------------------------------------------------------------------------------------------------------------

* Run Automation Scripts

*** Run normal Selenium scripts:
1] python valid_login.py
2] python cart_verify.py
3] python verify_checkout.py

*** Run PyTest scripts:
1] py -m pytest test_valid_login.py
2] py -m pytest test_cart.py
3] py -m pytest test_checkout.py

OR 

* To run all Pytest test scripts together:

py -m pytest 

------------------------------------------------------------------------------------------------------------------------------------------------------------

** Automated Test Scenarios
- Valid Login
- Add Product to Cart
- Successful Checkout

------------------------------------------------------------------------------------------------------------------------------------------------------------

** Test Results
All 3 test cases passed successfully!

![All Tests Passed](screenshots/All_Test_Passed_Result.png)
