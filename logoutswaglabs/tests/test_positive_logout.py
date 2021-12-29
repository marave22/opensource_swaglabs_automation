from time import sleep
from base_form.base_page import Base
from logoutswaglabs.pages_logout.logout_form import LogoutSwagLabs
import allure
import pytest


@pytest.mark.usefixtures('set_up')
@allure.feature("Open Swag Labs")
@allure.story("Testing the Swag Labs Logout Functionality")
class TestPositiveLogout(Base):
    @allure.title("Logout functionality")
    @allure.testcase("Verify the logs for the login and logout session")
    @allure.severity("Medium")
    def test_01(self):
        driver = self.driver
        logout = LogoutSwagLabs(driver)
        username_input = "standard_user"
        password_input = "secret_sauce"
        logout.input_username(username_input)
        logout.input_password(password_input)
        logout.login_button()
        logout.logout_burger_button()
        logout.logout_button(), "negative test failed"
        sleep(5)
