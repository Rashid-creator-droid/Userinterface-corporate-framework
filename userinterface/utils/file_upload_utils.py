from py_selenium_auto.browsers.browser_services import BrowserServices
from pywinauto.application import Application


class FileUploadDialogHandler:
    def __init__(self, dialog_title='Открытие', backend='win32'):
        self.dialog_title = dialog_title
        self.backend = backend
        self.timeout = BrowserServices.Instance.service_provider.timeout_configuration().condition

    def upload_file(self, file_path):
        app = Application(backend=self.backend).connect(title=self.dialog_title, timeout=self.timeout)
        dialog = app.window(title=self.dialog_title)

        dialog['Edit'].set_edit_text(file_path)
        dialog['Открыть'].wait('ready', timeout=self.timeout)
        dialog['Открыть'].click_input()
        dialog.wait_not('visible', timeout=self.timeout)
