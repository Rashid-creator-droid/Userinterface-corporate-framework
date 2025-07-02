import enum
from typing import List

from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class ContactUsTextField(enum.Enum):
    Password = "PROPERTY[NAME][0]"
    Email = "PROPERTY[8][0]"
    Domain = "PROPERTY[7][0]"


class CardTwoForm(Form):

    _card_two_unique_xpath = "//*[@class='avatar-and-interests__form']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._card_two_unique_xpath), "Card two form")
