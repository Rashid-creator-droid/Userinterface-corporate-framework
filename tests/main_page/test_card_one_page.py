# import time
#
# import allure
#
# from userinterface.forms.card_one_page import CardOneForm
# from userinterface.forms.main_form import MainForm, TypeOfTesting
# from tests.test_base import TestBase
#
#
# class TestMainForm(TestBase):
#     main_form = MainForm()
#     card_two_form = CardOneForm()
#
#     def setup_method(self):
#         with allure.step("Go to main page"):
#             self.go_to_start_page()
#
#         with allure.step("Main page is displayed"):
#             assert self.main_form.state.is_displayed()
#
#
#     def test_catd_two_form(self):
#         with allure.step("Go to next page"):
#             self.main_form.next_page_button.click()
#             assert self.card_two_form.state.is_displayed()
#
#
#     def test_registration_form(self):
#         with allure.step("Send: Password, Email and accept Terms"):
#             self.card_two_form.terms_checkbox.check()
#             # self.card_two_form.next_button.click()
#             time.sleep(5)