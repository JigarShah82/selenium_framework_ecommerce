
from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended
from python_sel_frameworkproject.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def get_all_product_names_in_cart(self):
        product_names_element = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_names_element]
        return product_names

    def fill_coupon_and_click_apply(self,coupon_code):
        self.sl.wait_and_input_text(self.COUPON_TEXT_BOX, coupon_code)
        self.sl.wait_and_click(self.APPLY_COUPON_BUTTON)

    def verify_coupon_is_applied(self):
        alert_text = self.sl.wait_and_get_text(self.APPLIED_COUPON_ALERT)
        return alert_text

    def proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_CHECKOUT)



