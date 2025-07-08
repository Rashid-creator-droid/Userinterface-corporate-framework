from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class CardThreeForm(Form):
    _card_two_unique_xpath = "//*[@class='personal-details']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._card_two_unique_xpath), "Card three form")
