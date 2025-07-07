import allure

from tests.test_base import TestBase
from userinterface.forms.main_form import MainForm
from userinterface.forms.start_page import StartPage


class TestHelpForm(TestBase):
    main_form = MainForm()
    start_page = StartPage()

    def setup_method(self):
        with allure.step("Go to start page"):
            self.go_to_start_page()

        with allure.step("Start page is displayed"):
            assert self.start_page.state.is_displayed(), "Start page is not displayed"

    def test_help_window(self):
        with allure.step("Go to next page"):
            self.start_page.click_next_page_button()
            assert self.main_form.state.is_displayed(), "Main form page is not open"

        with allure.step("Close help winodw"):
            self.main_form.close_help_window()
            assert self.main_form.wait_until_help_form_fully_collapsed(), "Help form is not collapsed"
