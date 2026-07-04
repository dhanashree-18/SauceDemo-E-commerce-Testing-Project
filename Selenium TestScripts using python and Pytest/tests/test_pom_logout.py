import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.logout
@pytest.mark.regression
def test_pom_logout(setup):
	driver = setup

	login_page = LoginPage(driver)
	login_page.login("standard_user", "secret_sauce")

	product_page = ProductPage(driver)
	product_page.click_menu_icon()
	product_page.click_logout_btn()
	

	assert driver.current_url == "https://www.saucedemo.com/"
	assert product_page.is_login_page_displayed()
	


	