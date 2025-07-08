import random

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator

from userinterface.utils.file_upload_utils import FileUploadDialogHandler


class InterestsAvatarForm(Form):
    _interests_avatar_form_unique_xpath = "//*[@class='avatar-and-interests__form']"
    _unselect_all_xpath = "//*[@for='interest_unselectall']"
    _all_interests_xpath = "//*[starts-with(@for, 'interest_') and not(contains(@for, 'selectall'))]"
    _next_button_xpath = "//*[text()='Next']"
    _file_input_button_xpath = "//*[@class='avatar-and-interests__upload-button']"
    _file_input_xpath = "//*[@id='auto-upload-input']"
    _avatar_image_xpath = "//*[@class='avatar-and-interests__avatar-image']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._interests_avatar_form_unique_xpath), "Card two form")

    def uncheck_unselect_all(self):
        unselect_all = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._unselect_all_xpath),
            "Unselect all checkbox"
        )
        unselect_all.click()

    def select_two_random_interests(self, selection_count):
        all_interest_elements = self._form_element.find_child_elements(
            CheckBox,
            Locator.by_xpath(self._all_interests_xpath),
            "All interests checkboxes"
        )
        random_interests = random.sample(all_interest_elements, selection_count)
        for interest in random_interests:
            if not interest.is_checked():
                interest.check()

    def upload_avatar_image(self, file_path):
        upload_button = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._file_input_button_xpath),
            "Upload avatar button"
        )
        upload_button.click()

        file_dialog = FileUploadDialogHandler()
        file_dialog.upload_file(file_path)

    def avatar_is_uploaded(self):
        return self._element_factory._element_finder.find_element(
            Locator.by_xpath(self._avatar_image_xpath),
            name="Avatar image",
            timeout=BrowserServices.Instance.service_provider.timeout_configuration().condition
        )
