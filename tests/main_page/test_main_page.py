import allure

from userinterface.configurations.user_data_loader import UserDataLoader
from userinterface.configurations.schemas import UserFields
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

        with allure.step("Load test data"):
            self.user_data: UserFields = UserDataLoader.get_user_data()

    def test_card_form(self):
        with allure.step("Go to next page"):
            self.main_form.next_page_button.click()
            assert self.card_one_form.state.is_displayed()

        with allure.step("Registration form"):
            self.card_one_form.password_field.clear()
            self.card_one_form.password_field.type(self.user_data.password)

            self.card_one_form.email_field.clear()
            self.card_one_form.email_field.type(self.user_data.email)

            self.card_one_form.domain_field.clear()
            self.card_one_form.domain_field.type(self.user_data.domain)

            self.card_one_form.select_domain_zone(self.user_data.domain_zone)

            self.card_one_form.terms_checkbox.check()

        with allure.step("Go to Next"):
            self.card_one_form.next_button.click()
            assert self.card_two_form.state.wait_for_displayed()

        with allure.step("Interests form and avatar"):
            self.card_two_form.uncheck_unselect_all()
            self.card_two_form.select_two_random_interests()


        with allure.step("Go to Next"):
            self.card_one_form.next_button.click()
            assert self.card_three_form.state.is_displayed()
