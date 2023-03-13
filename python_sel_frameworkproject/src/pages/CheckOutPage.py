
from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended
from python_sel_frameworkproject.src.pages.locators.CheckOutPageLocators import CheckOutPageLocators


class CheckOutPage(CheckOutPageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def billing_details(self, fname, lname, address, suburb, state, postcode, phone, email):
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME, fname)
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME, lname)
        self.sl.wait_and_input_text(self.BILLING_ADD_LINE1, address)
        self.sl.wait_and_input_text(self.BILLING_SUBURB, suburb)
        self.sl.wait_and_select_from_dropdown(self.BILLING_STATE, state)
        self.sl.wait_and_input_text(self.BILLING_POSTCODE, postcode)
        self.sl.wait_and_input_text(self.BILLING_PHONE, phone)
        self.sl.wait_and_input_text(self.BILLING_EMAIL, email)

    def place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)

