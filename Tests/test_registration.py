from selenium.common.exceptions import NoSuchElementException

from Pages.registration_page import RegistrationPage
from Base.base import Base
from Resources.test_data import RegistrationPageData
from Resources.locators import RegisterAccountLocators
import pytest

class TestRegistration(Base):

    def test_registration_empty_form_fail(self):
        driver = self.driver
        driver.get(RegistrationPageData.URL)
        register = RegistrationPage(driver)
        register.click_continue()
        current_url = driver.current_url

        if current_url != RegistrationPageData.URL:
            return False
        try:
            error_messages = register.get_list_of_elements(RegisterAccountLocators.TEXT_DANGER)
        except NoSuchElementException as e:
                return False
                raise
                print("Errors do not exist", format(e))


