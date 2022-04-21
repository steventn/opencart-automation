from selenium.webdriver.common.by import By


class HomePageLocators(object):
    REGISTER = (By.XPATH, '//a[normalize-space()="Register"]')
    LOGIN = (By.XPATH, '//a[normalize-space()="Login"]')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    SUBMIT = (By.CSS_SELECTOR, 'input[value="Login"]')
    NO_MATCH_ERROR = (By.CSS_SELECTOR, '.alert.alert-danger.alert-dismissible')


class MyAccountLocators(object):
    EDIT_ACC_INFO_LINK = (By.XPATH, '//a[normalize-space()="Edit your account information"]')
    MY_ACCOUNT_HEADERS = (By.ID, 'content')

class RegisterAccountLocators(object):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[value="Continue"]')
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    SUBSCRIBE_YES = (By.CSS_SELECTOR, '//label[normalize-space()="Yes"]')
    SUBSCRIBE_NO = (By.CSS_SELECTOR, 'input[value="0"]')
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, 'input[value="1"][name="agree"]')
    TEXT_DANGER = ((By.CLASS_NAME, "text-danger"))
    REGISTRATION_HEADER_SUCCESS = (By.CSS_SELECTOR, "div[id='content'] h1")

