import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

def test_pom_checkout(setup):
	driver = setup

	login_page = LoginPage(driver)
	login_page.login("standard_user", "secret_sauce")

	product_page = ProductPage(driver)
	product_page.add_to_cart()
	product_page.click_cart_icon()

	checkout_page = CheckoutPage(driver)
	checkout_page.click_checkout_btn()

	checkout_page.enter_first_name("John")
	checkout_page.enter_last_name("Smith")
	checkout_page.enter_postal_code("123456")

	checkout_page.click_continue_btn()
	checkout_page.click_finish_btn()
	
	assert "checkout-complete" in driver.current_url