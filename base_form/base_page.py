from selenium import webdriver
import pytest

path = 'drivers/chromedriver.exe'


class Base:

    @pytest.fixture()
    def set_up(self):
        self.driver = webdriver.Chrome(path)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
