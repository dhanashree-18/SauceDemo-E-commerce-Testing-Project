from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.cart
@pytest.mark.smoke
def test_cart(setup):
	
	driver = setup
	driver.find_element(By.ID, "user-name").send_keys("standard_user")
	driver.find_element(By.ID, "password").send_keys("secret_sauce")
	driver.find_element(By.ID, "login-button").click()

	WebDriverWait(driver,10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
	)

	add_cart = WebDriverWait(driver,10).until(
		EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
	)
	add_cart.click()

	cart_badge = WebDriverWait(driver,10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
	).text

	assert cart_badge == "1"