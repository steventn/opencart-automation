from selenium.webdriver.support.wait import WebDriverWait

from Resources.locators import MyStoreLocators
from Base.base import Base

class ShoppingCartPage(Base):

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.click(MyStoreLocators.HOME_PAGE)

    def add_to_cart(self, item):
        featured_add_to_cart: {
            'macbook': MyStoreLocators.MACBOOK_ADD_TO_CART,
            'iphone': MyStoreLocators.IPHONE_ADD_TO_CART,
            'apple_cinema': MyStoreLocators.APPLE_CINEMA_ADD_TO_CART,
            'cannon': MyStoreLocators.CANNON_ADD_TO_CART
        }

        self.click(featured_add_to_cart[item])

    def 






    
