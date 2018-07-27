from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Utils:

    @staticmethod
    def wait_for_element_to_be_visible(self, driver, element, timeout=''):
        if timeout == '':
            timeout = 10

        el = WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(element))

        return el

    @staticmethod
    def wait_for_element_to_be_clickable(self, driver, element, timeout=''):
        if timeout == '':
            timeout = 10

        el = WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(element))

        return el

    @staticmethod
    def get_element(self, driver, element):
        return driver.find_element(element)

    @staticmethod
    def get_text_from_element(self, driver, element):
        el = Utils.wait_for_element_to_be_visible(self, driver, element)
        text = el.text

        return text

    @staticmethod
    def driver_redirector(self, driver, first_class, second_class, boolean=''):
        if boolean == '':
            boolean = True

        if boolean:
            return first_class
        else:
            return second_class





