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

    def add_to_wishlist(self, item):
        featured_add_to_wishlist: {
            'macbook': MyStoreLocators.MACBOOK_ADD_TO_WISHLIST,
            'iphone': MyStoreLocators.IPHONE_ADD_TO_WISHLIST,
            'apple_cinema': MyStoreLocators.APPLE_CINEMA_ADD_TO_WISHLIST,
            'cannon': MyStoreLocators.CANNON_ADD_TO_WISHLIST
        }

        self.click(featured_add_to_wishlist[item])

    def add_to_compare(self, item):
        featured_add_to_compare: {
            'macbook': MyStoreLocators.MACBOOK_COMPARE,
            'iphone': MyStoreLocators.IPHONE_COMPARE,
            'apple_cinema': MyStoreLocators.APPLE_CINEMA_COMPARE,
            'cannon': MyStoreLocators.CANNON_COMPARE
        }

        self.click(featured_add_to_compare[item])






    
