from ui.pages.base_page import BasePage
from ui.locators.settings_locators import SettingsLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException

class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings/'
    locators = SettingsLocators()

    def input_phone(self, phone):
        self.find(self.locators.PHONE_INPUT).send_keys(phone)

    def input_inn(self, inn):
        self.find(self.locators.INN_INPUT).send_keys(inn)

    def input_full_name(self, name):
        self.find(self.locators.FULL_NAME_INPUT).send_keys(name)

    def click_save(self):
        el = self.wait(timeout=30).until(EC.element_to_be_clickable(self.locators.SAVE_BUTTON_CLICK))
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center', inline:'center'});", el
            )
            try:
                el.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", el)

    def click_add_email(self):
        self.click(self.locators.ADD_EMAIL_BUTTON)

    def click_delete_email(self):
        self.click(self.locators.DELETE_EMAIL_BUTTON)

    def click_hot_keys_link(self):
        self.click(self.locators.LIST_HOT_KEYS_LINK)

    def click_mytarget_bind(self):
        self.click(self.locators.MYTARGET_BIND_BUTTON)

    def is_hot_keys_modal_visible(self):
        try:
            self.find(self.locators.LIST_HOT_KEYS_MODAL, timeout=5)
            return True
        except TimeoutException:
            return False

    def is_mytarget_modal_visible(self):
        try:
            self.find(self.locators.MYTARGET_MODAL, timeout=10)
            return True
        except TimeoutException:
            return False

    def is_delete_email_button_visible(self):
        try:
            self.find(self.locators.DELETE_EMAIL_BUTTON, timeout=5)
            return True
        except TimeoutException:
            return False

    def is_save_button_visible(self):
        try:
            self.find(self.locators.SAVE_BUTTON, timeout=5)
            return True
        except TimeoutException:
            return False
        
    def get_inn_error_empty(self):
        try:
            return self.find(self.locators.INN_EMPTY, timeout=15).text
        except TimeoutException:
            return None
        
    def get_inn_error_less(self):
        try:
            return self.find(self.locators.INN_LESS, timeout=15).text
        except TimeoutException:
            return None

    def get_inn_error(self):
        try:
            return self.find(self.locators.INN_ERROR, timeout=15).text
        except TimeoutException:
            return None

    def get_full_name_error(self):
        try:
            return self.find(self.locators.FULL_NAME_ERROR_EMPTY, timeout=5).text
        except TimeoutException:
            return None

class CreateSettingsPage(SettingsPage):
    pass
    # locators_create_settings = CreateSettingsPagelocators()

    # def close_window(self):
    #     self.click(self.locators_create_settings.CLOSE_WINDOW_BTN)

    # def click_continue(self):
    #     self.click(self.locators_create_settings.CONTINUE_BTN)
    
    # def has_empty_input_error(self):
    #     self.find(self.locators_create_settings.EMPTY_INPUT_ERROR).is_displayed()
