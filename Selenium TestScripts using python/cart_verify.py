from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

assert cart_badge == "1"

driver.quit()

