from selenium.webdriver.common.by import By


class HomePageLocators(object):
    REGISTER = (By.XPATH, '//a[normalize-space()="Register"]')
    LOGIN = (By.XPATH, '//a[normalize-space()="Login"]')

class LoginPageLocators(object):
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    SUBMIT = (By.CSS_SELECTOR, 'input[value="Login"]')
    NO_MATCH_ERROR = (By.CSS_SELECTOR, '.alert.alert-danger.alert-dismissible')

class MyAccountLocators(object):
    EDIT_ACC_INFO_LINK = (By.XPATH, '//a[normalize-space()="Edit your account information"]')
    MY_ACCOUNT_HEADERS = (By.ID, 'content')

class RegisterAccountLocators(object):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[value="Continue"]')
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    SUBSCRIBE_YES = (By.CSS_SELECTOR, 'input[value="1"][name="newsletter"]')
    SUBSCRIBE_NO = (By.CSS_SELECTOR, 'input[value="0"]')
    PRIVACY_CHECKBOX = (By.CSS_SELECTOR, 'input[value="1"][name="agree"]')
    TEXT_DANGER = ((By.CLASS_NAME, "text-danger"))
    REGISTRATION_HEADER_SUCCESS = (By.CSS_SELECTOR, "div[id='content'] h1")

class MyStoreLocators(object):
    DESKTOP_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=20"]')
    LAPTOPS_AND_NOTEBOOKS_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=18"]')
    COMPONENTS_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=25"]')
    TABLETS_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=57"]')
    SOFTWARE_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=17"]')
    PHONES_AND_PDAS_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=24"]')
    CAMERAS_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=33"]')
    MP3_PLAYERS_DROPDOWN = (By.CSS_SELECTOR, '.dropdown-toggle[href="https://demo.opencart.com/index.php?route=product/category&path=34"]')
    HOME_PAGE = (By.CSS_SELECTOR, 'a[href="https://demo.opencart.com/index.php?route=common/home"]')
    MACBOOK_ADD_TO_CART = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
    MACBOOK_ADD_TO_WISHLIST = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)')
    MACBOOK_COMPARE = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)')
    IPHONE_ADD_TO_CART = (By.CSS_SELECTOR, '//body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/button[1]')
    IPHONE_ADD_TO_WISHLIST = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)')
    IPHONE_COMPARE = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)')
    APPLE_CINEMA_ADD_TO_CART = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
    APPLE_CINEMA_ADD_TO_WISHLIST = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)')
    APPLE_CINEMA_COMPARE = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)')
    CANNON_ADD_TO_CART = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)')
    CANNON_ADD_TO_WISHLIST = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > button:nth-child(2)')
    CANNON_COMPARE = (By.CSS_SELECTOR, 'body > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > button:nth-child(3)')

    SEARCH_BAR = (By.CSS_SELECTOR, 'input[placeholder="Search"]')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    CURRENT_DROPDOWN_MENU = (By.CSS_SELECTOR, 'ul[class="dropdown-menu"]')
    SHOPPING_CART = (By.CSS_SELECTOR, '.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle')