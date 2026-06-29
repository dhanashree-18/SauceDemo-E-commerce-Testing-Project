import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
	chrome_options = Options()
	chrome_options.add_experimental_option("prefs", {
		"credentials_enable_service": False,
		"profile.password_manager_enabled": False,
		"profile.password_manager_leak_detection": False
	})

	
	driver = webdriver.Chrome(options=chrome_options)
	driver.maximize_window()
	driver.get("https://www.saucedemo.com/")
	driver.implicitly_wait(10)
	yield driver
	driver.quit()