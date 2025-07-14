from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class StartPage(Form):
    _start_page_unique_xpath = "//*[contains(@class, 'start') and contains(@class, 'view')]"
    _next_button_xpath = "//*[@class='start__link']"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._start_page_unique_xpath), "Start page")

    def click_next_page_button(self):
        self._element_factory.get_button(
            Locator.by_xpath(self._next_button_xpath),
            "Next page button"
        ).click()
