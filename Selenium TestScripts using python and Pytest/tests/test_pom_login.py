import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

@pytest.mark.login
@pytest.mark.smoke
def test_pom_valid_login(setup):
	driver = setup
	login_page = LoginPage(driver)
	
	login_page.login("standard_user", "secret_sauce")
	
	assert "inventory" in driver.current_url