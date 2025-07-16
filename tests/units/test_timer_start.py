from datetime import timedelta

import allure

from tests.test_base import TestBase


class TestHelpForm(TestBase):

    @pytest.mark.parametrize("expected_start", [timedelta(0)])
    def test_timer_start(self):
        with allure.step("Prepare test data and open main form"):
            main_form = self.open_main_form_from_start()
            test_data = self.prepare_test_data()

        with allure.step("Verify timer starts from expected time"):
            actual_timer = main_form.get_timer_started_from()
            expected_timer = timedelta(0)

            assert actual_timer == expected_timer, (
                f"Expected timer {expected_timer} != {actual_timer}"
            )
