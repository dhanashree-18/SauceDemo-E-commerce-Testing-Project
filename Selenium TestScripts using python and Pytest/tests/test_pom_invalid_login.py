import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

def test_pom_invalid_login(setup):
	driver = setup

	login_page = LoginPage(driver)
	login_page.login("standard_user", "wrong_password")

	actual_msg = login_page.get_error_message()
	expected_msg = "Epic sadface: Username and password do not match any user in this service"

	assert actual_msg == expected_msg