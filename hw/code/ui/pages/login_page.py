from ui.pages.base_page import BasePage
from ui.locators import login_locators
import time

class LoginPage(BasePage):
    login_url = 'https://id.vk.com'
    locators_login = login_locators.LoginPageLocators()
    def login_by_phone(self, phone_number, password):
        self.click_to_login_link()
        self.enter_phone_number(phone_number)
        self.choose_another_login_way()
        self.choose_login_by_password()
        self.enter_password(password)
        self.choose_buisness_profile()

    def click_to_login_link(self):
        self.click(self.locators.LOGIN_LINK)
    
    def enter_phone_number(self, phone_number):
        phone_input = self.find(self.locators_login.PHONE_INPUT)
        phone_input.send_keys(phone_number)
        self.click(self.locators_login.PHONE_BTN)

    def choose_another_login_way(self):
        self.click(self.locators_login.CONFIRN_ANOTHER_WAY_BTN, timeout=60)

    def choose_login_by_password(self):
        self.click(self.locators_login.CHOOSE_PASSWORD_BTN)
    
    def choose_buisness_profile(self):
        self.click(self.locators_login.BUISNESS_PROFILE_BTN)

    def enter_password(self, password):
        password_input = self.find(self.locators_login.PASSWORD_INPUT)
        password_input.send_keys(password)
        self.click(self.locators_login.SEND_PASSWORD_BTN)
        