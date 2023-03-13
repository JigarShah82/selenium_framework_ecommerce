
from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended
from python_sel_frameworkproject.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators


class OrderReceivedPage(OrderReceivedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_order_received_banner_text(self, text):
        self.sl.wait_verify_element_contains_text(self.ORDER_RECEIVED_BANNER, text)

    def order_received_screenshot(self, filename):
        self.sl.wait_and_take_screenshot(self.ORDER_PAGE, filename)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NO)




