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
        self.click(self.locators_leadforms.EDIT_LEADFORM_WINDOW_TITLE)

class CreateLeadformPage(LeadformsPage):
    locators_create_leadform = CreateLeadformPageLocators()

    def close_window(self):
        self.click(self.locators_create_leadform.CLOSE_WINDOW_BTN)

    def click_continue(self):
        self.click(self.locators_create_leadform.CONTINUE_BTN)
    
    def has_empty_input_error(self):
        self.find(self.locators_create_leadform.EMPTY_INPUT_ERROR).is_displayed()
