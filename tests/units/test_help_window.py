import allure

from tests.test_base import TestBase
from userinyerface.forms.main_form import MainForm
from userinyerface.forms.start_page import StartPage


class TestHelpForm(TestBase):

    def test_help_window(self):
        with allure.step("Go to the main form"):
            main_form = self.open_main_form_from_start()

        with allure.step("Close the help window and verify it is collapsed"):
            main_form.close_help_window()
            assert main_form.wait_until_help_form_fully_collapsed(), "The help window is not collapsed"
