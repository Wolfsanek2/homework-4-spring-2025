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

    def hover_first_leadform(self):
        first_leadform = self.find(self.locators_leadforms.LEADFORM)
        self.hover(first_leadform)

    def click_edit_button(self):
        self.click(self.locators_leadforms.LEADFORM_EDIT_BTN)

class CreateLeadformPage(LeadformsPage):
    locators_create_leadform = CreateLeadformPageLocators()

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
        self.find(self.locators_create_leadform.SELECT_LOGO_INPUT).click()
        self.find(self.locators_create_leadform.LOGO_IN_MEDIA).click()
        self.find(self.locators_create_leadform.SAVE_LOGO_BTN).click()
    
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
    
    def fill_answers(self):
        inputs = self.find_all(self.locators_create_leadform.ANSWER_INPUT)
        counter = 1
        for input in inputs:
            input.send_keys(f'Тестовый ответ {counter}')
            counter += 1

    def fill_question_section(self):
        self.add_question('Тестовый вопрос')
        self.fill_answers()

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
        self.find(self.locators_create_leadform.FORM_NAME_INPUT).send_keys(name)
    
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

    def complete_all_sections(self, company_name="Тестовая компания", title="Тестовый заголовок", description="Тестовое описание", question="Тестовый вопрос", form_name="Тестовая лид-форма"):
        self.fill_form_name(form_name)
        self.fill_deco_section(company_name, title, description)
        self.click_continue()
        self.fill_question_section()
        self.click_continue()
        self.click_continue()
        self.fill_settings_section()
    
    def is_leadform_created(self, form_name):
        locator = (self.locators_create_leadform.CREATED_FORM_TITLE[0], 
                  self.locators_create_leadform.CREATED_FORM_TITLE[1].format(form_name))
        return self.has_element(locator)
