from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
	def __init__(self, driver):
		self.driver = driver

	MENU_BTN = (By.ID, "react-burger-menu-btn")
	ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
	CART_BTN = (By.ID, "shopping_cart_container")
	CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
	LOGOUT_BTN = (By.ID, "logout_sidebar_link")
	LOGIN_BTN = (By.ID, "login-button")

	def click_menu_icon(self):
		self.driver.find_element(*self.MENU_BTN).click()

	def add_to_cart(self):
		self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

	def click_cart_icon(self):
		self.driver.find_element(*self.CART_BTN).click()

	def get_cart_badge(self):
		return self.driver.find_element(*self.CART_BADGE).text

	def click_logout_btn(self):
		self.driver.find_element(*self.LOGOUT_BTN).click()

	def is_login_page_displayed(self):
		return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BTN)).is_displayed()