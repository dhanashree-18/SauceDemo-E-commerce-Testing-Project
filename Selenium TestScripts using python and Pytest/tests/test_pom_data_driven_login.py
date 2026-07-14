import sys
import os
import pytest
import csv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

def get_login_data():
	data = []
	with open("test_data/login_data.csv", "r") as file:
		reader = csv.reader(file)
		next(reader)
		for row in reader:
			data.append(row)
	return data

@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize("username, password, expected_msg",get_login_data())

def test_pom_parametrize_login(setup, username, password, expected_msg):
	driver = setup
	login_page = LoginPage(driver)
	login_page.login(username, password)
	actual_msg = login_page.get_error_message()
	assert actual_msg == expected_msg