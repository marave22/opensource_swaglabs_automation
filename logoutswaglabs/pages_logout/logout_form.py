from logoutswaglabs.locators_logout.locators_logout import LocatorsPathLogout


class LogoutSwagLabs:

    def __init__(self, driver):
        self.driver = driver
        self.username = LocatorsPathLogout.username
        self.password = LocatorsPathLogout.password
        self.login_btn = LocatorsPathLogout.login_btn
        self.burger_btn = LocatorsPathLogout.burger_btn
        self.logout_btn = LocatorsPathLogout.logout_btn

    def input_username(self, text):
        input_username = self.driver.find_element_by_id(self.username)
        input_username.send_keys(text)

    def input_password(self, text):
        input_password = self.driver.find_element_by_id(self.password)
        input_password.send_keys(text)

    def login_button(self):
        login_button = self.driver.find_element_by_id(self.login_btn)
        login_button.click()

    def logout_burger_button(self):
        burger_button = self.driver.find_element_by_id(self.burger_btn)
        burger_button.click()

    def logout_button(self):
        logout_button = self.driver.find_element_by_id(self.logout_btn)
        logout_button.click()
