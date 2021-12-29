from base_form.base_page import Base
from loginswaglabs.pages_login.login_form import LoginPageSwagLabs
from time import sleep
import allure
import pytest


@pytest.mark.usefixtures('set_up')
@allure.feature("Open Swag Labs")
@allure.story("Opens the Swag Labs Login page")
class TestPositiveLoginPage(Base):
    @allure.title("compare credentials positive test")
    @allure.testcase("Username & password inputs compare")
    @allure.severity("Low")
    def test_01(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username_input = "standard_user"
        username_output = "standard_user"
        login.input_username(username_input)
        driver.implicitly_wait(50)
        assert username_input == username_output, "positive test failed"

        password_input = "secret_sauce"
        password_output = "secret_sauce"
        login.input_password(password_input)
        driver.implicitly_wait(50)
        assert password_input == password_output, "positive test failed"

    @allure.testcase("Login with a valid username and valid password")
    @allure.title("Login with valid credentials")
    @allure.severity("Medium")
    def test_02(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username_input = "standard_user"
        password_input = "secret_sauce"
        login.input_username(username_input)
        login.input_password(password_input)
        login.login_button()
        sleep(5)

    @allure.testcase("Locked Out User login test")
    @allure.title("Locked Out User login test")
    @allure.severity("Medium")
    def test_03(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username_input = "locked_out_user"
        password_input = "secret_sauce"
        login.input_username(username_input)
        login.input_password(password_input)
        login.login_button()
        assert "Feedback has been sent to the administrator" not in driver.page_source
        sleep(5)

    @allure.testcase("Problem User login test")
    @allure.title("Problem User login test")
    @allure.severity("Medium")
    def test_04(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username_input = "problem_user"
        password_input = "secret_sauce"
        login.input_username(username_input)
        login.input_password(password_input)
        login.login_button()
        assert "Feedback has been sent to the administrator" not in driver.page_source
        sleep(5)

    @allure.testcase("Performance Glitch User login test")
    @allure.title("Performance Glitch User login test")
    @allure.severity("Medium")
    def test_05(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username_input = "performance_glitch_user"
        password_input = "secret_sauce"
        login.input_username(username_input)
        login.input_password(password_input)
        login.login_button()
        sleep(5)

    @allure.testcase("Wrong user credentials login test")
    @allure.severity("Medium")
    @allure.description("Messages for invalid login")
    @allure.title("Login with invalid credentials & error message")
    def test_06(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username = "test"
        password = "test"
        login.input_username(username)
        login.input_password(password)
        login.login_button()
        assert "Epic sadface: Username and password do not match any user in this service" in driver.page_source, \
            "positive test failed "
        sleep(5)

    @allure.testcase("Warning error message remove button test")
    @allure.title("Error button click case")
    @allure.severity("minor")
    def test_07(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username = ""
        password = ""
        login.input_username(username)
        login.input_password(password)
        login.login_button()
        login.error_button()
        sleep(5)
