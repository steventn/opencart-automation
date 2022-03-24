from Resources.locators import LoginPageLocators
from Base.base import Base

class RegistrationPage(Base):

    def __init__(self, driver):
        self.driver = driver
