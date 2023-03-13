
from selenium.webdriver.common.by import By


class HeaderPageLocators:

    SITE_HEADER_CART = (By.ID, 'site-header-cart')
    CART_PLACE_HOLDER = (By.CSS_SELECTOR, 'a.cart-contents span.count')
