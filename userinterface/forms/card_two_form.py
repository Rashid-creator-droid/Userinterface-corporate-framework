import random

from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.elements.button import Button


class CardTwoForm(Form):

    _card_two_unique_xpath = "//*[@class='avatar-and-interests__form']"
    _unselect_all_xpath = "//*[@for='interest_unselectall']"
    _all_interests_xpath = "//*[starts-with(@for, 'interest_') and not(contains(@for, 'selectall'))]"
    _next_button_xpath = "//*[text()='Next']"
    _file_input_xpath = "//*[@class='avatar-and-interests__upload-button']"

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

    @property
    def next_button(self) -> Button:
        return self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._next_button_xpath),
            "Next button"
        )
