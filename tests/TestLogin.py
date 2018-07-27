import pytest
from pages.EmailPage import EmailPage
from pages.BasePage import BasePage
from pages.HomePage import HomePage

@pytest.mark.usefixtures('setup')
class TestLogin(BasePage):

    __INVALID_EMAIL_TEXT = 'Email invalid'
    __MISSING_EMAIL = 'Camp obligatoriu'

    def test_invalid_email(self, setup):
        home_page = HomePage(setup)
        login_step = home_page.click_account()
        login_step.login_email_step('asdf', False)
        error_text = login_step.get_login_error_text()

        assert self.__INVALID_EMAIL_TEXT == error_text
        


    def test_missing_email(self, setup):
        home_page = HomePage(setup)
        login_step = home_page.click_account()
        login_step.login_email_step('', False)
        error_text = login_step.get_login_error_text()

        assert self.__MISSING_EMAIL == error_text
