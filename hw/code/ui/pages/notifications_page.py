from ui.pages.base_page import BasePage
from ui.locators.notifications_locators import NotificLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException


class NotificationsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/notifications'
    locators = NotificLocators()

    def check_checkbox_state(self, locator):
        element = self.find(locator)

        is_checked = element.is_selected()
        is_enabled = element.is_enabled()

        return {
            "checked": is_checked,
            "enabled": is_enabled
        }

    def get_all_checkboxes(self):
        return [
            NotificLocators.FINANCE_CHECKBOCKS,
            NotificLocators.MODERATION_CHECKBOCKS,
            NotificLocators.AD_CHECKBOCKS,
            NotificLocators.RULES_CHECKBOCKS,
            NotificLocators.EDIT_CHECKBOCKS,
            NotificLocators.NEWS_CHECKBOCKS,
            NotificLocators.EVENTS_CHECKBOCKS,
            NotificLocators.SALES_CHECKBOCKS
        ]

    def click_checbocks(self, locator):
        self.click(locator)

    def toggle_email_switch(self, locator):
        self.click(locator)

    def is_switch_active(self, locator):
        element = self.find(locator)
        return element.is_selected()
    
    def is_save_button_enabled(self):
        button = self.find(NotificLocators.SAVE_BUTTON)

        is_disabled = button.get_attribute("disabled") is not None

        return not is_disabled
