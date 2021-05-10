from behave import *

from Testcases.base_test import BaseTest
from Pages.manager_homepage import ManageHomepage
from selenium.webdriver.common.keys import Keys
from Locators.manager_page_locators import ManagerPageLocator

class CustomerCreation(BaseTest):

##### create new Customer ###################################################################################
    @when(u'clik on New Customer tag')
    def clickNewCustomerTag(context):
        context.tag = ManageHomepage(context.driver)
        context.tag.click_new_customer_tag()

    @when(u'I do not enter value name field')
    def enterblankvalue(context):
        context.customer = ManageHomepage(context.driver)
        context.customer.click(ManagerPageLocator().CUSTOMER_NAME)
        context.customer.enter_customer_value("")

    @when(u'press TAB button')
    def step_impl(context):
        context.customer = ManageHomepage(context.driver)
        context.customer.enter_customer_value(Keys.TAB)

    @then(u'Error message "Customer name must not be blank" must be show')
    def step_impl(context):
        context.mess = ManageHomepage(context.driver).get_message(ManagerPageLocator().CUSTOMER_NAME_MESSAGE)
        context.driver.close()
        assert context.mess=="Customer name must not be blank"

    @when(u'I enter a number to value name field')
    def step_impl(context):
        context.customer = ManageHomepage(context.driver)
        context.customer.click(ManagerPageLocator().CUSTOMER_NAME)
        context.customer.enter_customer_value("123432")

    @then(u'Error message "Numbers are not allowed" must be show')
    def step_impl_number(context):
        context.mess1 = ManageHomepage(context.driver).get_message(ManagerPageLocator().CUSTOMER_NAME_MESSAGE)
        context.driver.close()
        assert context.mess1 == "Numbers are not allowed"


