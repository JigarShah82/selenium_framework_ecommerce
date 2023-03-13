from selenium.webdriver.common.by import By


class CheckOutPageLocators:

    BILLING_FIRST_NAME = (By.ID, 'billing_first_name')
    BILLING_LAST_NAME = (By.ID, 'billing_last_name')
    BILLING_ADD_LINE1 = (By.ID, 'billing_address_1')
    BILLING_SUBURB = (By.ID, 'billing_city')
    BILLING_STATE = (By.ID, 'billing_state')
    BILLING_POSTCODE = (By.ID, 'billing_postcode')
    BILLING_PHONE = (By.ID, 'billing_phone')
    BILLING_EMAIL = (By.ID, 'billing_email')
    PLACE_ORDER_BTN = (By.ID, 'place_order')


