from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
	def __init__(self, driver):
		self.driver = driver

	CHECKOUT_BTN = (By.ID, "checkout")
	CONTINUE_BTN = (By.ID, "continue")
	FINISH_BTN = (By.ID, "finish")
	FIRST_NAME = (By.ID, "first-name")
	LAST_NAME = (By.ID, "last-name")
	POSTAL_CODE = (By.ID, "postal-code")

	def click_checkout_btn(self):
		self.driver.find_element(*self.CHECKOUT_BTN).click()
		WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME))

	def enter_first_name(self, firstname):
		self.driver.find_element(*self.FIRST_NAME).send_keys(firstname)

	def enter_last_name(self, lastname):
		self.driver.find_element(*self.LAST_NAME).send_keys(lastname)

	def enter_postal_code(self, postalcode):
		self.driver.find_element(*self.POSTAL_CODE).send_keys(postalcode)

	def click_continue_btn(self):
		self.driver.find_element(*self.CONTINUE_BTN).click()
		WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FINISH_BTN))

	def click_finish_btn(self):
		self.driver.find_element(*self.FINISH_BTN).click()




