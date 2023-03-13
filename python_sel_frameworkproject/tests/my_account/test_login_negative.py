import pytest
from python_sel_frameworkproject.src.pages.MyAccountSignedOut import MyAccountSignedOut
import logging as logger


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_invalid_user(self):
        my_account = MyAccountSignedOut(self.driver)
        # goto my account
        my_account.go_to_my_account()

        # type username and password and click login
        my_account.input_login_username("alsjfa@abc.com")
        my_account.input_login_password("lasjdf")
        my_account.click_login_button()
        # verify error message
        expected_err = "Unknown email address. Check again or try your username."
        my_account.verify_error_message(expected_err)
