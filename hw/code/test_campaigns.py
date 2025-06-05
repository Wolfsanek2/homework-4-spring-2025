from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.campaigns_page import CampaignPage
import time

class TestCampaign(BaseCase):
    @fixture(scope='function')
    def campaign_page(self):
        driver = self.driver
        driver.get(CampaignPage.url)
        return CampaignPage(driver)
    
    def test_create_campaign(self, campaign_page):
        campaign_page.create_campaign()

    def test_website_input_validation(self, campaign_page):
        self.campaign_page.click_site(campaign_page)
        campaign_page.input_website("invalid-url")
        campaign_page.click_continue()
        assert "Не удалось подгрузить данные ссылки" in campaign_page.get_website_error()

    def test_differences_input_limit(self, campaign_page):
        long_text = "a" * 301
        campaign_page.input_differences(long_text)
        assert "Превышен лимит символов" in campaign_page.get_differences_error()
