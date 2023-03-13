from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException,\
                                    ElementClickInterceptedException, WebDriverException
from selenium.webdriver.support.ui import Select
import time


class SeleniumExtended:

    def __init__(self, driver):

        self.driver = driver
        self.default_timeout = 10

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException,
                WebDriverException):
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_verify_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            raise TimeoutException("Cannot verify element contains expected text")

    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"unable to find elements located by '{locator}',"\
                              f"after time out of {timeout}"
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)
        return elements

    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text
        return element_text

    def wait_and_select_from_dropdown(self, locator, option, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        Select(WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )).select_by_visible_text(option)

    def wait_and_take_screenshot(self, locator, filename, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).screenshot(f"C:\\Users\\jigar\\python_sel_frameworkproject\\python_sel_frameworkproject\\screenshots"
                     f"\\{filename}.png")
