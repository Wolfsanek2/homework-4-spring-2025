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
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        assert surveys_page.is_element_visible(surveys_page.locators.SURVEY_CREATE_MODAL)

    def test_empty_input_errors(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for continue button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CONTINUE_BUTTON))
        surveys_page.click_continue()
        # Add small delay to let errors appear
        time.sleep(1)
        errors = surveys_page.get_error_texts()
        assert errors["name"] == "Нужно заполнить"
        assert errors["company"] == "Нужно заполнить"
        assert errors["title"] == "Нужно заполнить"
        assert errors["description"] == "Нужно заполнить"

    def test_error_disappears_after_input(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for inputs to be visible
        surveys_page.wait.until(EC.visibility_of_element_located(surveys_page.locators.SURVEY_NAME_INPUT))
        surveys_page.fill_data("Test Survey", "Test Company", "Test Title", "Test Description")
        # Add small delay to let errors disappear
        time.sleep(1)
        errors = surveys_page.get_error_texts()
        assert errors["name"] == ""
        assert errors["company"] == ""
        assert errors["title"] == ""
        assert errors["description"] == ""

    def test_media_library_opens(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for load image button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.LOAD_IMAGE_BUTTON))
        surveys_page.click(surveys_page.locators.LOAD_IMAGE_BUTTON)
        # Add small delay to let file input appear
        time.sleep(1)
        assert surveys_page.is_element_visible(surveys_page.locators.LOAD_IMAGE_INPUT)

    def test_upload_image(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for load image button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.LOAD_IMAGE_BUTTON))
        surveys_page.upload_image("/path/to/test/image.jpg")  # You'll need to provide a valid test image path
        # Add small delay to let image upload
        time.sleep(2)
        assert surveys_page.is_element_visible(surveys_page.locators.UPLOADED_IMAGE_ITEM)

    def test_questions_section_opens(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for questions button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.QUESTIONS_BUTTON))
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        # Add small delay to let question input appear
        time.sleep(1)
        assert surveys_page.is_element_visible(surveys_page.locators.QUESTION_TITLE_INPUT)

    def test_add_question(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for questions button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.QUESTIONS_BUTTON))
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        # Add small delay to let question input appear
        time.sleep(1)
        surveys_page.click_add_question()
        # Add small delay to let question list appear
        time.sleep(1)
        assert surveys_page.is_element_visible(surveys_page.locators.QUESTION_LIST)

    def test_fill_question_and_answers(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for questions button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.QUESTIONS_BUTTON))
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        # Add small delay to let question input appear
        time.sleep(1)
        surveys_page.fill_title("Test Question")
        surveys_page.fill_answers("Answer 1", "Answer 2")
        # Add small delay to let text appear
        time.sleep(1)
        assert surveys_page.get_text(surveys_page.locators.QUESTION_TITLE_INPUT) == "Test Question"

    def test_add_stop_screen(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        # Wait for questions button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.QUESTIONS_BUTTON))
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        # Add small delay to let question input appear
        time.sleep(1)
        surveys_page.click(surveys_page.locators.ADD_STOP_BUTTON)
        # Add small delay to let stop screen appear
        time.sleep(1)
        assert surveys_page.is_element_visible(surveys_page.locators.STOP_HEADING_INPUT)

    def test_archive_survey(self, surveys_page):
        # Wait for button to be clickable
        surveys_page.wait.until(EC.element_to_be_clickable(surveys_page.locators.CREATE_SURVEY_BUTTON))
        surveys_page.click_create_survey_button()
        # Add small delay to let modal appear
        time.sleep(1)
        surveys_page.fill_data("Test Survey", "Test Company", "Test Title", "Test Description")
        # Add small delay to let data be filled
        time.sleep(1)
        surveys_page.click_continue()
        # Add small delay to let survey be created
        time.sleep(2)
        surveys_page.remove_survey()
        # Add small delay to let survey be archived
        time.sleep(1)
        assert not surveys_page.is_element_visible(surveys_page.locators.FIRST_SURVAY_NAME)

    def test_delete_all_forms(self, surveys_page):
        surveys_page.delete_all_forms("Test Survey")
        # Add small delay to let forms be deleted
        time.sleep(1)
        assert not surveys_page.is_element_visible(surveys_page.locators.FIRST_LEAD_FORM_NAME)
