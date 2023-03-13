from selenium.webdriver.common.by import By


class MyAccountSignedInLocators:

    LOGOUT_LEFT_PANEL = (By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link--customer-logout')
    LOGGED_IN_CONTENT = (By.XPATH, '//div[@class="woocommerce-MyAccount-content"]')


