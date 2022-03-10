from Locators.locators import LoginPageLocators
from Base.base import Base

class LoginPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def set_email(self):
        self.enter_text(LoginPageLocators.EMAIL, "test123@email.com")

    def set_password(self):
        self.enter_text(LoginPageLocators.PASSWORD, "pass")

    def click_submit(self):
        self.click(LoginPageLocators.SUBMIT)

    def login(self):
        self.set_email()
        self.set_password()
        self.click_submit()

    def error_msg(self):
        return self.get_text(LoginPageLocators.NO_MATCH_ERROR)



