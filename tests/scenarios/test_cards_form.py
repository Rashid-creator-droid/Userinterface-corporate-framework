import allure

from tests.test_base import TestBase
from userinyerface.configurations.user_data_loader import AvatarLoader
from userinyerface.forms.email_password_card import EmailPasswordForm
from userinyerface.forms.interests_avatar_card import InterestsAvatarForm
from userinyerface.forms.more_info_card import MoreInfoForm
from userinyerface.utils.faker_factory import FakeUserFactory


class TestCardsForm(TestBase):

    def test_card_form(self):
        with allure.step("Start registration and load data"):
            test_data = self.prepare_test_data()
            user_data = FakeUserFactory.create()
            self.open_main_form_from_start()
            email_form = EmailPasswordForm()

        with allure.step("Filling out the registration form"):
            email_form.input_password_field(user_data.password)
            email_form.input_email_field(user_data.email)
            email_form.input_domain_field(user_data.domain)
            email_form.select_domain_zone(user_data.domain_zone)
            email_form.terms_checkbox_chek()

        with allure.step("Navigate to the Interests and Avatar card"):
            email_form.next_button_click()
            interests_avatar_form = InterestsAvatarForm()
            assert interests_avatar_form.state.wait_for_displayed(), "Interest and avatar card is not open"

        with allure.step("Select interests and upload avatar"):
            interests_avatar_form.uncheck_unselect_all()
            interests_avatar_form.select_two_random_interests(test_data.interest_selection_count)

            avatar_path = AvatarLoader.get_avatar_absolute_path()
            interests_avatar_form.upload_avatar_image(avatar_path)
            assert interests_avatar_form.avatar_is_uploaded(), "Avatar is not uploaded"

        with allure.step("Go to more info card"):
            email_form.next_button_click()
            more_info_form = MoreInfoForm()
            assert more_info_form.state.is_displayed(), "More info card is not open"
