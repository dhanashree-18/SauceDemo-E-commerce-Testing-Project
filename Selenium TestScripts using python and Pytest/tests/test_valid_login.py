from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.login
@pytest.mark.smoke
def test_valid_login(setup):
	
	driver = setup
	
	driver.find_element(By.ID, "user-name").send_keys("standard_user")
	driver.find_element(By.ID, "password").send_keys("secret_sauce")
	driver.find_element(By.ID, "login-button").click()

	WebDriverWait(driver,10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
	)
	
	assert "inventory" in driver.current_url, "Login failed - inventory page not reached"