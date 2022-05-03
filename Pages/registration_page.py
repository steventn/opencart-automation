from selenium.webdriver.support.wait import WebDriverWait

from Resources.locators import RegisterAccountLocators
from Base.base import Base

class RegistrationPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.enter_text(RegisterAccountLocators.FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.enter_text(RegisterAccountLocators.LAST_NAME, last_name)

    def set_email(self, email):
        self.enter_text(RegisterAccountLocators.EMAIL, email)

    def set_telephone(self, telephone):
        self.enter_text(RegisterAccountLocators.TELEPHONE, telephone)

    def set_password(self, password):
        self.enter_text(RegisterAccountLocators.PASSWORD, password)

    def set_password_confirm(self, password_confirm):
        self.enter_text(RegisterAccountLocators.PASSWORD_CONFIRM, password_confirm)

    def set_subscribe(self, choice):
        if choice.lower() == "yes":
            self.click(RegisterAccountLocators.SUBSCRIBE_YES)
        else:
            self.click(RegisterAccountLocators.SUBSCRIBE_NO)

    def set_privacy_policy(self, choice):
        if choice.lower() == "yes":
            self.click(RegisterAccountLocators.PRIVACY_CHECKBOX)

    def click_continue(self):
        self.click(RegisterAccountLocators.CONTINUE_BUTTON)
