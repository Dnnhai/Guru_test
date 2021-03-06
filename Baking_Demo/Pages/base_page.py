import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 60
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def navigate_to(self, url):
        self.driver.get(url)


    def get_title(self):
        return self.driver.title
        # this function performs click on web element whose locator is passed to it.

    def click(self, by_locator):
        message = "Click on the element with locator '{}'"
        logging.info(message.format(','.join(by_locator)))

        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        message = "Enter value '{}' into the element with locator '{}'"
        logging.info(message.format(text, ','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))
        message = "Get text '{}' from the element with the locator '{}'"
        logging.info(message.format(element.text, ','.join(by_locator)))
        return element.text

    def is_visible(self, by_locator):
        message = "Check the element with the locator '{}' is visible or not"
        logging.info(message.format(','.join(by_locator)))

        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.is_displayed()

    def is_invisible(self, by_locator):
        message = "Check the element with the locator '{}' is visible or not"
        logging.info(message.format(','.join(by_locator)))

        flag = False
        try:
            element = self.driver.find_element(by_locator)
            element.is_displayed()
        except:
            flag = True
            pass

        return flag

    def get_current_url(self):
        return self.driver.current_url