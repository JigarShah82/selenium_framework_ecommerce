from python_sel_frameworkproject.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended
from python_sel_frameworkproject.src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(MyAccountSignedOutLocators):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def verify_error_message(self, exp_err):
        self.sl.wait_verify_element_contains_text(self.ERRORS, exp_err)

    def input_reg_username(self, rusername):
        self.sl.wait_and_input_text(self.REG_USER_NAME, rusername)

    def input_reg_password(self, rpassword):
        self.sl.wait_and_input_text(self.REG_PASSWORD, rpassword)

    def click_register_button(self):
        self.sl.wait_and_click(self.REG_BUTTON)


