from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.leadforms_page import LeadformsPage, CreateLeadformPage

class TestLeadforms(BaseCase):
    @fixture(scope='function')
    def leadforms_page(self):
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
