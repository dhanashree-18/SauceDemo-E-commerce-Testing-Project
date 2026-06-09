from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

driver.find_element(By.ID, "shopping_cart_container").click()
driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("XYZ")
driver.find_element(By.ID, "last-name").send_keys("PQR")
driver.find_element(By.ID, "postal-code").send_keys("1111")

driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()

assert "checkout-complete" in driver.current_url

driver.quit()

