import time

import allure

from tests.test_base import TestBase
from userinterface.configurations.schemas import UserFields
from userinterface.configurations.user_data_loader import UserDataLoader, AvatarLoader
from userinterface.forms.card_one_form import CardOneForm
from userinterface.forms.card_two_form import CardTwoForm
from userinterface.forms.catd_three_form import CardThreeForm
from userinterface.forms.main_form import MainForm
from userinterface.forms.start_page import StartPage


class TestCardsForm(TestBase):
    main_form = MainForm()
    card_one_form = CardOneForm()
    card_two_form = CardTwoForm()
    card_three_form = CardThreeForm()
    start_page = StartPage()

    def setup_method(self):
        with allure.step("Go to start page"):
            self.go_to_start_page()

        with allure.step("Start page is displayed"):
            assert self.start_page.state.is_displayed(), "Start page is displayed"

        with allure.step("Load test data"):
            self.user_data: UserFields = UserDataLoader.get_user_data()

    def test_card_form(self):
        with allure.step("Go to next page"):
            self.start_page.click_next_page_button()
            assert self.card_one_form.state.is_displayed(), "Main form page is not open"

        with allure.step("Registration form"):
            self.card_one_form.input_password_field(self.user_data.password)
            self.card_one_form.input_email_field(self.user_data.email)
            self.card_one_form.input_domain_field(self.user_data.domain)
            self.card_one_form.select_domain_zone(self.user_data.domain_zone)

            self.card_one_form.terms_checkbox_chek()

        with allure.step("Go to Next"):
            self.card_one_form.next_button_click()
            assert self.card_two_form.state.wait_for_displayed(), "Two card is not open"

        with allure.step("Interests form and avatar"):
            self.card_two_form.uncheck_unselect_all()
            self.card_two_form.select_two_random_interests()

            avatar_path = AvatarLoader.get_avatar_absolute_path()
            self.card_two_form.upload_avatar_image(avatar_path)
            assert self.card_two_form.avatar_is_uploaded(), "Avatar is not upload"

            self.card_one_form.next_button_click()
            assert self.card_three_form.state.is_displayed(), "Three card is not open"
