import allure

from tests.test_base import TestBase
from userinterface.configurations.test_data_loader import TestDataLoader
from userinterface.forms.main_form import MainForm
from userinterface.forms.start_page import StartPage


class TestHelpForm(TestBase):
    main_form = MainForm()
    start_page = StartPage()
    test_data = TestDataLoader.get_test_data()

    def setup_method(self):
        with allure.step("Go to start page"):
            self.go_to_start_page()

        with allure.step("Verify the start page is displayed"):
            assert self.start_page.state.is_displayed(), "Start page is not visible"

    def test_timer_start(self):
        with allure.step("Navigate to main form"):
            self.start_page.click_next_page_button()
            assert self.main_form.state.is_displayed(), "Main form page is not open"

        with allure.step("Verify timer starts from expected time"):
            actual_timer = self.main_form.get_timer_started_from()
            expected_timer = self.test_data.timer_start

            assert actual_timer == expected_timer, (
                f"Expected timer {expected_timer} != {actual_timer}"
            )
