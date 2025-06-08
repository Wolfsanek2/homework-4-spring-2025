import time

from ui.pages.base_page import BasePage
from ui.locators.leadforms_locators import *

class LeadformsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators_leadforms = LeadformsPageLocators()

    def go_to_create_leadform_page(self):
        self.click_create_leadform_button()
        return CreateLeadformPage(self.driver)

    def click_create_leadform_button(self):
        self.click(self.locators_leadforms.CREATE_LEADFORM_BTN)
    
    def click_edit_leadform_button(self):
        self.click(self.locators_leadforms.LEADFORM_EDIT_BTN)

    def go_to_edit_leadform_page(self, leadform_name):
        self.hover_leadform(leadform_name)
        self.click_edit_leadform_button()

    def go_to_archive_section(self):
        self.click(self.locators_leadforms.LEADFORM_SECTIONS)
        self.click(self.locators_leadforms.ARCHIVE_SECTION)

    def hover_first_leadform(self):
        first_leadform = self.find(self.locators_leadforms.LEADFORM)
        self.hover(first_leadform)
    
    def hover_leadform(self, leadform_name):
        leadform = self.find(self.locators_leadforms.LEADFORM_BY_NAME(leadform_name))
        self.hover(leadform)

    def click_archive_button(self):
        self.click(self.locators_leadforms.LEADFORM_ARCHIVE_BTN)
        self.click(self.locators_leadforms.LEADFORM_ARCHIVE_CONFIRM_BTN)

    def archive_leadform(self, leadform_data):
        self.hover_leadform(leadform_data['leadform_name'])
        self.click_archive_button()

    def get_leadform_id(self, leadform_data):
        leadform = self.find(self.locators_leadforms.LEADFORM_BY_NAME(leadform_data['leadform_name']))
        return leadform.get_attribute("data-entityid")

    def is_leadform_archived(self, id):
        self.go_to_archive_section()
        return self.has_element(self.locators_leadforms.LEADFORM_ID_LOCATOR(id))

class LeadformFormPage(LeadformsPage):
    locators_leadform_form = LeadformFormPageLocators()

    def click_continue(self):
        self.find(self.locators_leadform_form.CONTINUE_BTN).click()
    
    def has_empty_input_error(self):
        return self.find(self.locators_leadform_form.EMPTY_INPUT_ERROR).is_displayed()
    
    def fill_company_name(self, name):
        self.fill(self.locators_leadform_form.COMPANY_NAME_INPUT, name)

    def has_company_name_error(self):
        return self.has_element(self.locators_leadform_form.COMPANY_NAME_ERROR)

    def upload_logo(self, filepath='media/test_picture.jpg'):
        if (self.is_element_present(self.locators_leadform_form.UPLOAD_LOGO_TITLE)):
            self.click(self.locators_leadform_form.SELECT_LOGO_INPUT)
        else:
            self.click(self.locators_leadform_form.CHANGE_LOGO_INPUT)
        self.click(self.locators_leadform_form.LOGO_IN_MEDIA)
        self.click(self.locators_leadform_form.SAVE_LOGO_BTN, 30)
    
    def has_logo_error(self):
        return self.has_element(self.locators_leadform_form.LOGO_ERROR)

    def fill_title(self, title):
        input = self.find(self.locators_leadform_form.TITLE_INPUT)
        input.clear()
        input.send_keys(title)
    
    def fill_description(self, description):
        input = self.find(self.locators_leadform_form.DESCRIPTION_INPUT)
        input.clear()
        input.send_keys(description)

    def fill_deco_section(self, company_name="Название_компании", title="Тестовый заголовок", description="Тестовое описание", logo='media/test_picture.jpg'):
        self.fill_company_name(company_name)
        self.fill_title(title)
        self.fill_description(description)
        self.upload_logo(logo)
        self.wait_until_element_disappears(self.locators_leadform_form.IMAGE_CROPPER)

    def is_question_section_active(self):
        return self.has_element(self.locators_leadform_form.QUESTIONS_ACTIVE_SECTION)
    
    def get_description_counter_value(self):
        return self.find(self.locators_leadform_form.DESCRIPTION_COUNTER).text
    
    def has_max_length_error(self):
        return self.has_element(self.locators_leadform_form.MAX_LENGTH_ERROR)
    
    def click_back(self):
        self.click(self.locators_leadform_form.BACK_BTN)
    
    def is_design_section_active(self):
        return "Новая лид-форма" in self.find(self.locators_leadform_form.CREATE_LEADFORM_WINDOW_TITLE).text
    
    def fill_question(self, question_text, q_number):
        if not self.is_element_present(self.locators_leadform_form.QUESTION_CONTAINER):
            self.click(self.locators_leadform_form.ADD_QUESTION_BTN)
        questions = self.find_all(self.locators_leadform_form.QUESTION_CONTAINER)
        if q_number > len(questions):
            self.click(self.locators_leadform_form.ADD_QUESTION_BTN)
        questions = self.find_all(self.locators_leadform_form.QUESTION_CONTAINER)
        inputs = questions[q_number-1].find_elements(
            self.locators_leadform_form.QUESTION_INPUT[0],
            self.locators_leadform_form.QUESTION_INPUT[1]
        )
        input = inputs[q_number-1]
        self.fill_input(input, question_text)
    
    def is_question_form_visible(self):
        return self.has_element(self.locators_leadform_form.QUESTION_INPUT)

    def fill_answers(self, answers, q_number):
        inputs = self.find_all(self.locators_leadform_form.ANSWER_INPUT)
        counter = 0
        for input in inputs:
            self.fill_input(input, answers[counter])
            counter += 1

    def fill_question_section(self, questions):
        q_number = 1
        for q in questions:
            self.fill_question(q['question'], q_number)
            self.fill_answers(q['answers'], q_number)
            q_number += 1

    def has_empty_question_error(self):
        return self.has_element(self.locators_leadform_form.EMPTY_QUESTION_ERROR)
    
    def is_result_section_active(self):
        return "Результат" in self.find(self.locators_leadform_form.ACTIVE_SECTION_TITLE).text
    
    def get_result_title(self):
        return self.find(self.locators_leadform_form.RESULT_TITLE).get_attribute('value')
    
    def get_result_description(self):
        return self.find(self.locators_leadform_form.RESULT_DESCRIPTION).get_attribute('value')
    
    def is_settings_section_active(self):
        return "Настройки" in self.find(self.locators_leadform_form.ACTIVE_SECTION_TITLE).text

    def fill_leadform_name(self, name):
        input = self.find(self.locators_leadform_form.LEADFORM_NAME_INPUT)
        input.clear()
        input.send_keys(name)
    
    def click_save(self):
        self.click(self.locators_leadform_form.SAVE_BTN)
    
    def has_settings_error(self):
        return self.has_element(self.locators_leadform_form.SETTINGS_ERROR)
    
    def fill_user_name(self, name='Тестовое имя'):
        self.fill(self.locators_leadform_form.USER_NAME_INPUT, name)

    def fill_adress(self, adress='Тестовый адрес'):
        self.fill(self.locators_leadform_form.ADRESS_INPUT, adress)

    def fill_settings_section(self):
        self.fill_user_name()
        self.fill_adress()

    def complete_all_sections(
            self,
            company_name="Тестовая компания",
            title="Тестовый заголовок", 
            description="Тестовое описание", 
            questions=[{
                'question': "Тестовый вопрос",
                'answers': ['Ответ 1', 'Ответ 2']
            }],
            leadform_name="Тестовая лид-форма"):
        self.fill_leadform_name(leadform_name)
        self.fill_deco_section(company_name, title, description)
        self.click_continue()
        self.fill_question_section(questions)
        self.click_continue()
        self.click_continue()
        self.fill_settings_section()

    def leadform_name_match(self, leadform_name):
        input = self.find(self.locators_leadform_form.LEADFORM_NAME_INPUT)
        if input.get_attribute('value') != leadform_name:
            return False
        return True

    def company_name_match(self, company_name):
        input = self.find(self.locators_leadform_form.COMPANY_NAME_INPUT)
        if input.get_attribute('value') != company_name:
            return False
        return True

    def title_match(self, title):
        input = self.find(self.locators_leadform_form.TITLE_INPUT)
        if input.get_attribute('value') != title:
            return False
        return True

    def description_match(self, description):
        input = self.find(self.locators_leadform_form.DESCRIPTION_INPUT)
        if input.get_attribute('value') != description:
            return False
        return True

    def deco_section_match(self, leadform_name, company_name, title, description):
        if not self.leadform_name_match(leadform_name):
            return False
        if not self.company_name_match(company_name):
            return False
        if not self.title_match(title):
            return False
        if not self.description_match(description):
            return False
        return True

