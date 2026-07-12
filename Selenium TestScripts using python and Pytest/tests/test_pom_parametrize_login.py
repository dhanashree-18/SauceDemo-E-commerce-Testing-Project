import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected_msg",[
	("standard_user", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
	("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
	("", "secret_sauce", "Epic sadface: Username is required"),
	("standard_user", "", "Epic sadface: Password is required"),
])

def test_pom_parametrize_login(setup, username, password, expected_msg):
	driver = setup
	login_page = LoginPage(driver)
	login_page.login(username, password)
	actual_msg = login_page.get_error_message()
	assert actual_msg == expected_msg