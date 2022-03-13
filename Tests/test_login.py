from Pages.login_page import LoginPage
from Base.base import Base
from Resources.test_data import LoginPageData
from Resources.locators import MyAccountLocators
import pytest


class TestLogin(Base):

    def test_login_fail(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(LoginPageData.EMAIL_FAIL, LoginPageData.PASSWORD_FAIL)

        try:
            assert login.get_error_msg() == "Warning: No match for E-Mail Address and/or Password."
        except Exception as e:
            raise
            print("Error is wrong", format(e))

    def test_user_login_fail(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(LoginPageData.EMAIL_FAIL, LoginPageData.PASSWORD_PASS)

        try:
            assert login.get_error_msg() == "Warning: No match for E-Mail Address and/or Password."
        except Exception as e:
            raise
            print("Error is wrong", format(e))

    def test_pass_login_fail(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(LoginPageData.EMAIL_PASS, LoginPageData.PASSWORD_FAIL)

        try:
            assert login.get_error_msg() == "Warning: No match for E-Mail Address and/or Password."
        except Exception as e:
            raise
            print("Error is wrong", format(e))

    def test_login_pass(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login(LoginPageData.EMAIL_PASS, LoginPageData.PASSWORD_PASS)
        my_account_content = login.get_text(MyAccountLocators.MY_ACCOUNT_HEADERS)
        exist = False
        if "My Account" in my_account_content:
            exist = True
        try:
            assert exist == True
        except Exception as e:
            raise
            print("User is not logged in", format(e))