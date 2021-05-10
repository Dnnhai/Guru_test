from behave import *
import time
from Testcases.base_test import BaseTest
from Pages.manager_homepage import ManageHomepage
from Locators.manager_page_locators import ManagerPageLocator

Myname = "Nguyen Hai a"
dayOB = 11111991
address = "Vo Van Ngan"
city = "Ho Chi Minh"
state = "Thu Duc"
PINcode = "122133"
MoblieNo = "0987654321"
email = "qw12@gmail.com"
password = "1234567890aaa"
deposit_value = 123455
deposit_amount = 12000
mess2=''
mess3=''

class CustomerCreation(BaseTest):
    ##### create new user ###################################################################################
    @when(u'I click to customer name field and enter my name "NguyenHai" to name field')
    def step_impl(context):
        time.sleep(1)
        context.customer = ManageHomepage(context.driver)
        context.customer.click(ManagerPageLocator().CUSTOMER_NAME)
        context.customer.enter_customer_value(Myname)

    @when(u'I enter day of birth "11111991" to day of birth field')
    def step_impl(context):
        context.day_of_birth = ManageHomepage(context.driver)
        context.day_of_birth.enter_common_value(ManagerPageLocator().DATE_OF_BIRTH, dayOB)
        time.sleep(1)

    @when(u'enter addresss "Vo Van Ngan" to address feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().ADDRESS, address)
        time.sleep(1)

    @when(u'enter city "Ho Chi Minh" to city feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().CITY, city)
        time.sleep(1)

    @when(u'enter state "Thu Duc" to state feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().STATE, state)
        time.sleep(1)

    @when(u'enter PIN "122133" to PIN feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().PIN, PINcode)
        time.sleep(1)

    @when(u'enter Mobile Number "0987654321" to Mobile Number feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().MOBILE_NUMBER, MoblieNo)
        time.sleep(1)

    @when(u'enter email "a123@a.aa" to email feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().EMAIL, email)
        time.sleep(1)

    @when(u'enter Password "1234567890" to Password feild')
    def step_impl(context):
        context.address = ManageHomepage(context.driver)
        context.address.enter_common_value(ManagerPageLocator().PASSWORD_CUSTOMER, password)
        time.sleep(1)

    @when(u'click submit button')
    def step_impl(context):
        ManageHomepage(context.driver).click_submit_customer()
        time.sleep(2)

    @then(u'message "Customer Registered Successfully!!!" must be show')
    def step_impl(context):
        mess2 = ManageHomepage(context.driver).get_message(ManagerPageLocator().MESSAGE_SUCCESSFUL_SHOW)
        if (mess2 == 'Customer Registered Successfully!!!'):
            assert(True, "Test Passed")
        else:
            assert (False, "Test Failed")

##### create new Account ###################################################################################

    @when(u'I have user ID after that i click to New Account Tag')
    def step_impl(context):
        context.userID = ManageHomepage(context.driver).get_message(ManagerPageLocator().CUSTOMER_ID_SHOW)
        context.new_account = ManageHomepage(context.driver)
        context.new_account.click_new_account_tag()

    @when(u'I enter user ID to customer field')
    def step_impl(context):
        print(context.userID)
        context.customerfield = ManageHomepage(context.driver)
        context.customerfield.enter_common_value(ManagerPageLocator().CUSTOMER_ID_FIELD, context.userID)
        time.sleep(1)

    @when(u'I enter Initial deposit "123455" to deposit field')
    def step_impl(context):
        context.depositfield = ManageHomepage(context.driver)
        context.depositfield.enter_common_value(ManagerPageLocator().DEPOSIT_FEILD, deposit_value)

    @when(u'I click submit account button')
    def step_impl(context):
        ManageHomepage(context.driver).click_submit_account()
        time.sleep(2)

    @then(u'message "Account Generated Successfully!!!" must be show')
    def step_impl(context):
        context.AccID = ManageHomepage(context.driver).get_message(ManagerPageLocator().ACC_ID_SHOW)
        print(context.AccID)
        mess3 = ManageHomepage(context.driver).get_message(ManagerPageLocator().MESSAGE_SUCCESSFUL_SHOW)
        if (mess3 == 'Account Generated Successfully!!!'):
            assert(True, "Test Passed")
        else:
            assert (False, "Test Failed")


##### Deposite ###################################################################################


    @when(u'I have account ID after that i click to Deposite Tag')
    def step_impl(context):
        context.AccID = ManageHomepage(context.driver).get_message(ManagerPageLocator().ACC_ID_SHOW)
        context.new_deposite = ManageHomepage(context.driver)
        context.new_deposite.click_deposite_tag()

    @when(u'I enter account ID to account No field')
    def step_impl(context):
        print(context.AccID)
        context.deposite_acc = ManageHomepage(context.driver)
        context.deposite_acc.enter_common_value(ManagerPageLocator().ACCOUNT_NO, context.AccID)
        time.sleep(1)

    @when(u'I enter Initial deposit "12000" to deposit field and fill description "demo deposite"')
    def step_impl(context):
        context.deposit_ammout = ManageHomepage(context.driver)
        context.deposit_ammout.enter_common_value(ManagerPageLocator().AMOUNT_DEPOSITE, deposit_amount)
        context.deposit_ammout.enter_common_value(ManagerPageLocator().AMOUNT_DESCRIPTION, "10 chars")

    @when(u'I click submit deposite button')
    def step_impl(context):
        ManageHomepage(context.driver).click_submit_deposite()
        time.sleep(2)

    @then(u'message "Transaction details of Deposit for Account <Acc_No>" must be show')
    def step_impl(context):
        context.AccNo = ManageHomepage(context.driver).get_message(ManagerPageLocator().ACC_NUMBER_SHOW_AFTER_DEPOSITE)
        mess3 = ManageHomepage(context.driver).get_message(ManagerPageLocator().MESSAGE_SUCCESSFUL_SHOW)
        if (mess3 == 'Transaction details of Deposit for Account ' + context.AccNo):
            assert(True, "Test Passed")
        else:
            assert (False, "Test Failed")
        context.driver.close()
