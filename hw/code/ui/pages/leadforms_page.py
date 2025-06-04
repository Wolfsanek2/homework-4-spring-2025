from ui.pages.base_page import BasePage
from ui.locators.leadforms_locators import LeadformsPageLocators

class LeadformsPage(BasePage):
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    locators_leadforms = LeadformsPageLocators()

    def create_leadform(self):
        self.click_create_leadform_button()
        pass

    def click_create_leadform_button(self):
        self.click(self.locators_leadforms.CREATE_LEADFORM_BTN)
