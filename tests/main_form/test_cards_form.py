import allure

from tests.test_base import TestBase
from userinterface.configurations.schemas import UserFields, DataTest
from userinterface.configurations.test_data_loader import DataLoader
from userinterface.configurations.user_data_loader import UserDataLoader, AvatarLoader
from userinterface.forms.email_password_card import EmailPasswordForm
from userinterface.forms.interests_avatar_card import InterestsAvatarForm
from userinterface.forms.main_form import MainForm
from userinterface.forms.more_info_card import MoreInfoForm
from userinterface.forms.start_page import StartPage


class TestCardsForm(TestBase):
    main_form = MainForm()
    email_password_form = EmailPasswordForm()
    avatar_interests_form = InterestsAvatarForm()
    more_info_form = MoreInfoForm()
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
            assert self.email_password_form.state.is_displayed(), "Main form page is not open"

        with allure.step("Filling out the registration form"):
            self.email_password_form.input_password_field(self.user_data.password)
            self.email_password_form.input_email_field(self.user_data.email)
            self.email_password_form.input_domain_field(self.user_data.domain)
            self.email_password_form.select_domain_zone(self.user_data.domain_zone)

            self.email_password_form.terms_checkbox_chek()

        with allure.step("Navigate to the Next page"):
            self.email_password_form.next_button_click()
            assert self.avatar_interests_form.state.wait_for_displayed(), "Interest and avatar card is not open"

        with allure.step("Selecting interests for registration and uploading an avatar"):
            self.avatar_interests_form.uncheck_unselect_all()
            self.avatar_interests_form.select_two_random_interests(self.test_data.interest_selection_count)

            avatar_path = AvatarLoader.get_avatar_absolute_path()
            self.avatar_interests_form.upload_avatar_image(avatar_path)
            assert self.avatar_interests_form.avatar_is_uploaded(), "Avatar is not upload"

            self.email_password_form.next_button_click()
            assert self.more_info_form.state.is_displayed(), "More info card is not open"
