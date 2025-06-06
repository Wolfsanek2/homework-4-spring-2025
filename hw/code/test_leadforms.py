from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.leadforms_page import LeadformsPage, CreateLeadformPage
import time
import pytest

leadform_data={
    'company_name': 'Тестовая компания',
    'title': 'Тестовый заголовок',
    'description': 'Тестовое описание',
    'questions': [{
        'question': 'Тестовый вопрос',
        'answers': ['Тестовый ответ 1', 'Тестовый ответ 2']
    }],
    'leadform_name': 'Тестовая лидформа'
}

class TestLeadforms(BaseCase):
    @fixture(scope='function')
    def leadforms_page(self):
        driver = self.driver
        driver.get(LeadformsPage.url)
        return LeadformsPage(driver)

    @pytest.fixture
    def create_leadform_fixture(self):
        create_leadform_page = CreateLeadformPage(self.driver)
        yield create_leadform_page
        create_leadform_page.archive_leadform(leadform_data['leadform_name'])

    def test_create_leadform(self, create_leadform_fixture: CreateLeadformPage):
        create_leadform_fixture.create_leadform(leadform_data)
        assert create_leadform_fixture.is_leadform_created(leadform_data)

    def test_edit_leadform(self):
        pass

    def test_archive_leadform(self):
        pass

class TestCreateLeadform(BaseCase):
    @fixture(scope='function')
    def create_leadform_page(self):
        driver = self.driver
        driver.get(LeadformsPage.url)
        return LeadformsPage(driver).go_to_create_leadform_page()
    
    def test_close_window(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.close_window()
        assert create_leadform_page.is_abscent(create_leadform_page.locators_create_leadform.CLOSE_WINDOW_BTN)
    
    def test_empty_input_errors(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.click_continue()
        assert create_leadform_page.has_empty_input_error()

    def test_error_disappears_after_input(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.click_continue()
        assert create_leadform_page.has_company_name_error()
        create_leadform_page.fill_company_name("Название_компании")
        assert create_leadform_page.is_abscent(create_leadform_page.locators_create_leadform.COMPANY_NAME_ERROR)
    
    def test_error_disappears_after_logo_select(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.click_continue()
        assert create_leadform_page.has_company_name_error()
        create_leadform_page.upload_logo("test_logo.png")
        assert create_leadform_page.is_abscent(create_leadform_page.locators_create_leadform.LOGO_ERROR)
    
    def test_continue_to_questions_section(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_deco_section()
        create_leadform_page.click_continue()
        assert create_leadform_page.is_question_section_active()

    def test_character_counter(self, create_leadform_page: CreateLeadformPage):
        test_text = "Тестовое описание"
        create_leadform_page.fill_description(test_text)
        counter_value = create_leadform_page.get_description_counter_value()
        assert f'{len(test_text)} / 35' == counter_value

    def test_max_length_error(self, create_leadform_page: CreateLeadformPage):
        long_text = "a" * 51
        create_leadform_page.fill_description(long_text)
        create_leadform_page.click_continue()
        assert create_leadform_page.has_max_length_error()

    def test_back_to_design_section(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_deco_section()
        create_leadform_page.click_continue()
        create_leadform_page.click_back()
        assert create_leadform_page.is_design_section_active()

    def test_add_question(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_deco_section()
        create_leadform_page.click_continue()
        create_leadform_page.add_question()
        assert create_leadform_page.is_question_form_visible()

    def test_continue_to_result_section(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_deco_section()
        create_leadform_page.click_continue()
        create_leadform_page.fill_question_section()
        create_leadform_page.click_continue()
        assert create_leadform_page.is_result_section_active()

    def test_result_section_default_texts(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_deco_section()
        create_leadform_page.click_continue()
        create_leadform_page.fill_question_section()
        create_leadform_page.click_continue()
        assert create_leadform_page.get_result_title() == "Спасибо за ответы!"
        assert create_leadform_page.get_result_description() == "Заявка отправлена"

    def test_continue_to_settings_section(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_deco_section()
        create_leadform_page.click_continue()
        create_leadform_page.fill_question_section()
        create_leadform_page.click_continue()
        create_leadform_page.click_continue()
        assert create_leadform_page.is_settings_section_active()

    def test_successful_leadform_creation(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.complete_all_sections(
            company_name="Тестовая компания",
            title="Тестовый заголовок",
            description="Тестовое описание",
            question="Тестовый вопрос",
            form_name="Тестовая лид-форма"
        )
        create_leadform_page.click_save()
        assert create_leadform_page.is_leadform_created("Тестовая лид-форма")
