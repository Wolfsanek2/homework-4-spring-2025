from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.surveys_page import SurveyPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class TestSurveys(BaseCase):
    @fixture(scope='function')
    def surveys_page(self):
        driver = self.driver
        driver.get(SurveyPage.url)
        return SurveyPage(driver)

    def test_create_survey_button_exists(self, surveys_page):
        assert surveys_page.is_element_visible(surveys_page.locators.CREATE_SURVEY_BUTTON)

    def test_create_survey_window_appears(self, surveys_page):
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        assert surveys_page.is_element_visible(surveys_page.locators.SURVEY_CREATE_MODAL)

    def test_empty_input_errors(self, surveys_page):
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.CONTINUE_BUTTON))
        surveys_page.click_continue()
        
        errors = surveys_page.get_error_texts()
        assert errors["name"] == "Нужно заполнить"
        assert errors["company"] == "Нужно заполнить"
        assert errors["title"] == "Нужно заполнить"
        assert errors["description"] == "Нужно заполнить"

    def test_error_disappears_after_input(self, surveys_page):
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        surveys_page.wait().until(EC.visibility_of_element_located(surveys_page.locators.SURVEY_NAME_INPUT))
        surveys_page.fill_data("Test Survey", "Test Company", "Test Title", "Test Description")

        errors = surveys_page.get_error_texts()
        assert errors["name"] == ""
        assert errors["company"] == ""
        assert errors["title"] == ""
        assert errors["description"] == ""

    def test_media_library_opens(self, surveys_page):
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.LOAD_IMAGE_BUTTON))
        surveys_page.click(surveys_page.locators.LOAD_IMAGE_BUTTON)

        surveys_page.wait().until(EC.visibility_of_element_located(surveys_page.locators.LOAD_IMAGE_INPUT))

    def test_upload_image(self, surveys_page):
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        surveys_page.wait().until(EC.element_to_be_clickable(surveys_page.locators.LOAD_IMAGE_BUTTON))
        surveys_page.upload_image("media/test_picture.jpg")

        assert surveys_page.is_element_visible(surveys_page.locators.UPLOADED_IMAGE_ITEM)