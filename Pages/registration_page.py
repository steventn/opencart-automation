from Resources.locators import MyAccountLocators
from Base.base import Base

class RegistrationPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.enter_text(MyAccountLocators.FIRST_NAME, first_name)

    def set_last_name(self, last_name):
        self.enter_text(MyAccountLocators.LAST_NAME, last_name)

    def set_email(self, email):
        self.enter_text(MyAccountLocators.EMAIL, email)

    def set_telephone(self, telephone):
        self.enter_text(MyAccountLocators.TELEPHONE, telephone)

    def set_password(self, password):
        self.enter_text(MyAccountLocators.PASSWORD, password)

    def set_password_confirm(self, password_confirm):
        self.enter_text(MyAccountLocators.PASSWORD_CONFIRM, password_confirm)

    def set_subscribe(self, choice):
        if choice.lower() == "yes":
            self.click(MyAccountLocators.SUBSCRIBE_YES)
        else:
            self.click(MyAccountLocators.SUBSCRIBE_NO)

    def set_privacy_policy(self, choice):
        if choice.lower() == "yes":
            if Base.check_selected_checkbox(MyAccountLocators.PRIVACY_CHECKBOX) == False:
                self.click(MyAccountLocators.PRIVACY_CHECKBOX)
        else:
            self.click(MyAccountLocators.PRIVACY_CHECKBOX)

    def click_continue(self):
        self.click(MyAccountLocators.CONTINUE_BUTTON)
