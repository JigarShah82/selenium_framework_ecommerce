
from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    COUPON_TEXT_BOX = (By.ID, 'coupon_code')
    APPLY_COUPON_BUTTON = (By.NAME, 'apply_coupon')
    PROCEED_CHECKOUT = (By.CSS_SELECTOR, 'a.wc-forward')
    APPLIED_COUPON_ALERT = (By.CSS_SELECTOR, 'div.woocommerce-message')

