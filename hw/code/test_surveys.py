from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.surveys_page import SurveyPage

class TestSurveys(BaseCase):
    @fixture(scope='function')
    def surveys_page(self):
        driver = self.driver
        driver.get(SurveyPage.url)
        return SurveyPage(driver)

    def test_create_survey_button_exists(self, surveys_page):
        element = surveys_page.find(surveys_page.locators.CREATE_SURVEY_BUTTON)
        assert element.is_displayed()

    def test_create_survey_window_appears(self, surveys_page):
        surveys_page.click_create_survey_button()
        assert surveys_page.find(surveys_page.locators.SURVEY_CREATE_MODAL).is_displayed()

    def test_empty_input_errors(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click_continue()
        errors = surveys_page.get_error_texts()
        assert errors["name"] == "Нужно заполнить"
        assert errors["company"] == "Нужно заполнить"
        assert errors["title"] == "Нужно заполнить"
        assert errors["description"] == "Нужно заполнить"

    def test_media_library_window_appears(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.LOAD_IMAGE_BUTTON)
        assert surveys_page.find(surveys_page.locators.UPLOAD_IMAGE_MODAL).is_displayed()

    def test_upload_image(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.upload_image("utils/image.png")
        assert surveys_page.find(surveys_page.locators.UPLOADED_IMAGE_ITEM).is_displayed()

    def test_questions_section_appears(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        assert surveys_page.find(surveys_page.locators.QUESTION_LIST).is_displayed()

    def test_add_question(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        surveys_page.click_add_question()
        assert len(surveys_page.find_all(surveys_page.locators.QUESTION_LIST)) > 0

    def test_fill_question(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        surveys_page.click_add_question()
        surveys_page.fill_title("Test Question")
        assert surveys_page.find(surveys_page.locators.QUESTION_TITLE_INPUT).get_attribute("value") == "Test Question"

    def test_fill_answers(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        surveys_page.click_add_question()
        surveys_page.fill_answers("Answer 1", "Answer 2")
        assert surveys_page.find(surveys_page.locators.ANSWER_1_INPUT).get_attribute("value") == "Answer 1"
        assert surveys_page.find(surveys_page.locators.ANSWER_2_INPUT).get_attribute("value") == "Answer 2"

    def test_selector_many(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        surveys_page.click_add_question()
        surveys_page.click_selector_many()
        assert surveys_page.find(surveys_page.locators.SELECTOR_MANY).is_displayed()

    def test_selector_answer(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        surveys_page.click_add_question()
        surveys_page.click_selector_answer()
        assert surveys_page.find(surveys_page.locators.SELECTOR_ANSWER).is_displayed()

    def test_selector_scale(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.click(surveys_page.locators.QUESTIONS_BUTTON)
        surveys_page.click_add_question()
        surveys_page.click_selector_scale()
        assert surveys_page.find(surveys_page.locators.SELECTOR_SCALE).is_displayed()

    def test_fill_thanks(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.fill_thanks("Thank you")
        assert surveys_page.find(surveys_page.locators.HEADER_3).get_attribute("value") == "Thank you!"

    def test_fill_description(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.fill_description("Test description")
        assert surveys_page.find(surveys_page.locators.DESCRIPTION_3).get_attribute("value") == "Test description"

    def test_fill_link(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.fill_link("https://test.com")
        assert surveys_page.find(surveys_page.locators.LINK_3).get_attribute("value") == "https://test.com"

    def test_archive_survey(self, surveys_page):
        surveys_page.click_create_survey_button()
        surveys_page.remove_survey()
        assert not surveys_page.find(surveys_page.locators.FIRST_SURVAY_NAME).is_displayed()

    def test_delete_all_forms(self, surveys_page):
        surveys_page.delete_all_forms("Test Survey")
        assert not surveys_page.find(surveys_page.locators.FIRST_LEAD_FORM_NAME).is_displayed() 