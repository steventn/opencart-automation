from Resources.locators import MyAccountLocators
from Base.base import Base

class MyAccountPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def check_link(self, path):
        return self.check_existence(path)
