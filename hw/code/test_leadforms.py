from test_vk_ads import BaseCase
from pytest import fixture

@fixture(scope='function')
def go_to_leadforms(driver):
    driver.main_page.go_to_leadforms_and_surveys()

class TestLeadforms(BaseCase):
    def test_create_leadform_buton_exists(self):
        self.main_page.go_to_leadforms_and_surveys()
        element = self.leadforms_page.find(self.leadforms_page.locators_leadforms.CREATE_LEADFORM_BTN)
        assert element.is_displayed()

    def test_create_lead_form_appears(self):
        pass
