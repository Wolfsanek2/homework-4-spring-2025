import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
import time
from ui.pages.login_page import LoginPage
from ui.pages.leadforms_page import LeadformsPage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.campaigns_page import CampaignPage
from utils.session import Session
from utils.local_storage import get_all_local_storage, clear_local_storage, local_storage_set_item
from utils.session import write_session_to_file

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.leadforms_page = LeadformsPage(driver)
        self.main_page = MainPage(driver)
        self.settings_page = SettingsPage(driver)
        self.campaign_page = CampaignPage(driver)

        session = self.extract_session(request)
        if session['cookie'] is None or session['local_storage'] is None:
            credentials = request.getfixturevalue('credentials')
            login_page = LoginPage(driver)
            login_page.login_by_phone(
                credentials["phone_number"],
                credentials["password"]
            )
            session['cookie'] = self.driver.get_cookies()
            session['local_storage'] = get_all_local_storage(self.driver)
            write_session_to_file(session)
        else:
            for cookie in session['cookie']:
                self.driver.add_cookie(cookie)
            clear_local_storage(self.driver)
            for key, value in session['local_storage'].items():
                local_storage_set_item(self.driver, key, value)
    
    def extract_session(self, request: FixtureRequest) -> Session:
        return request.getfixturevalue('session')

@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = config.get("driver")