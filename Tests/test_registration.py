from Pages.registration_page import RegistrationPage
from Base.base import Base
from Resources.test_data import RegistrationPageData
from Resources.locators import MyAccountLocators
import pytest


class TestRegistration(Base):

    def registration_empty_form_fail(self):
        driver = self.driver
        register = RegistrationPage(driver)

        try:
            assert register.get_error_msg() == ""
        except Exception as e:
            raise
            print("Error is wrong", format(e))

