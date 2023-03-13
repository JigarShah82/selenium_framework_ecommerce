from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended
from python_sel_frameworkproject.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators


class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LOGOUT_LEFT_PANEL)

    def left_nav_sign_out(self):
        self.sl.wait_and_click(self.LOGOUT_LEFT_PANEL)

    def take_screenshot(self, filename):
        self.sl.wait_and_take_screenshot(self.LOGGED_IN_CONTENT, filename)

