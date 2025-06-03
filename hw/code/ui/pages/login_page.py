from ui.pages.base_page import BasePage
from ui.locators import locators_vk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class LoginPage(BasePage):
    def login(self, phone_number, password):
        self.click(locators_vk.LoginPageLocators.LOGIN_LINK, timeout=10)
        time.sleep(1) 
        self.find(locators_vk.LoginPageLocators.PHONE_INPUT, timeout=10).send_keys(phone_number)
        time.sleep(1) 
        self.click(locators_vk.LoginPageLocators.PHONE_BTN, timeout=10)
        time.sleep(10)
        