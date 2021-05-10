import sys
import unittest

from selenium import webdriver


sys.path.append(".")


# Base class for the test
class BaseTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Admin\Desktop\Interview_Test_Python\Baking_Demo\Drivers\chromedriver.exe')
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        try:
            self.driver.close()
            self.driver.quit()
        except Exception as e:
            pass
