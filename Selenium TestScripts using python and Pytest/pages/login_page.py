from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    USERNAME    = (By.ID, "user-name")
    PASSWORD    = (By.ID, "password")
    LOGIN_BTN   = (By.ID, "login-button")
    ERROR_MSG   = (By.CLASS_NAME, "error-message-container")

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MSG)
        ).text

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()