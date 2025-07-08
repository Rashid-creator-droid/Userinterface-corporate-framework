from pathlib import Path

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from userinterface.configurations.schemas import TestData


class TestDataLoader:

    @staticmethod
    def get_test_data() -> TestData:
        env_name = BrowserServices.Instance.service_provider.settings_file().get("environment")

        logic_data_sub_path = Path("environment", env_name, "test_data.json")
        logic_data_file = JsonSettingsFile(
            str(logic_data_sub_path),
            RootPathHelper.current_root_path(__file__),
        )
        raw_data = logic_data_file.setting_json
        return TestData(**raw_data)
