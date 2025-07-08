import datetime

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto.forms.form import Form
from py_selenium_auto_core.locator.locator import Locator


class MainForm(Form):
    _main_form_unique_xpath = "//*[@class='game view']"
    _next_button_xpath = "//*[@class='start__link']"
    _help_button_xpath = "//*[contains(@class, 'help-form__send')]"
    _help_form_container_xpath = "//*[@class='help-form__container']"
    _cookie_button_accept_xpath = "//*[contains(@class, 'button--transparent')]"
    _cookie_xpath = "//*[contains(@class, 'cookies')]"
    _timer_xpath = "//*[contains(@class, 'timer')]"

    def __init__(self):
        super().__init__(Locator.by_xpath(self._main_form_unique_xpath), "Main form")

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
                return height <= 10;
                """,
                help_form_container.get_element()
            ),
            BrowserServices.Instance.service_provider.timeout_configuration().script,
        )
        return True

    def accept_cookie_button_click(self):
        self._element_factory.get_button(
            Locator.by_xpath(self._cookie_button_accept_xpath),
            "Accept cookie button"
        ).click()

    def is_cookie_banner_closed(self):
        return self._element_factory._element_finder.find_element(
            Locator.by_xpath(self._cookie_xpath),
            name="Cookie window",
            timeout=BrowserServices.Instance.service_provider.timeout_configuration().condition
        )

    def get_timer_started_from(self):
        timer_label = self._element_factory.get_label(
            Locator.by_xpath(self._timer_xpath), "Timer"
        )

        timer_text = timer_label.get_text().strip()
        actual_time = datetime.datetime.strptime(timer_text, "%H:%M:%S").time()
        return actual_time
