import time

import allure

from userinterface.forms.card_one_page import CardOneForm, ContactUsTextField
from userinterface.forms.main_form import MainForm, TypeOfTesting
from tests.test_base import TestBase


class TestMainForm(TestBase):
    main_form = MainForm()
    card_two_form = CardOneForm()

    def setup_method(self):
        with allure.step("Go to main page"):
            self.go_to_start_page()

        with allure.step("Main page is displayed"):
            assert self.main_form.state.is_displayed()


    def test_catd_two_form(self):
        with allure.step("Go to next page"):
            self.main_form.next_page_button.click()
            assert self.card_two_form.state.is_displayed()

        with allure.step("Form"):
            self.card_two_form.password_field.clear()
            self.card_two_form.password_field.type("MySecureP@ss123")

            self.card_two_form.email_field.clear()
            self.card_two_form.email_field.type("test@email.com")

            self.card_two_form.domain_field.clear()
            self.card_two_form.domain_field.type("example")

            self.card_two_form.select_domain_zone(".com")

            self.card_two_form.terms_checkbox.check()

        with allure.step("Go to Next"):
            self.card_two_form.next_button.click()
            time.sleep(5)