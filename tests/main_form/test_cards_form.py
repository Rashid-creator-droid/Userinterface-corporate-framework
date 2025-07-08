import allure

from tests.test_base import TestBase
from userinterface.configurations.schemas import UserFields, DataTest
from userinterface.configurations.test_data_loader import DataLoader
from userinterface.configurations.user_data_loader import UserDataLoader, AvatarLoader
from userinterface.forms.email_password_card import CardOneForm
from userinterface.forms.interests_avatar_card import CardTwoForm
from userinterface.forms.main_form import MainForm
from userinterface.forms.more_info_card import CardThreeForm
from userinterface.forms.start_page import StartPage


class TestCardsForm(TestBase):
    main_form = MainForm()
    card_one_form = CardOneForm()
    card_two_form = CardTwoForm()
    card_three_form = CardThreeForm()
    start_page = StartPage()

    def setup_method(self):
        with allure.step("Open the start page"):
            self.go_to_start_page()

        with allure.step("Verify the start page is displayed"):
            assert self.start_page.state.is_displayed(), "The start page is not visible"

        with allure.step("Load test and user data"):
            self.user_data: UserFields = UserDataLoader.get_user_data()
            self.test_data: DataTest = DataLoader.get_test_data()

    def test_card_form(self):
        with allure.step("Go to next page"):
            self.start_page.click_next_page_button()
            assert self.card_one_form.state.is_displayed(), "Main form page is not open"

        with allure.step("Filling out the registration form"):
            self.card_one_form.input_password_field(self.user_data.password)
            self.card_one_form.input_email_field(self.user_data.email)
            self.card_one_form.input_domain_field(self.user_data.domain)
            self.card_one_form.select_domain_zone(self.user_data.domain_zone)

            self.card_one_form.terms_checkbox_chek()

        with allure.step("Navigate to the Next page"):
            self.card_one_form.next_button_click()
            assert self.card_two_form.state.wait_for_displayed(), "Interest and avatar card is not open"

        with allure.step("Selecting interests for registration and uploading an avatar"):
            self.card_two_form.uncheck_unselect_all()
            self.card_two_form.select_two_random_interests(self.test_data.interest_selection_count)

            avatar_path = AvatarLoader.get_avatar_absolute_path()
            self.card_two_form.upload_avatar_image(avatar_path)
            assert self.card_two_form.avatar_is_uploaded(), "Avatar is not upload"

            self.card_one_form.next_button_click()
            assert self.card_three_form.state.is_displayed(), "More info card is not open"
