from selenium.webdriver.common.by import By


class MyAccountSignedOutLocators:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')
    ERRORS = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    REG_USER_NAME = (By.ID, 'reg_email')
    REG_PASSWORD = (By.ID, 'reg_password')
    REG_BUTTON = (By.NAME, 'register')



