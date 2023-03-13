import pytest
from python_sel_frameworkproject.src.pages.MyAccountSignedOut import MyAccountSignedOut
from python_sel_frameworkproject.src.helpers.generic_helpers import generic_random_email_pwd
from python_sel_frameworkproject.src.pages.MyAccountSignedIn import MyAccountSignedIn


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):

        my_account_so = MyAccountSignedOut(self.driver)
        my_account_si = MyAccountSignedIn(self.driver)
        #goto my account
        my_account_so.go_to_my_account()

        #fill in email and password and hit register
        rand_email_pwd = generic_random_email_pwd()
        my_account_so.input_reg_username(rand_email_pwd["email"])
        my_account_so.input_reg_password(rand_email_pwd["password"])
        my_account_so.click_register_button()

        #verify user is registered
        my_account_si.verify_user_signed_in()
        my_account_si.take_screenshot(rand_email_pwd["email"])
        my_account_si.left_nav_sign_out()



