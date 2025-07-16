import datetime

import allure

from tests.test_base import TestBase


class TestHelpForm(TestBase):

    def test_timer_start(self):
        with allure.step("Prepare test data and open main form"):
            main_form = self.open_main_form_from_start()

        with allure.step("Verify timer starts from expected time"):
            actual_timer = main_form.get_timer_started_from()
            expected_timer = datetime.time(0, 0, 0)

            assert actual_timer == expected_timer, (
                f"Expected timer {expected_timer} != {actual_timer}"
            )
