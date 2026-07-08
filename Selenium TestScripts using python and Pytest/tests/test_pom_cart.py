import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.product_page import ProductPage

@pytest.mark.cart
@pytest.mark.smoke
def test_pom_cart(logged_in_setup):
	driver = logged_in_setup
	product_page = ProductPage(driver)
	product_page.add_to_cart()
	cart_count = product_page.get_cart_badge()
	assert cart_count == "1"