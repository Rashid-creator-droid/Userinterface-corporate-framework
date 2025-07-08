import os
from pathlib import Path

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from userinterface.configurations.schemas import DataTest


class DataLoader:

    @staticmethod
    def get_test_data() -> DataTest:
        env_name = BrowserServices.Instance.service_provider.settings_file().get("environment")

        data_sub_path = Path("environment", env_name, "test_data.json")
        data_file = JsonSettingsFile(
            str(data_sub_path),
            RootPathHelper.current_root_path(__file__),
        )
        raw_data = data_file.setting_json
        test_data_fields = DataTest(**raw_data)
        return test_data_fields
