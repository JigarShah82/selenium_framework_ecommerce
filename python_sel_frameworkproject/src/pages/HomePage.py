from python_sel_frameworkproject.src.pages.locators.HomePageLocators import HomePageLocators
from python_sel_frameworkproject.src.SeleniumExtended import SeleniumExtended
from python_sel_frameworkproject.src.helpers.config_helpers import get_base_url


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_homepage(self):
        url = get_base_url()
        self.driver.get(url)

    def add_item_to_cart(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BEANIE)









