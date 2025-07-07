import allure

from tests.test_base import TestBase
from userinterface.forms.main_form import MainForm
from userinterface.forms.start_page import StartPage


class TestCookieWindow(TestBase):
    main_form = MainForm()
    start_page = StartPage()

    def setup_method(self):
        with allure.step("Go to start page"):
            self.go_to_start_page()

        with allure.step("Start page is displayed"):
            assert self.start_page.state.is_displayed(), "Start page is not displayed"

    def test_cookie_window(self):
        with allure.step("Go to next page"):
            self.start_page.click_next_page_button(), "Main form page is not open"
            assert self.main_form.state.is_displayed()

        with allure.step("Accept cookie"):
            self.main_form.accept_cookie_button_click()
            assert self.main_form.is_cookie_banner_closed(), "Cookie banner is not closed"
