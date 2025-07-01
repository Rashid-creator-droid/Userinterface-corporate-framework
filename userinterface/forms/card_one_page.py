import enum
from typing import List

from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class ContactUsTextField(enum.Enum):
    Password = "PROPERTY[NAME][0]"
    Email = "PROPERTY[8][0]"
    Domain = "PROPERTY[7][0]"
    Email = "PROPERTY[9][0]"
    Message = "PROPERTY[10][0]"


class CardOneForm(Form):

    def __init__(self):
        super().__init__(Locator.by_xpath("//*[@class='game view']"), "Card two form")


    def get_text_field(self, name: ContactUsTextField) -> TextBox:
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_name(name.value),
            f"TextBox: {name}"
        )