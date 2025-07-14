import os
from pathlib import Path

from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper


class AvatarLoader:

    @staticmethod
    def get_avatar_absolute_path(filename: str = "avatar.png") -> str:
        relative_path = Path(filename)
        absolute_path = os.path.abspath(
            os.path.join(RootPathHelper.current_root_path(__file__), str(relative_path))
        )
        return absolute_path
