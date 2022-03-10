from selenium.webdriver.common.by import By

class HomePageLocators(object):
    REGISTER = (By.XPATH, '//a[normalize-space()="Register"]')
    LOGIN = (By.XPATH, '//a[normalize-space()="Login"]')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    SUBMIT = (By.CSS_SELECTOR, 'input[value="Login"]')
    NO_MATCH_ERROR = (By.CSS_SELECTOR, '.alert.alert-danger.alert-dismissible')
    NO_MATCH_ERROR_TEXT = "Warning: No match for E-Mail Address and/or Password."