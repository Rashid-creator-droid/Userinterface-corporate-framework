import os
from pathlib import Path

from py_selenium_auto.browsers.browser_services import BrowserServices
from py_selenium_auto_core.utilities.json_settings_file import JsonSettingsFile
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from userinterface.configurations.schemas import UserFields


class UserDataLoader:

    @staticmethod
    def get_user_data() -> UserFields:
        env_name = BrowserServices.Instance.service_provider.settings_file().get("environment")

        user_data_sub_path = Path("environment", env_name, "user_data.json")
        user_data_file = JsonSettingsFile(
            str(user_data_sub_path),
            RootPathHelper.current_root_path(__file__),
        )
        raw_data = user_data_file.setting_json
        user_fields = UserFields(**raw_data)

        return user_fields


class AvatarLoader:

    @staticmethod
    def get_avatar_absolute_path(filename: str = "avatar.png") -> str:
        relative_path = str(Path("resources", filename))
        absolute_path = os.path.abspath(
            os.path.join(RootPathHelper.current_root_path(__file__), relative_path)
        )
        return absolute_path
