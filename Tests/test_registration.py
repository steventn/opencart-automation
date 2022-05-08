from selenium.common.exceptions import NoSuchElementException

from Pages.registration_page import RegistrationPage
from Base.base import Base
from Resources.test_data import RegistrationPageData
from Resources.locators import RegisterAccountLocators
import csv

class TestRegistration(Base):

    def save_acount_details(self, email, password):
        csv_header = ['Email', 'Password']
        csv_data = [email, password]
        csv_file = "account_info.csv"

        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_header)
                writer.writerow(csv_data)
        except IOError:
            print("I/O error")

    def test_invalid_empty_registration_form(self):
        driver = self.driver
        driver.get(RegistrationPageData.URL)
        register = RegistrationPage(driver)
        register.click_continue()
        current_url = driver.current_url

        if current_url != RegistrationPageData.REGISTRATION_URL:
            return False
        try:
            register.get_list_of_elements(RegisterAccountLocators.TEXT_DANGER)
        except NoSuchElementException as e:
                return False
                raise
                print("Errors do not exist", format(e))

#TODO create method to register, create method for CSV file creation and debug, debug unreachable code
    def test_valid_registration_form(self):
        driver = self.driver
        driver.get(RegistrationPageData.URL)
        register = RegistrationPage(driver)
        register.set_first_name(RegistrationPageData.FIRSTNAME)
        register.set_last_name(RegistrationPageData.LASTNAME)
        register.set_email(RegistrationPageData.EMAIL)
        register.set_telephone(RegistrationPageData.TELEPHONE)
        register.set_password(RegistrationPageData.PASSWORD)
        register.set_password_confirm(RegistrationPageData.PASSWORD_CONFIRM)
        register.set_subscribe("yes")
        register.set_privacy_policy("yes")
        register.click_continue()
        driver.implicitly_wait(30)
        current_url = driver.current_url
        print(current_url)
        print(RegistrationPageData.REGISTRATION_SUCCESS_URL)

        self.save_acount_details(RegistrationPageData.EMAIL, RegistrationPageData.PASSWORD)

        if str(current_url) != RegistrationPageData.REGISTRATION_SUCCESS_URL:
            return False

        try:
            print(register.get_text(RegisterAccountLocators.REGISTRATION_HEADER_SUCCESS))
            if register.get_text(RegisterAccountLocators.REGISTRATION_HEADER_SUCCESS) != RegistrationPageData.REGISTRATION_HEADER_SUCCESS_TEXT:
                return False
        except NoSuchElementException as e:
                return False
                raise
                print("Registration is not successful", format(e))





