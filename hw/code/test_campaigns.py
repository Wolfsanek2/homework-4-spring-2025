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

    def test_website_input_validation(self, campaign_page):
        campaign_page.click_site()
        campaign_page.input_website("invalid-url")
        campaign_page.click_continue()
        assert "Неверный формат URL" in campaign_page.get_website_error()

    def test_input_length(self, campaign_page):
        campaign_page.click_site_success()
        length = campaign_page.check_length()
        assert "300" == length

    def test_ok(self, campaign_page):
        campaign_page.click_site_success()

        campaign_page.fill_budget(10000)
        time.sleep(1) # иначе не работает
        campaign_page.click_continue()

    def test_groups_empty_inputs(self, campaign_page):
        campaign_page.settings_continue()

        assert campaign_page.test_groups_empty_inputs() == True

    def test_invalid_utm(self, campaign_page):
        assert campaign_page.test_invalid_utm() == True


    # def test_toggle_ok(self, campaign_page): не работает
    #     campaign_page.click_site_success()
    #     campaign_page.budget_toggle()

    # def test_empty_inputs(self, campaign_page): Не работает пока
    #     campaign_page.click_site()
    #     campaign_page.input_website("https://ads.vk.com/")
    #     campaign_page.click_continue()