import allure

from tests.test_base import TestBase
from userinyerface.configurations.schemas import DataTest
from userinyerface.configurations.test_data_loader import DataLoader
from userinyerface.forms.main_form import MainForm
from userinyerface.forms.start_page import StartPage


class TestHelpForm(TestBase):

    def test_timer_start(self):
        with allure.step("Prepare test data and open main form"):
            main_form = self.open_main_form_from_start()
            test_data = self.prepare_test_data()

        with allure.step("Verify timer starts from expected time"):
            actual_timer = main_form.get_timer_started_from()
            expected_timer = test_data.timer_start

            assert actual_timer == expected_timer, (
                f"Expected timer {expected_timer} != {actual_timer}"
            )
