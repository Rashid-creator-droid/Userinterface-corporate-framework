import allure

from tests.test_base import TestBase
from userinterface.forms.main_form import MainForm
from userinterface.forms.start_page import StartPage


class TestHelpForm(TestBase):
    main_form = MainForm()
    start_page = StartPage()

    def setup_method(self):
        with allure.step("Open the start page"):
            self.go_to_start_page()

        with allure.step("Verify the start page is displayed"):
            assert self.start_page.state.is_displayed(), "The start page is not visible"

    def test_help_window(self):
        with allure.step("Navigate to the main form"):
            self.start_page.click_next_page_button()
            assert self.main_form.state.is_displayed(), "Main form is not visible"

        with allure.step("Close the help window and verify it is collapsed"):
            self.main_form.close_help_window()
            assert self.main_form.wait_until_help_form_fully_collapsed(), "The help window is not collapsed"
