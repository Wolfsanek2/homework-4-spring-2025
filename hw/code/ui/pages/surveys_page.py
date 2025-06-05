from ..pages.base_page import BasePage
from ..locators.survey_locators import SurveyLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SurveyPage(BasePage):
    url = "https://ads.vk.com/hq/leadads/surveys"
    locators = SurveyLocators()

    def click_continue(self):
        self.click(self.locators.CONTINUE_BUTTON)

    def click_create_survey_button(self):
        self.click(self.locators.CREATE_SURVEY_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.locators.SURVEY_CREATE_MODAL))

    def get_last_image_name_from_media_library(self) -> str:
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        return self.get_text(self.locators.UPLOADED_IMAGE_NAME)

    def fill_empty_data(self):
        self.fill(self.locators.SURVEY_NAME_INPUT, "")
        self.fill(self.locators.SURVEY_COMPANY_NAME_INPUT, "")
        self.fill(self.locators.SURVEY_TITLE_INPUT, "")
        self.fill(self.locators.SURVEY_DESCRIPTION_INPUT, "")

    def fill_data(self, name, company, title, desc):
        # Wait for inputs to be visible
        self.wait.until(EC.visibility_of_element_located(self.locators.SURVEY_NAME_INPUT))
        self.wait.until(EC.visibility_of_element_located(self.locators.SURVEY_COMPANY_NAME_INPUT))
        self.wait.until(EC.visibility_of_element_located(self.locators.SURVEY_TITLE_INPUT))
        self.wait.until(EC.visibility_of_element_located(self.locators.SURVEY_DESCRIPTION_INPUT))

        self.fill(self.locators.SURVEY_NAME_INPUT, name)
        self.fill(self.locators.SURVEY_COMPANY_NAME_INPUT, company)
        self.fill(self.locators.SURVEY_TITLE_INPUT, title)
        self.fill(self.locators.SURVEY_DESCRIPTION_INPUT, desc)

    def upload_image(self, filepath: str):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.locators.LOAD_IMAGE_INPUT))
        self.click(self.locators.LOAD_IMAGE_INPUT)
        # self.driver.execute_script(
        #     "arguments[0].style.display = 'block';", 
        #     self.driver.find_element(*self.locators.LOAD_IMAGE_INPUT)
        # )

        self.driver.execute_script("arguments[0].style.display = 'block';", filepath)
        # self.fill(self.locators.LOAD_IMAGE_INPUT, filepath)

    def delete_all_from_media_library(self):
        self.click(self.locators.EDIT_IMAGES_BUTTON)
        self.click(self.locators.SELECT_ALL_IMAGES_BUTTON)
        self.click(self.locators.DELETE_IMAGES_BUTTON)
        self.click(self.locators.CONFIRM_DELETE_BUTTON)

    def fill_title(self, title):
        self.wait.until(EC.visibility_of_element_located(self.locators.QUESTION_TITLE_INPUT))
        self.fill(self.locators.QUESTION_TITLE_INPUT, title)

    def click_add_question(self):
        self.click(self.locators.ADD_QUESTION_BUTTON)
        # Wait for question input to appear
        self.wait.until(EC.visibility_of_element_located(self.locators.QUESTION_TITLE_INPUT))

    def fill_answer(self, answer):
        self.wait.until(EC.visibility_of_element_located(self.locators.ANSWER_1_INPUT))
        self.fill(self.locators.ANSWER_1_INPUT, answer)

    def fill_answers(self, answer1, answer2):
        self.wait.until(EC.visibility_of_element_located(self.locators.ANSWER_1_INPUT))
        self.fill(self.locators.ANSWER_1_INPUT, answer1)
        self.wait.until(EC.visibility_of_element_located(self.locators.ANSWER_2_INPUT))
        self.fill(self.locators.ANSWER_2_INPUT, answer2)

    def click_selector_many(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_MANY)

    def click_selector_answer(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_ANSWER)

    def click_selector_scale(self):
        self.click(self.locators.SELECTOR_INPUT)
        self.click(self.locators.SELECTOR_SCALE)

    def fill_thanks(self, thanks):
        self.wait.until(EC.visibility_of_element_located(self.locators.HEADER_3))
        self.fill(self.locators.HEADER_3, thanks)

    def fill_description(self, description):
        self.wait.until(EC.visibility_of_element_located(self.locators.DESCRIPTION_3))
        self.fill(self.locators.DESCRIPTION_3, description)

    def fill_link(self, link):
        self.wait.until(EC.visibility_of_element_located(self.locators.LINK_3))
        self.fill(self.locators.LINK_3, link)

    def remove_survey(self):
        self.click(self.locators.ARCHIVE_BUTTON)
        self.click(self.locators.ARCHIVE_ACCEPT_BUTTON)

    def click_last_image_name_from_media_library(self):
        self.click(self.locators.LOAD_IMAGE_BUTTON)
        self.hover(self.locators.UPLOADED_IMAGE_ITEM)
        self.click(self.locators.UPLOADED_IMAGE_NAME)
        self.wait.until(EC.invisibility_of_element_located(self.locators.UPLOAD_IMAGE_MODAL))

    def get_form_name(self) -> str:
        return self.get_text(self.locators.FIRST_LEAD_FORM_NAME)

    def get_error_texts(self) -> dict:
        try:
            return {
                "name": self.get_text(self.locators.ERROR_1_TITLE).strip(),
                "company": self.get_text(self.locators.ERROR_1_COMPANY).strip(),
                "title": self.get_text(self.locators.ERROR_1_HEADER).strip(),
                "description": self.get_text(self.locators.ERROR_1_DESCRIPTION).strip(),
            }
        except TimeoutException:
            return {
                "name": "",
                "company": "",
                "title": "",
                "description": "",
            }
    
    def delete_all_forms(self, name: str):
        try:
            self.click(self.locators.SELECT_ALL_FORMS)
            self.click(self.locators.SELECT_ACTIONS_BUTTON)
            self.click(self.locators.DELETE_ACTION)
        except Exception as e:
            print(f"Не удалось удалить опросы: {e}")