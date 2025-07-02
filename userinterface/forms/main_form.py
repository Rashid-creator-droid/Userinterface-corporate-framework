from enum import Enum
from typing import List

from py_selenium_auto.elements.button import Button
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class TypeOfTesting(Enum):
    Functional = "/functional_testing/"
    Automation = "/services/testing_automation/"
    Mobile = "/services/mobile_application_testing/"


class MainForm(Form):

    _main_form_unique_xpath = "//*[contains(@class, 'start') and contains(@class, 'view')]"
    _next_button_xpath = "//*[@class='start__link']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._main_form_unique_xpath), "Main form")

        self.next_page_button = self._element_factory.get_button(
            Locator.by_xpath(self._next_button_xpath),
            "Next page button"
        )
