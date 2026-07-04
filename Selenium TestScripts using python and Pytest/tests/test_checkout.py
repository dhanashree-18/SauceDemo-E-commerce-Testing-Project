from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.checkout
@pytest.mark.smoke
def test_checkout(setup):
	driver = setup
	driver.find_element(By.ID, "user-name").send_keys("standard_user")
	driver.find_element(By.ID, "password").send_keys("secret_sauce")
	driver.find_element(By.ID, "login-button").click()

	WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))
	)

	driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
	driver.find_element(By.ID, "shopping_cart_container").click()

	checkout_btn = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, "checkout"))
	)
	checkout_btn.click()

	WebDriverWait(driver, 10).until(
		EC.visibility_of_element_located((By.ID, "first-name"))
	)

	driver.find_element(By.ID, "first-name").send_keys("John")
	driver.find_element(By.ID, "last-name").send_keys("Smith")
	driver.find_element(By.ID, "postal-code").send_keys("123456")

	continue_btn = WebDriverWait(driver, 10).until(
		EC.element_to_be_clickable((By.ID, "continue"))
	)
	continue_btn.click()

	finish_btn = WebDriverWait(driver, 20).until(
		EC.element_to_be_clickable((By.ID, "finish"))
	)
	finish_btn.click()

	assert "checkout-complete" in driver.current_url

