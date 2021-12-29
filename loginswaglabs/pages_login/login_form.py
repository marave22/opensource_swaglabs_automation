from loginswaglabs.locators_login.locators_login import LocatorsPathLogin


class LoginPageSwagLabs:

    def __init__(self, driver):
        self.driver = driver
        self.username = LocatorsPathLogin.username
        self.password = LocatorsPathLogin.password
        self.login_btn = LocatorsPathLogin.login_btn
        self.error_btn = LocatorsPathLogin.error_btn

    def input_username(self, text):
        input_username = self.driver.find_element_by_id(self.username)
        input_username.send_keys(text)

    def input_password(self, text):
        input_password = self.driver.find_element_by_id(self.password)
        input_password.send_keys(text)

    def login_button(self):
        login_button = self.driver.find_element_by_id(self.login_btn)
        login_button.click()

    def error_button(self):
        error_button = self.driver.find_element_by_xpath(self.error_btn)
        error_button.click()
