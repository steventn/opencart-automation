from Resources.locators import LoginPageLocators
from Base.base import Base

class RegistrationPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL, email)