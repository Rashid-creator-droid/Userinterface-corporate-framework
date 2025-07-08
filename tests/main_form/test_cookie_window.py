import allure

from tests.test_base import TestBase
from userinterface.forms.main_form import MainForm
from userinterface.forms.start_page import StartPage


class TestCookieWindow(TestBase):
    main_form = MainForm()
    start_page = StartPage()

    def setup_method(self):
        with allure.step("Open the start page"):
            self.go_to_start_page()

        with allure.step("Verify the start page is displayed"):
            assert self.start_page.state.is_displayed(), "The start page is not visible"

    def test_cookie_window(self):
        with allure.step("Navigate to the main form"):
            self.start_page.click_next_page_button()
            assert self.main_form.state.is_displayed(), "Main form should be visible after navigating from start page"

        with allure.step("Accept cookies and verify the banner is hidden"):
            self.main_form.accept_cookie_button_click()
            assert self.main_form.is_cookie_banner_closed(), "Cookie banner not to be hidden"
