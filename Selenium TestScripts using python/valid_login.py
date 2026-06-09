from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch browser
driver = webdriver.Chrome()

# Open SauceDemo website
driver.get("https://www.saucedemo.com/")

# Maximize window
driver.maximize_window()

# Enter username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter password
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login button
driver.find_element(By.ID, "login-button").click()

# Basic validation after login (check URL contains inventory)
assert "inventory" in driver.current_url

# Close browser
driver.quit()