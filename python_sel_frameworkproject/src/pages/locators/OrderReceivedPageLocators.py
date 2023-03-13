
from selenium.webdriver.common.by import By


class OrderReceivedPageLocators:

    ORDER_RECEIVED_BANNER = (By.CSS_SELECTOR, 'h1.entry-title')
    ORDER_NO = (By.CSS_SELECTOR, 'li.order strong')
    ORDER_PAGE = (By.CSS_SELECTOR, 'div.woocommerce-order')


