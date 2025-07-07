import allure

from userinterface.forms.card_one_form import CardOneForm
from userinterface.forms.card_two_form import CardTwoForm
from userinterface.forms.catd_three_form import CardThreeForm
from userinterface.forms.main_form import MainForm
from tests.test_base import TestBase


class TestMainForm(TestBase):
    main_form = MainForm()
    card_one_form = CardOneForm()
    card_two_form = CardTwoForm()
    card_three_form = CardThreeForm()

    def setup_method(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_form.state.is_displayed()

    def test_help_window(self):
        with allure.step("Go to next page"):
            self.main_form.click_next_page_button()
            assert self.card_one_form.state.is_displayed()

        with allure.step("Close help winodw"):
            self.main_form.close_help_window()
            assert self.main_form.wait_until_help_form_fully_collapsed(), "Help form is not collapsed"