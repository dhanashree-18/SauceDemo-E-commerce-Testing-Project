import pytest
from selenium import webdriver

@pytest.fixture
def setup():
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get("https://www.saucedemo.com/")
	driver.implicitly_wait(10)
	yield driver
	driver.quit()