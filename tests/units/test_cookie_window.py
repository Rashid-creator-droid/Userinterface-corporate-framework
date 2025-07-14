import allure

from tests.test_base import TestBase


class TestCookieWindow(TestBase):

    def test_cookie_window(self):
        with allure.step("Go to the main form"):
            main_form = self.open_main_form_from_start()

        with allure.step("Accept cookies and verify the banner is hidden"):
            main_form.accept_cookie_button_click()
            assert main_form.is_cookie_banner_closed(), "Cookie banner should be hidden"
