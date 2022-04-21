from selenium.common.exceptions import NoSuchElementException

from Pages.registration_page import RegistrationPage
from Base.base import Base
from Resources.test_data import RegistrationPageData
from Resources.locators import RegisterAccountLocators
import pytest

class TestRegistration(Base):

    def test_invalid_empty_registration_form(self):
        driver = self.driver
        driver.get(RegistrationPageData.URL)
        register = RegistrationPage(driver)
        register.click_continue()
        current_url = driver.current_url

        if current_url != RegistrationPageData.REGISTRATION_URL:
            return False
        try:
            error_messages = register.get_list_of_elements(RegisterAccountLocators.TEXT_DANGER)
        except NoSuchElementException as e:
                return False
                raise
                print("Errors do not exist", format(e))

    def test_valid_registration_form(self):
        driver = self.driver
        driver.get(RegistrationPageData.URL)
        register = RegistrationPage(driver)
        register.set_first_name(RegistrationPageData.FIRSTNAME)
        register.set_last_name(RegistrationPageData.LASTNAME)
        register.set_email(RegistrationPageData.EMAIL)
        register.set_password(RegistrationPageData.PASSWORD)
        register.set_password_confirm(RegistrationPageData.PASSWORD_CONFIRM)
        register.set_subscribe("yes")
        register.set_privacy_policy("yes")
        register.click_continue()
        current_url = driver.current_url

        if current_url != RegistrationPageData.REGRISTRATION_SUCCESS_URL:
            return False

        try:
            if RegistrationPageData.REGISTRATION_HEADER_SUCCESS != RegistrationPageData.REGISTRATION_HEADER_SUCCESS_TEXT
                return False
        except NoSuchElementException as e:
                return False
                raise
                print("Registration is not successful", format(e))



