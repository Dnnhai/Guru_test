from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    INPUT_USERNAME = (By.NAME, 'uid')
    INPUT_PASSWORD = (By.NAME, 'password')
    BUTTON_LOGIN = (By.NAME, 'btnLogin')
    BUTTON_RESET = (By.NAME, 'btnReset')
    LABEL_MISSING_UID = (By.ID, 'message23')
    LABEL_MISSING_UID = (By.ID, 'message18')