class CreateLeadformPage(LeadformFormPage):
    locators_create_leadform = CreateLeadformPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self.url)
        self.click_create_leadform_button()

    def close_window(self):
        self.click(self.locators_create_leadform.CLOSE_WINDOW_BTN)

    def create_leadform(self, leadform_data):
        self.complete_all_sections(
            company_name=leadform_data['company_name'],
            title=leadform_data['title'],
            description=leadform_data['description'],
            questions=leadform_data['questions'],
            leadform_name=leadform_data['leadform_name']
        )
        self.click_save()

    def match_question(self, question):
        inputs = self.find_all(self.locators_leadform_form.QUESTION_INPUT)
        for input in inputs:
            if input.get_attribute('value') == question:
                return True
        return False

    def match_answers(self, answers):
        results = []
        inputs = self.find_all(self.locators_leadform_form.ANSWER_INPUT)
        for answer in answers:
            for input in inputs:
                if input.get_attribute('value') == answer:
                    results.append(True)
        if results.count(False) > 0:
            return False
        return True

    def questions_section_match(self, questions):
        for q in questions:
            if not self.match_question(q['question']):
                return False
            if not self.match_answers(q['answers']):
                return False
        return True

    def is_leadform_created(self, leadform_data):
        if not self.has_element(self.locators_leadforms.LEADFORM_BY_NAME(leadform_data['leadform_name'])):
            return False
        self.go_to_edit_leadform_page(leadform_data['leadform_name'])
        if not self.deco_section_match(
            leadform_data['leadform_name'],
            leadform_data['company_name'], 
            leadform_data['title'], 
            leadform_data['description']
        ):
            return False
        self.click_continue()
        if not self.questions_section_match(leadform_data['questions']):
            return False
        self.close_window()
        return True

class EditLeadformPage(CreateLeadformPage):
    locators_edit_leadform = EditLeadFormPageLocators()

    def __init__(self, driver, leadform_data):
        super().__init__(driver)
        self.leadform_initial_data = leadform_data
        self.create_leadform(leadform_data)
        self.go_to_edit_initial_leadform_page()

    def go_to_edit_initial_leadform_page(self):
        self.hover_leadform(self.leadform_initial_data['leadform_name'])
        self.click_edit_leadform_button()

    def close_window(self):
        self.click(self.locators_edit_leadform.CLOSE_WINDOW_BTN)

    def edit_leadform(self, leadform_data):
        self.complete_all_sections(
            company_name=leadform_data['company_name'],
            title=leadform_data['title'],
            description=leadform_data['description'],
            questions=leadform_data['questions'],
            leadform_name=leadform_data['leadform_name']
        )
        self.click_save()
    
    def is_leadform_edited(self, leadform_data):
        return self.is_leadform_created(leadform_data)
