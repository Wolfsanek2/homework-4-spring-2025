from ui.pages.base_page import BasePage
from ui.locators.leadforms_locators import LeadformsPageLocators, CreateLeadformPageLocators

class LeadformsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators_leadforms = LeadformsPageLocators()

    def go_to_create_leadform_page(self):
        self.click_create_leadform_button()
        return CreateLeadformPage(self.driver)

    def click_create_leadform_button(self):
        self.click(self.locators_leadforms.CREATE_LEADFORM_BTN)

    def go_to_archive_section(self):
        self.click(self.locators_leadforms.LEADFORM_SECTIONS)
        self.click(self.locators_leadforms.LEADFORM_SECTION_ARCHIVE)

    def hover_first_leadform(self):
        first_leadform = self.find(self.locators_leadforms.LEADFORM)
        self.hover(first_leadform)
    
    def hover_leadform(self, leadform_name):
        leadform = self.find(self.locators_leadforms.LEADFORM_BY_NAME(leadform_name))
        self.hover(leadform)

    def click_edit_button(self):
        self.click(self.locators_leadforms.LEADFORM_EDIT_BTN)

    def click_archive_button(self):
        self.click(self.locators_leadforms.LEADFORM_ARCHIVE_BTN)
        self.click(self.locators_leadforms.LEADFORM_ARCHIVE_CONFIRM_BTN)

    def archive_leadform(self, leadform_name):
        self.hover_leadform(leadform_name)
        self.click_archive_button()

class CreateLeadformPage(LeadformsPage):
    locators_create_leadform = CreateLeadformPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(self.url)
        self.click_create_leadform_button()

    def close_window(self):
        self.click(self.locators_create_leadform.CLOSE_WINDOW_BTN)

    def click_continue(self):
        self.find(self.locators_create_leadform.CONTINUE_BTN).click()
    
    def has_empty_input_error(self):
        return self.find(self.locators_create_leadform.EMPTY_INPUT_ERROR).is_displayed()
    
    def fill_company_name(self, name):
        self.find(self.locators_create_leadform.COMPANY_NAME_INPUT).send_keys(name)

    def has_company_name_error(self):
        return self.has_element(self.locators_create_leadform.COMPANY_NAME_ERROR)

    def upload_logo(self, filepath='media/test_picture.jpg'):
        self.click(self.locators_create_leadform.SELECT_LOGO_INPUT)
        self.click(self.locators_create_leadform.LOGO_IN_MEDIA)
        self.click(self.locators_create_leadform.SAVE_LOGO_BTN, 30)
    
    def has_logo_error(self):
        return self.has_element(self.locators_create_leadform.LOGO_ERROR)

    def fill_title(self, title):
        self.find(self.locators_create_leadform.TITLE_INPUT).send_keys(title)
    
    def fill_description(self, description):
        self.find(self.locators_create_leadform.DESCRIPTION_INPUT).send_keys(description)

    def fill_deco_section(self, company_name="Название_компании", title="Тестовый заголовок", description="Тестовое описание", logo='media/test_picture.jpg'):
        self.fill_company_name(company_name)
        self.fill_title(title)
        self.fill_description(description)
        self.upload_logo(logo)

    def is_question_section_active(self):
        return self.has_element(self.locators_create_leadform.QUESTIONS_ACTIVE_SECTION)
    
    def get_description_counter_value(self):
        return self.find(self.locators_create_leadform.DESCRIPTION_COUNTER).text
    
    def has_max_length_error(self):
        return self.has_element(self.locators_create_leadform.MAX_LENGTH_ERROR)
    
    def click_back(self):
        self.click(self.locators_create_leadform.BACK_BTN)
    
    def is_design_section_active(self):
        return "Новая лид-форма" in self.find(self.locators_create_leadform.CREATE_LEADFORM_WINDOW_TITLE).text
    
    def add_question(self, question_text=None):
        self.click(self.locators_create_leadform.ADD_QUESTION_BTN)
        if question_text:
            self.find(self.locators_create_leadform.QUESTION_INPUT).send_keys(question_text)
    
    def is_question_form_visible(self):
        return self.has_element(self.locators_create_leadform.QUESTION_INPUT)

    def fill_answers(self, answers):
        inputs = self.find_all(self.locators_create_leadform.ANSWER_INPUT)
        counter = 0
        for input in inputs:
            input.send_keys(answers[counter])
            counter += 1

    def fill_question_section(self, questions):
        for q in questions:
            self.add_question(q['question'])
            self.fill_answers(q['answers'])

    def has_empty_question_error(self):
        return self.has_element(self.locators_create_leadform.EMPTY_QUESTION_ERROR)
    
    def is_result_section_active(self):
        return "Результат" in self.find(self.locators_create_leadform.ACTIVE_SECTION_TITLE).text
    
    def get_result_title(self):
        return self.find(self.locators_create_leadform.RESULT_TITLE).get_attribute('value')
    
    def get_result_description(self):
        return self.find(self.locators_create_leadform.RESULT_DESCRIPTION).get_attribute('value')
    
    def is_settings_section_active(self):
        return "Настройки" in self.find(self.locators_create_leadform.ACTIVE_SECTION_TITLE).text

    def fill_form_name(self, name):
        input = self.find(self.locators_create_leadform.FORM_NAME_INPUT)
        input.clear()
        input.send_keys(name)
    
    def click_save(self):
        self.click(self.locators_create_leadform.SAVE_BTN)
    
    def has_settings_error(self):
        return self.has_element(self.locators_create_leadform.SETTINGS_ERROR)
    
    def fill_user_name(self, name='Тестовое имя'):
        self.find(self.locators_create_leadform.USER_NAME_INPUT).send_keys(name)

    def fill_adress(self, adress='Тестовый адрес'):
        self.find(self.locators_create_leadform.ADRESS_INPUT).send_keys(adress)

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
        self.fill_form_name(leadform_name)
        self.fill_deco_section(company_name, title, description)
        self.click_continue()
        self.fill_question_section(questions)
        self.click_continue()
        self.click_continue()
        self.fill_settings_section()

    def create_leadform(self, leadform_data):
        self.complete_all_sections(
            company_name=leadform_data['company_name'],
            title=leadform_data['title'],
            description=leadform_data['description'],
            questions=leadform_data['questions'],
            leadform_name=leadform_data['leadform_name']
        )
        self.click_save()

    def is_leadform_created(self, leadform_data):
        return self.has_element(self.locators_leadforms.LEADFORM_BY_NAME(leadform_data['leadform_name']))

    def get_leadform_id(self, leadform_data):
        leadform = self.find(self.locators_leadforms.LEADFORM_BY_NAME(leadform_data['leadform_name']))
        return leadform.get_attribute("data-entityid")

    def check_leadform_in_archive(self, id):
        self.go_to_archive_section()
        return self.has_element(id)