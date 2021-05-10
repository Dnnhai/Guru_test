import logging

from Locators.manager_page_locators import ManagerPageLocator
# from Objects.product import Product
from Pages.base_page import BasePage

class ManageHomepage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def enter_customer_value(self, your_text):
        self.enter_text(ManagerPageLocator.CUSTOMER_NAME, your_text)

    def enter_day_of_birth_value(self, your_text):
        self.enter_text(ManagerPageLocator.DATE_OF_BIRTH, your_text)

    def enter_common_value(self,locator, your_text):
        self.enter_text(locator, your_text)

    def click_submit_customer(self):
        self.click(ManagerPageLocator.SUBMIT_CUSTOM_BUTTON)

    def click_reset_customer(self):
        return self.click(ManagerPageLocator.RESET_CUSTOM_BUTTON)

################################################################################################################

    def click_new_customer_tag(self):
        return self.click(ManagerPageLocator.NEW_CUSTOMER_TAG)

    def click_new_account_tag(self):
        return self.click(ManagerPageLocator.NEW_ACCOUNT_TAG)

    def click_submit_account(self):
        self.click(ManagerPageLocator.SUBMIT_ACCOUNT_BUTTON)

 ################################################################################################################


    def click_deposite_tag(self):
        return self.click(ManagerPageLocator.DEPOSIT_TAG)

    def click_submit_deposite(self):
        self.click(ManagerPageLocator.SUBMIT_DEPOSITE_BUTTON)

    def get_manager_url(self):
        return self.get_current_url()

    def get_message(self, locator):
        return self.get_text(locator)

