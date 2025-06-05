from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from ui.locators.campaigns_locators import CampaignsLocators
from ui.pages.base_page import BasePage

class CampaignPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard'
    locators = CampaignsLocators()

    def create_campaign(self):
        self.click(self.locators.CREATE_CAMPAIGN)

    def click_site(self):
        self.create_campaign()
        self.click(self.locators.SITE_CONVERSIONS_OPTION)

    def click_site_success(self):
        self.click_site()
        self.input_website("https://ads.vk.com/")
        self.click_continue()

    def input_website(self, website):
        self.find(self.locators.WEBSITE_INPUT).send_keys(website)
        return self

    def get_website_error(self):
        return self.find(self.locators.WEBSITE_ERROR).text
    
    def click_continue(self):
        self.wait().until(lambda d: 'vkuiClickable__realClickable' in d.find_element(*self.locators.CREATE_CONTINUE_BTN).get_attribute("class"))
        return self.click(self.locators.CREATE_CONTINUE_BTN)
    
    def check_length(self):
        line = "a" * 301
        full_text = self.find(self.locators.IMPORTANT_DETAILS).text
        return full_text.split()[-1]
    
    def budget_toggle(self):
        self.click(self.locators.BUDGET_OPTIMIZATION_TOGGLE)

    def fill_budget(self, budget):
        self.find(self.locators.BUDGET_INPUT).send_keys(budget)

    def settings_continue(self):
        self.click_site_success()
        self.fill_budget(10000)
        self.click_continue()

    def test_groups_empty_inputs(self):
        self.click_continue()
        try:
            self.find(self.locators.ONE_ERROR)
            return True
        except TimeoutException:
            return False
        
    def test_invalid_utm(self):
        self.settings_continue()
        self.find(self.locators.UTM_RADIO).send_keys("1")
        try:
            self.find(self.locators.INVALID_UTM)
            return True
        except TimeoutException:
            return False 
        