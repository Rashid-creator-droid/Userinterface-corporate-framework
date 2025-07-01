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


class CardOneForm(Form):

    def __init__(self):
        super().__init__(Locator.by_xpath("//*[@class='game view']"), "Card one form")

        self.terms_checkbox = self._form_element.find_child_element(
            CheckBox,
            Locator.by_xpath("//*[@class='checkbox__label']"),
            "Terms and Conditions checkbox"
        )

    @property
    def password_field(self) -> TextBox:
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath("//input[@placeholder='Choose Password']"),
            "Password field"
        )

    @property
    def email_field(self) -> TextBox:
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath("//input[@placeholder='Your email']"),
            "Email field"
        )

    @property
    def domain_field(self) -> TextBox:
        return self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath("//input[@placeholder='Domain']"),
            "Domain field"
        )

    @property
    def next_button(self) -> Button:
        return self._form_element.find_child_element(
            Button,
            Locator.by_xpath("//a[text()='Next']"),
            "Next button"
        )

    def select_domain_zone(self, zone_text: str):
        dropdown_opener = self._form_element.find_child_element(
            Button,
            Locator.by_xpath("//div[contains(@class, 'dropdown__opener')]"),
            "Dropdown opener"
        )
        dropdown_opener.click()
        option = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(f"//div[contains(@class,'dropdown__list-item') and text()='{zone_text}']"),
            f"Dropdown option {zone_text}"
        )
        option.click()