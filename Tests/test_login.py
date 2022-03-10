from Pages.login_page import LoginPage
from Base.base import Base
import pytest

# @pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    def test_login_fail(self):
        driver = self.driver
        login = LoginPage(driver)
        login.login()

        try:
            assert login.error_msg() == "Warning: No match for E-Mail Address and/or Password."
        except Exception as e:
            raise
            print("Error is wrong", format(e))