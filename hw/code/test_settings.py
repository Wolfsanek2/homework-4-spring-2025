import pytest
from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.settings_page import SettingsPage, CreateSettingsPage


class TestSettingsPage(BaseCase):
    @fixture(scope='function')
    def settings_page(self):
        driver = self.driver
        driver.get(SettingsPage.url)
        return SettingsPage(driver)
    
    # def test_invalid_phone_error(self, driver, phone):
    #     self.settings_page.input_phone('abc')
    #     self.settings_page.click_save()
    #     assert self.settings_page.get_phone_error() == "Некорректный номер телефона"

    def test_add_email_button(self, settings_page):
        settings_page.click_add_email()
        assert settings_page.is_delete_email_button_visible()

    def test_delete_email_button(self, settings_page):
        settings_page.click_add_email()
        assert settings_page.is_delete_email_button_visible()
        settings_page.click_delete_email()
        assert not settings_page.is_delete_email_button_visible()

    # @pytest.mark.parametrize('inn', ['123', 'abc', '12345678901']) //?
    def test_invalid_inn_error(self, settings_page):
        settings_page.input_inn('abc')
        settings_page.click_save()
        assert settings_page.get_inn_error() == "Некорректный ИНН"

    def test_inn_length_error(self, settings_page):
        settings_page.input_inn('1234567')
        settings_page.click_save()
        assert settings_page.get_inn_error_less() == "Длина ИНН должна быть 12 символов"

    def test_save_button_appears_with_full_name(self, settings_page):
        settings_page.input_full_name('Иван Иванов')
        assert settings_page.is_save_button_visible()

    def test_save_button_appears_with_valid_inn(self, settings_page):
        settings_page.input_inn('123456789012')
        assert settings_page.is_save_button_visible()

    def test_empty_inn_error(self, settings_page):
        settings_page.input_full_name('Иван Иванов')
        settings_page.click_save()
        assert settings_page.get_inn_error_empty() == "Нужно заполнить"

    def test_empty_full_name_error(self, settings_page):
        settings_page.input_inn('123456789012')
        settings_page.click_save()
        assert settings_page.get_full_name_error() == "Нужно заполнить"

    # def test_hot_keys_modal(self, settings_page):
    #     settings_page.click_hot_keys_link()
    #     assert settings_page.is_hot_keys_modal_visible()

    def test_mytarget_modal(self, settings_page):
        settings_page.click_mytarget_bind()
        assert settings_page.is_mytarget_modal_visible() 