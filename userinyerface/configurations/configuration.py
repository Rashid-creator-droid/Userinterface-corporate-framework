from py_selenium_auto.browsers.browser_services import BrowserServices


class Configuration:

    @classmethod
    def start_url(cls):
        settings = BrowserServices.Instance.service_provider.settings_file()
        return settings.get("startUrl")