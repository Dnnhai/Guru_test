from behave import *
from Pages.login_page import LoginPage
from Objects.account import Account
from Testcases.base_test import BaseTest
from Pages.manager_homepage import ManageHomepage


class Guru99Bank1(BaseTest):

    @given(u'I launch browser')
    def setUp(context):
        # context.driver = webdriver.Firefox(executable_path=r'Drivers\geckodriver.exe')
        context.driver = BaseTest.setUp()

    @when(u'I open the hompage')
    def openHomepage(context):
        context.login_page = LoginPage(context.driver)

    @when(u'enter username "{user}" and password "{pwd}" and click on login button')
    def enterUserAndPass(context,user,pwd):
        context.account = Account(user,pwd)
        context.login_page.login(context.account)

    @then(u'I login to managers homepage')
    def step_impl(context):
        try:
            manager = ManageHomepage(context.driver)
            my_url = manager.get_manager_url()
        except:
            context.driver.close()
            assert(False, "Test Failed")

        if (my_url == 'http://demo.guru99.com/v4/manager/Managerhomepage.php'):
            context.driver.close()
            assert(True, "Test Passed")
