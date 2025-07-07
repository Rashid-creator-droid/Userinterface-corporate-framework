import random

from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class CardTwoForm(Form):
    _card_two_unique_xpath = "//*[@class='avatar-and-interests__form']"
    _unselect_all_xpath = "//*[@for='interest_unselectall']"
    _all_interests_xpath = "//*[starts-with(@for, 'interest_') and not(contains(@for, 'selectall'))]"
    _next_button_xpath = "//*[text()='Next']"
    _file_input_button_xpath = "//*[@class='avatar-and-interests__upload-button']"
    _file_input_xpath = "//*[@id='auto-upload-input']"

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
        random_interests = random.sample(all_interest_elements, 2)
        for interest in random_interests:
            if not interest.is_checked():
                interest.check()

    def upload_avatar_image(self, file_path: str):
        upload_button = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._file_input_button_xpath),
            "Upload avatar button"
        )

        upload_button.js_actions.execute_script("""
            const form = document.querySelector('.avatar-and-interests__form');
            if (!document.getElementById('auto-upload-input')) {
                const input = document.createElement('input');
                input.type = 'file';
                input.id = 'auto-upload-input';
                input.style.display = 'block';
                form.appendChild(input);
            }
        """)

        file_input = self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath(self._file_input_xpath),
            "Upload avatar input"
        )
        file_input.send_keys(file_path)

        upload_button.js_actions.execute_script("""
            const fileInput = document.getElementById('auto-upload-input');
            const file = fileInput.files[0];
            if (!file) {
                console.error('File not found');
                return;
            }

            const reader = new FileReader();
            reader.onload = function(event) {
                const dataUrl = event.target.result;
                const avatarBox = document.querySelector('.avatar-and-interests__avatar-box');
                if (avatarBox) {
                    avatarBox.innerHTML = '<img src="' + dataUrl + '" style="width: 100%; height: auto;">';
                }
                if (window.app && app.$children && app.$children[0].validation) {
            app.$children[0].validation.hasAvatar = true;
        }
            };
            reader.readAsDataURL(file);
        """)
