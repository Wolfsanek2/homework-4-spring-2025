from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.leadforms_page import LeadformsPage, CreateLeadformPage
import time
import pytest

class TestLeadforms(BaseCase):
    @fixture(scope='function')
    def leadforms_page(self):
        pass
        driver = self.driver
        driver.get(LeadformsPage.url)
        return LeadformsPage(driver)

    def test_create_leadform_buton_exists(self, leadforms_page):
        element = leadforms_page.find(leadforms_page.locators_leadforms.CREATE_LEADFORM_BTN)
        assert element.is_displayed()

    def test_create_lead_form_window_appears(self, leadforms_page: LeadformsPage):
        leadforms_page.click_create_leadform_button()
        assert leadforms_page.find(leadforms_page.locators_leadforms.CREATE_LEADFORM_WINDOW_TITLE).is_displayed()
    
    def test_edit_button_appears_on_hover(self, leadforms_page: LeadformsPage):
        leadforms_page.hover_first_leadform()
        assert leadforms_page.find(leadforms_page.locators_leadforms.LEADFORM_EDIT_BTN).is_displayed()

    def test_edit_leadform_window_appears(self, leadforms_page: LeadformsPage):
        leadforms_page.hover_first_leadform()
        leadforms_page.click_edit_button()
        assert leadforms_page.find(leadforms_page.locators_leadforms.EDIT_LEADFORM_WINDOW_TITLE).is_displayed()

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
        create_leadform_page.fill_required_fields_and_continue()
        create_leadform_page.click_back()
        assert create_leadform_page.is_design_section_active()

    def test_add_question(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_required_fields_and_continue()
        create_leadform_page.add_question()
        assert create_leadform_page.is_question_form_visible()

    def test_empty_question_error(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_required_fields_and_continue()
        create_leadform_page.add_question()
        create_leadform_page.click_continue()
        assert create_leadform_page.has_empty_question_error()

    def test_continue_to_result_section(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_required_fields_and_continue()
        create_leadform_page.add_question("Тестовый вопрос")
        create_leadform_page.click_continue()
        assert create_leadform_page.is_result_section_active()

    def test_result_section_default_texts(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_required_fields_and_continue()
        create_leadform_page.add_question("Тестовый вопрос")
        create_leadform_page.click_continue()
        assert create_leadform_page.get_result_title() == "Спасибо за ответы!"
        assert create_leadform_page.get_result_description() == "Заявка отправлена"

    def test_continue_to_settings_section(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.fill_required_fields_and_continue()
        create_leadform_page.add_question("Test Question")
        create_leadform_page.click_continue()
        create_leadform_page.click_continue()
        assert create_leadform_page.is_settings_section_active()

    def test_empty_settings_error(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.complete_all_sections()
        create_leadform_page.click_save()
        assert create_leadform_page.has_settings_error()

    def test_successful_leadform_creation(self, create_leadform_page: CreateLeadformPage):
        create_leadform_page.complete_all_sections(
            company_name="Test Company",
            title="Test Title",
            description="Test Description",
            question="Test Question",
            form_name="Test Form"
        )
        create_leadform_page.click_save()
        assert create_leadform_page.is_leadform_created("Test Form")