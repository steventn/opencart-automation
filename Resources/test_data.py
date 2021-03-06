import random

class LoginPageData(object):
    NO_MATCH_ERROR_TEXT = "Warning: No match for E-Mail Address and/or Password."
    EMAIL_PASS = "stevenautomationproj@gmail.com"
    PASSWORD_PASS = "12345"
    EMAIL_FAIL = "test@gmail.com"
    PASSWORD_FAIL = "password"


def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    return '{}-{}-{}'.format(first, second, last)

class RegistrationPageData(object):
    FIRSTNAME = "Test"
    LASTNAME = "User"
    EMAIL = "stevenautomationproj" + str(random.randint(1, 1000)) + "@gmail.com"
    TELEPHONE = random_phone_num_generator()
    REGISTRATION_URL = "https://demo.opencart.com/index.php?route=account/register"
    PASSWORD = "12345"
    PASSWORD_CONFIRM = "12345"
    REGISTRATION_SUCCESS_URL = "https://demo.opencart.com/index.php?route=account/success"
    REGISTRATION_HEADER_SUCCESS_TEXT = "Your Account Has Been Created!"
    URL = "https://demo.opencart.com/index.php?route=account/register"






