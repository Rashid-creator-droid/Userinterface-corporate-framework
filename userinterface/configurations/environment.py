from pathlib import Path

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class Environment:

    @staticmethod
    def current_environment():
        env_name = BrowserServices.Instance.service_provider.settings_file().get("environment")
        env_sub_path = str(Path("environment", env_name, "config.json"))
        return JsonSettingsFile(env_sub_path, RootPathHelper.current_root_path(__file__))
