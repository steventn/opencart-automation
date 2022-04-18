import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://demo.opencart.com/index.php?route=account/login")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return web_element.text

    def check_selected_checkbox(self, by_locator):
        return self.driver.find_element(by_locator).is_selected()

    # def check_text(self, by_locator, text):
    #     text_content = self.get_text(by_locator)
    #     if text in text_content:
    #         return True