import allure
from py_selenium_auto.browsers.browser_services import BrowserServices

from userinyerface.configurations.configuration import Configuration
from userinyerface.models.schemas import DataTest, UserFields
from userinyerface.configurations.test_data_loader import DataLoader
from userinyerface.configurations.user_data_loader import UserDataLoader
from userinyerface.forms.main_form import MainForm
from userinyerface.forms.start_page import StartPage


class TestBase:

    @staticmethod
    def go_to_start_page():
        BrowserServices.Instance.browser.go_to(Configuration.start_url())
        BrowserServices.Instance.browser.wait_for_page_to_load()


    def open_main_form_from_start(self):
        self.go_to_start_page()
        start_page = StartPage()
        main_form = MainForm()

        assert start_page.state.is_displayed(), "Start page is not visible"
        start_page.click_next_page_button()

        assert main_form.state.is_displayed(), "Main form is not visible"
        return main_form


    @staticmethod
    def prepare_test_data():
        with allure.step("Load test data"):
            test_data: DataTest = DataLoader.get_test_data()
            return test_data


    @staticmethod
    def prepare_user_data():
        with allure.step("Load user data"):
            user_data: UserFields = UserDataLoader.get_user_data()
            return user_data
