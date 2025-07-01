import allure

from userinterface.forms.main_form import MainForm, TypeOfTesting
from tests.test_base import TestBase


class TestMainForm(TestBase):
    main_form = MainForm()

    def setup(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_form.state.is_displayed()



    def test_main_page(self):
        with allure.step("Go to next page"):
            assert self.main_form.next_page_button.click()