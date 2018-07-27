import pytest
from selenium import webdriver


class BasePage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome("C:\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get('https://www.emag.ro/homepage')

        yield self.driver

        print('Close web driver')
        self.driver.close()
        self.driver.quit()



