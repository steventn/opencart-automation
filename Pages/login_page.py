from Resources.locators import LoginPageLocators
from Base.base import Base

class LoginPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL, email)

    def set_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD, password)

    def click_submit(self):
        self.click(LoginPageLocators.SUBMIT)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_submit()

    def get_error_msg(self):
        return self.get_text(LoginPageLocators.NO_MATCH_ERROR)



