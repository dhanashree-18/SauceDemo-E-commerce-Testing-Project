from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.login
@pytest.mark.regression
def test_invalid_login(setup):

	driver = setup
	driver.find_element(By.ID, "user-name").send_keys("standard_user")
	driver.find_element(By.ID, "password").send_keys("wrong_password")
	driver.find_element(By.ID, "login-button").click()

	error_msg = WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
	)

	actual_msg = error_msg.text
	
	expected_msg = "Epic sadface: Username and password do not match any user in this service"
	assert actual_msg == expected_msg
	

