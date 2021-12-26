from loginswaglabs.locators.locators import LocatorsPath


class LoginPageSwagLabs:

    def __init__(self, driver):
        self.driver = driver
        self.username = LocatorsPath.username
        self.password = LocatorsPath.password
        self.login_btn = LocatorsPath.login_btn
        self.error_message = LocatorsPath.error_message
        self.error_btn = LocatorsPath.error_btn

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
        error_button = self.driver.find_element_by_id(self.error_btn)
        error_button.click()
