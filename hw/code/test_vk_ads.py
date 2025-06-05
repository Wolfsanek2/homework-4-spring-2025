import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
import time
from ui.pages.login_page import LoginPage
from ui.pages.leadforms_page import LeadformsPage
from ui.pages.main_page import MainPage
from utils.session import Session
from utils.local_storage import get_all_local_storage, clear_local_storage, local_storage_set_item
from utils.session import write_session_to_file

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
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


# class TestLogin(BaseCase):
#     def test_login(self, credentials):
#         self.login_page.login_by_phone(
#             credentials["phone_number"],
#             credentials["password"]
#         )

# class TestLK(BaseCase):
#     def test_search_classmate(self, credentials):
#         self.login_page.login(
#             credentials["username"],
#             credentials["password"]
#         )

#         # self.feed_page = FeedPage(self.driver) 

#         username = "Александр Новиков"
#         self.feed_page.search_classmate(username, "user_189524")
#         assert username == self.feed_page.get_user_name()

#     def test_search_lesson_info(self, credentials):
#         self.login_page.login(
#             credentials["username"],
#             credentials["password"]
#         )

#         # self.feed_page = FeedPage(self.driver)
#         lesson_info = self.feed_page.search_lesson_info(30921)
#         assert "Семинар 2. End-to-End тесты на Python" in lesson_info.text, "название занятия не совпадает"
