from py_selenium_auto.browsers.browser_services import BrowserServices

from userinterface.configurations.configuration import Configuration


class TestBase:

    @staticmethod
    def go_to_start_page():
        BrowserServices.Instance.browser.go_to(Configuration.start_url())
        BrowserServices.Instance.browser.wait_for_page_to_load()