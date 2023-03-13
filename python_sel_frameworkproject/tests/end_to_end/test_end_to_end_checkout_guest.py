from python_sel_frameworkproject.src.pages.HomePage import HomePage
from python_sel_frameworkproject.src.pages.Header import Header
from python_sel_frameworkproject.src.pages.CartPage import CartPage
from python_sel_frameworkproject.src.configs.generic_configs import GenericConfigs
from python_sel_frameworkproject.src.pages.CheckOutPage import CheckOutPage
from python_sel_frameworkproject.src.pages.OrderReceivedPage import OrderReceivedPage
from python_sel_frameworkproject.src.helpers.generic_helpers import generic_random_email_pwd
from python_sel_frameworkproject.src.helpers.database_helpers import get_order_from_db_by_orderno
import pytest


@pytest.mark.usefixtures("init_driver")
class TestEndtoEndCheckoutGuest:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest(self):
        # go to homepage
        homepage = HomePage(self.driver)
        header = Header(self.driver)
        cartpage = CartPage(self.driver)
        checkout = CheckOutPage(self.driver)
        order_received = OrderReceivedPage(self.driver)

        homepage.go_to_homepage()
        cart_counter = 0

        # add 1 item to cart
        homepage.add_item_to_cart()
        cart_counter += 1

        # verify cart
        header.verify_cart_is_updated(cart_counter)

        # go to cart and verify number of items
        header.click_on_cart()
        products = cartpage.get_all_product_names_in_cart()
        assert len(products) == 1, f"Expected 1 itme in cart but found {len(products)}"

        # apply coupon and verify
        cartpage.fill_coupon_and_click_apply(GenericConfigs.FREE_COUPON)
        applied_coupon_alert_text = cartpage.verify_coupon_is_applied()
        assert applied_coupon_alert_text == GenericConfigs.APPLIED_COUPON_ALERT, f"Incorrect Alert " \
                                                                                 f"Correct Alert Message is {GenericConfigs.APPLIED_COUPON_ALERT}"

        # proceed to checkout
        cartpage.proceed_to_checkout()

        # enter billing details
        rand_email = generic_random_email_pwd()
        checkout.billing_details(GenericConfigs.TEST_FNAME, GenericConfigs.TEST_LNAME,
                                 GenericConfigs.TEST_ADD, GenericConfigs.TEST_SUBURB,
                                 GenericConfigs.TEST_STATE, GenericConfigs.TEST_POSTCODE,
                                 GenericConfigs.TEST_PHONE, rand_email["email"])
        # place order
        checkout.place_order()

        # verify order received and take screenshot
        order_received.get_order_received_banner_text(GenericConfigs.ORDER_RECEIVED_BANNER_TEXT)
        order_received.order_received_screenshot(rand_email["email"])

        # verify order is recorded in db(via SQL or via API)
        order_no = order_received.get_order_number()
        print(f"Order is RECEIVED with the order number {order_no}")

        db_order = get_order_from_db_by_orderno(order_no)
        assert db_order, f"Front end order, not found in DB." \
                         f" ORDER NO : {order_no}"

        print(db_order)

