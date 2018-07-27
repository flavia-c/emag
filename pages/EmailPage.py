from selenium.webdriver.common.by import By
from .Utils import Utils
from .PasswordPage import PasswordPage


class EmailPage:
    __EMAIL_FIELD = (By.ID, 'email')
    __CONTINUA = (By.CSS_SELECTOR, '.gui-btn.auth-btn-primary.auth-submit')
    __ERROR_TEXT = (By.CSS_SELECTOR, '.gui-input-explain.-is-error')

    def __init__(self, driver):
        self.driver = driver

    def email_input(self, email):
        email_field = Utils.wait_for_element_to_be_visible(self, self.driver, self.__EMAIL_FIELD)
        email_field.send_keys(email)

    def click_submit(self):
        submit_button = Utils.wait_for_element_to_be_visible(self, self.driver, self.__CONTINUA)
        submit_button.click()

    def login_email_step(self, email, correct_email):
        self.email_input(email)
        self.click_submit()

        return Utils.driver_redirector(self, self.driver, PasswordPage, EmailPage, correct_email)

    def get_login_error_text(self):
        error_message = Utils.get_text_from_element(self, self.driver, self.__ERROR_TEXT)

        return error_message

