from selenium.webdriver.common.by import By
from .Utils import Utils
from .EmailPage import EmailPage

class HomePage:

    #__ACCOUNT_BUTTON = (By.CSS_SELECTOR, '.em.em-user_fill.navbar-icon')
    __ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'a[href$="/user/login?ref=hdr_login_btn"]')

    def __init__(self, driver):
        self.driver = driver

    def click_account(self):
        account_button = Utils.wait_for_element_to_be_clickable(self, self.driver, self.__ACCOUNT_BUTTON)
        account_button.click()

        return EmailPage(self.driver)

