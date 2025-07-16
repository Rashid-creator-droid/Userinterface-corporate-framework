from py_selenium_auto.elements.button import Button
from py_selenium_auto.elements.check_box import CheckBox
from py_selenium_auto.elements.text_box import TextBox
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class EmailPasswordForm(Form):
    _email_pass_form_unique_xpath = "//*[@class='game view']"
    _terms_checkbox_xpath = "//*[@class='checkbox__label']"
    _email_box_xpath = "//input[@placeholder='Your email']"
    _password_box_xpath = "//input[@placeholder='Choose Password']"
    _domain_box_xpath = "//input[@placeholder='Domain']"
    _next_button_xpath = "//*[text()='Next']"
    _dropdown_opener_xpath = "//*[contains(@class, 'dropdown__opener')]"
    _dropdown_list_xpath = "//*[@class='dropdown__list-item']"
    _dropdown_options_xpath = "//*[contains(@class,'dropdown__list-item') and text()='{zone_text}']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._email_pass_form_unique_xpath), "Email password card")

    def terms_checkbox_chek(self):
        terms_checkbox = self._form_element.find_child_element(
            CheckBox,
            Locator.by_xpath(self._terms_checkbox_xpath),
            "Terms and Conditions checkbox"
        )
        terms_checkbox.check()

    def input_password_field(self, text):
        password_field = self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath(self._password_box_xpath),
            "Password field"
        )
        password_field.clear()
        password_field.send_keys(text)

    def input_email_field(self, text):
        email_field = self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath(self._email_box_xpath),
            "Email field"
        )
        email_field.clear()
        email_field.send_keys(text)

    def input_domain_field(self, text):
        domain_field = self._form_element.find_child_element(
            TextBox,
            Locator.by_xpath(self._domain_box_xpath),
            "Domain field"
        )
        domain_field.clear()
        domain_field.send_keys(text)

    def next_button_click(self):
        self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._next_button_xpath),
            "Next button"
        ).click()

    def open_dropdown(self):
        dropdown_opener = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._dropdown_opener_xpath),
            "Dropdown opener"
        )
        dropdown_opener.click()

    def select_domain_zone(self, zone_text: str):
        option = self._form_element.find_child_element(
            Button,
            Locator.by_xpath(self._dropdown_options_xpath.format(zone_text=zone_text)),
            f"Dropdown option {zone_text}"
        )
        option.click()

    def get_domain_zone_list(self):
        domains = self._form_element.find_child_elements(
            TextBox,
            Locator.by_xpath(self._dropdown_list_xpath),
            "Domains list"
        )
        return [element.get_text() for element in domains]