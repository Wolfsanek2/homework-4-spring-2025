from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

    def input_website(self, website):
        self.find(self.locators.WEBSITE_INPUT).send_keys(website)
        return self

    def get_website_error(self):
        return self.find(self.locators.WEBSITE_ERROR).text