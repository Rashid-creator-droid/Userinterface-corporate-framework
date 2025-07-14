import locale
import ctypes

import allure
from py_selenium_auto.browsers.browser_services import BrowserServices
from pywinauto.application import Application

from userinyerface.configurations.test_data_loader import DataLoader


class FileUploadDialogHandler:
    def __init__(self, backend='win32'):
        self.backend = backend
        self.timeout = BrowserServices.Instance.service_provider.timeout_configuration().condition

        test_data = DataLoader.get_test_data()
        self.current_lang = self.get_os_language()
        self.dialog_config = test_data.os_language.get(self.current_lang)


    @staticmethod
    def get_os_language(default="ru"):
        lang_id = ctypes.windll.kernel32.GetUserDefaultUILanguage()
        locale_name = locale.windows_locale.get(lang_id)
        if locale_name:
            return locale_name[:2].lower()
        return default

    def upload_file(self, file_path):
        with allure.step("Selecting an image in a windows window"):
            app = Application(backend=self.backend).connect(
                title=self.dialog_config.dialog_title,
                timeout=self.timeout
            )
            dialog = app.window(title=self.dialog_config.dialog_title)

            dialog[self.dialog_config.edit].set_edit_text(file_path)
            dialog[self.dialog_config.open_button].wait('ready', timeout=self.timeout)
            dialog[self.dialog_config.open_button].click_input()
            dialog.wait_not('visible', timeout=self.timeout)
