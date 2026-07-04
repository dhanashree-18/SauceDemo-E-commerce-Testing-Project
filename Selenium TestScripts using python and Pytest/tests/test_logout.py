from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.logout
@pytest.mark.regression
def test_logout(setup):

	driver = setup
	driver.find_element(By.ID, "user-name").send_keys("standard_user")
	driver.find_element(By.ID, "password").send_keys("secret_sauce")
	driver.find_element(By.ID, "login-button").click()

	WebDriverWait(driver,10).until(
		EC.visibility_of_element_located((By.ID, "react-burger-menu-btn"))
	)
	driver.find_element(By.ID, "react-burger-menu-btn").click()


	WebDriverWait(driver,10).until(
    		EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
	)
	driver.find_element(By.ID, "logout_sidebar_link").click()

	login_btn = WebDriverWait(driver,10).until(
		EC.visibility_of_element_located((By.ID, "login-button"))
	)

	assert driver.current_url == "https://www.saucedemo.com/"
	assert login_btn.is_displayed()