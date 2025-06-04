from ui.pages.base_page import BasePage
from ui.locators.main_locators import MainPageLocators
from ui.pages.leadforms_page import LeadformsPage

class MainPage(BasePage):
    locators_main = MainPageLocators()

    def go_to_leadforms_and_surveys(self):
        self.click(self.locators_main.LEADFORMS_AND_SURVEYS_BTN)
        return LeadformsPage(self.driver)
