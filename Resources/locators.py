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