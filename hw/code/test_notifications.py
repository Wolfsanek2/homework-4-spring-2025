from ui.pages.notifications_page import NotificationsPage
from ui.locators.notifications_locators import NotificLocators
from test_vk_ads import BaseCase
from pytest import fixture


class TestNotificationsPage(BaseCase):
    @fixture(scope='function')
    def notifications_page(self):
        driver = self.driver
        driver.get(NotificationsPage.url)
        return NotificationsPage(driver)

    def test_all_checkbocks_disable(self, notifications_page):
        all_checkboxes = notifications_page.get_all_checkboxes()
        for locator in all_checkboxes:
            assert not notifications_page.check_checkbox_state(locator)[
                "enabled"]   
        stateSwitch = notifications_page.is_switch_active(
            NotificLocators.switch_by_email("aleksansdr.nov.2002@gmail.com"))
        assert not stateSwitch

    def test_checbocks_active_after_switch(self, notifications_page):
        switch = NotificLocators.switch_by_email("aleksansdr.nov.2002@gmail.com")
        notifications_page.toggle_email_switch(switch)
    
        all_checkboxes = notifications_page.get_all_checkboxes()
        for locator in all_checkboxes:
            assert notifications_page.check_checkbox_state(locator)[
                "enabled"]  
        assert not notifications_page.is_save_button_enabled()

    def test_checbocks_checked(self, notifications_page):
        switch = NotificLocators.switch_by_email("aleksansdr.nov.2002@gmail.com")
        notifications_page.toggle_email_switch(switch)
    
        all_checkboxes = notifications_page.get_all_checkboxes()
        for locator in all_checkboxes:
            notifications_page.click_checbocks(locator)
            state = notifications_page.check_checkbox_state(locator)
            assert state["enabled"] and state["checked"]
            assert notifications_page.is_save_button_enabled()
        
