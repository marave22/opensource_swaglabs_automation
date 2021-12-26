from loginswaglabs.pages.base_page import Base
from loginswaglabs.pages.login_form import LoginPageSwagLabs
import pytest


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):
    def test_01(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        username_input = "standard_user"
        username_output = "standard_user"
        login.input_username(username_input)
        driver.implicitly_wait(20)
        assert username_input == username_output, "positive test failed"

        password_input = "secret_sauce"
        password_output = "secret_sauce"
        login.input_password(password_input)
        driver.implicitly_wait(20)
        assert password_input == password_output, "positive test failed"

    def test_02(self):
        driver = self.driver
        login = LoginPageSwagLabs(driver)
        login.error_button()