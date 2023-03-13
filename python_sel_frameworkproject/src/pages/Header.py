from python_sel_frameworkproject.src.pages.locators.HeaderPageLocators import HeaderPageLocators
from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended


class Header(HeaderPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_cart_is_updated(self, count):
        cart_text = str(count) + ' item'
        self.sl.wait_verify_element_contains_text(self.CART_PLACE_HOLDER, cart_text)

    def click_on_cart(self):
        self.sl.wait_and_click(self.SITE_HEADER_CART)

