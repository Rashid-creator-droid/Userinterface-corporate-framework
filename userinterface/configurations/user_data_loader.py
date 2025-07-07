from userinterface.configurations.schemas import UserFields
from pathlib import Path

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

class UserDataLoader:

    @staticmethod
    def get_user_data() -> UserFields:
        env_name = BrowserServices.Instance.service_provider.settings_file().get("environment")

        user_data_sub_path = str(Path("environment", env_name, "user_data.json"))
        user_data_file = JsonSettingsFile(
            str(user_data_sub_path),
            RootPathHelper.current_root_path(__file__),
        )
        raw_data = user_data_file.setting_json
        user_fields = UserFields(**raw_data)

        return user_fields