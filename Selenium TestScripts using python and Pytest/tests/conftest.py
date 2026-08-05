import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.login_page import LoginPage

@pytest.fixture(params=["chrome", "edge"])
def setup(request):
	browser = request.param

	if browser == "chrome":
		chrome_options = ChromeOptions()
		chrome_options.add_experimental_option("prefs", {
			"credentials_enable_service": False,
			"profile.password_manager_enabled": False,
			"profile.password_manager_leak_detection": False
		})
		if os.environ.get("CI"):
			chrome_options.add_argument("--headless")
			chrome_options.add_argument("--no-sandbox")
			chrome_options.add_argument("--disable-dev-shm-usage")
			chrome_options.add_argument("--window-size=1920,1080")
		driver = webdriver.Chrome(options=chrome_options)

	elif browser == "edge":
		edge_options = EdgeOptions()
		edge_options.add_experimental_option("prefs", {
			"credentials_enable_service": False,
			"profile.password_manager_enabled": False,
			"profile.password_manager_leak_detection": False
		})
		if os.environ.get("CI"):
			edge_options.add_argument("--headless")
			edge_options.add_argument("--no-sandbox")
			edge_options.add_argument("--disable-dev-shm-usage")
			edge_options.add_argument("--window-size=1920,1080")
		driver = webdriver.Edge(options=edge_options)

	if not os.environ.get("CI"):
		driver.maximize_window()
	driver.get("https://www.saucedemo.com/")
	driver.implicitly_wait(10)
	yield driver
	driver.quit()

@pytest.fixture
def logged_in_setup(setup):
	driver = setup
	login_page = LoginPage(driver)
	login_page.login("standard_user", "secret_sauce")
	yield driver