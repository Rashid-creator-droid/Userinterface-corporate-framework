import random
import time

from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from pywinauto.application import Application
from pywinauto.findwindows import find_windows
from py_selenium_auto.browsers.browser_services import BrowserServices


class CardTwoForm(Form):
    _card_two_unique_xpath = "//*[@class='avatar-and-interests__form']"
    _unselect_all_xpath = "//*[@for='interest_unselectall']"
    _all_interests_xpath = "//*[starts-with(@for, 'interest_') and not(contains(@for, 'selectall'))]"
    _next_button_xpath = "//*[text()='Next']"
    _file_input_button_xpath = "//*[@class='avatar-and-interests__upload-button']"
    _file_input_xpath = "//*[@id='auto-upload-input']"
    _avatar_image_xpath = "//*[@class='avatar-and-interests__avatar-image']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._card_two_unique_xpath), "Card two form")

    def uncheck_unselect_all(self):
        unselect_all = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._unselect_all_xpath),
            "Unselect all checkbox"
        )
        unselect_all.click()

    def select_two_random_interests(self):
        all_interest_elements = self._form_element.find_child_elements(
            CheckBox,
            Locator.by_xpath(self._all_interests_xpath),
            "All interests checkboxes"
        )
        random_interests = random.sample(all_interest_elements, 3)
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

        app = Application(backend="win32").connect(title='Открытие', timeout=5)
        dialog = app.window(title='Открытие')
        dialog['Edit'].set_edit_text(file_path)
        dialog['Открыть'].wait('ready', timeout=5)
        dialog['Открыть'].click_input()
        dialog.wait_not('visible', timeout=5)

    def avatar_is_uploaded(self):

        if self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath(self._avatar_image_xpath),
            "Avatar image block"
        ):
            return True
        return False


