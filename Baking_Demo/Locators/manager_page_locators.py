from selenium.webdriver.common.by import By

class ManagerPageLocator(object):

    #
    #New customer locaters
    #
    NEW_CUSTOMER_TAG = (By.XPATH,"//a[@href='addcustomerpage.php']")
    CUSTOMER_NAME = (By.XPATH, "//input[@name='name']")
    CUSTOMER_NAME_MESSAGE = (By.XPATH, "//label[@id='message']")

    GENDER_MALE = (By.XPATH, "//input[@type='radio'][1]")
    GENDER_FEMALE = (By.XPATH, "//input[@type='radio'][2]")

    DATE_OF_BIRTH = (By.XPATH, "//input[@name='dob']")
    DATE_OF_BIRTH_MESSAGE = (By.XPATH, "//label[@id='message24']")

    ADDRESS = (By.XPATH, "//textarea[@name='addr']")
    ADDRESS_MESSAGE = (By.XPATH, "/label[@id='message3']")

    CITY = (By.XPATH, "//input[@name='city']")
    CITY_MESSAGE = (By.XPATH, "/label[@id='message4']")

    STATE = (By.XPATH, "//input[@name='state']")
    STATE_MESSAGE = (By.XPATH, "/label[@id='message5']")

    PIN = (By.XPATH, "//input[@name='pinno']")
    PIN_MESSAGE = (By.XPATH, "/label[@id='message6']")

    MOBILE_NUMBER = (By.XPATH, "//input[@name='telephoneno']")
    MOBILE_NUMBER_MESSAGE = (By.XPATH, "/label[@id='message7']")

    EMAIL = (By.XPATH, "//input[@name='emailid']")
    EMAIL_MESSAGE = (By.XPATH, "/label[@id='message9']")

    PASSWORD_CUSTOMER = (By.XPATH, "//input[@name='password']")
    PASSWORD_CUSTOMER_MESSAGE = (By.XPATH, "/label[@id='message18']")

    SUBMIT_CUSTOM_BUTTON = (By.XPATH, "//input[@name='sub']")
    RESET_CUSTOM_BUTTON = (By.XPATH, "//input[@name='res']")


    MESSAGE_SUCCESSFUL_SHOW = (By.XPATH, "//p[@class='heading3']")

    CUSTOMER_ID_SHOW = (By.XPATH, "//tbody//tr[4]//td[2]")

    #
    #New acount locaters
    #
    NEW_ACCOUNT_TAG = (By.XPATH,"//a[@href='addAccount.php']")
    CUSTOMER_ID_FIELD = (By.XPATH,"// input[@name='cusid']")
    DEPOSIT_FEILD = (By.XPATH,"// input[@name='inideposit']")

    SUBMIT_ACCOUNT_BUTTON = (By.XPATH, "//input[@name='button2']")
    RESET_ACCOUNT_BUTTON = (By.XPATH, "//input[@name='reset']")
    ACC_ID_SHOW = (By.XPATH, "//tbody//tr[4]//td[2]")
    #
    # Deposite locaters
    #
    DEPOSIT_TAG = (By.XPATH,"//a[@href='DepositInput.php']")
    ACCOUNT_NO = (By.XPATH,"// input[@name='accountno']")
    AMOUNT_DEPOSITE = (By.XPATH,"//input[@name='ammount']")
    AMOUNT_DESCRIPTION = (By.XPATH,"//tr[8]//td[2]//input[@name='desc']")

    SUBMIT_DEPOSITE_BUTTON = (By.XPATH, "//input[@name='AccSubmit']")
    RESET_DEPOSITE_BUTTON = (By.XPATH, "//input[@name='res']")

    ACC_NUMBER_SHOW_AFTER_DEPOSITE = (By.XPATH, "//tbody//tr[7]//td[2]")