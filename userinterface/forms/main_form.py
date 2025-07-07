from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator
from selenium.webdriver.support.wait import WebDriverWait


class MainForm(Form):

    _main_form_unique_xpath = "//*[contains(@class, 'start') and contains(@class, 'view')]"
    _next_button_xpath = "//*[@class='start__link']"
    _help_button_xpath = "//*[contains(@class, 'help-form__send')]"
    _help_form_container_xpath = "//*[@class='help-form__container']"
    _cookie_accept_xpath = "//*[contains(@class, 'button--transparent')]"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._main_form_unique_xpath), "Main form")


    def click_next_page_button(self):
        self._element_factory.get_button(
            Locator.by_xpath(self._next_button_xpath),
            "Next page button"
        ).click()


    def close_help_window(self):
        self._element_factory.get_button(
            Locator.by_xpath(self._help_button_xpath),
            "Close help button"
        ).click()


    def wait_until_help_form_fully_collapsed(self):
        help_form_container = self._element_factory.get_combo_box(
            Locator.by_xpath(self._help_form_container_xpath),
            "Help form container"
        )
        self._conditional_wait.wait_for_condition(
            lambda: help_form_container.js_actions.execute_script(
                """
                const height = parseFloat(window.getComputedStyle(arguments[0]).height);
                return height <= 50;
                """,
                help_form_container.get_element()
            ),
            BrowserServices.Instance.service_provider.timeout_configuration().script,
        )
        return True
