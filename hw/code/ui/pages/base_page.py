import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = basic_locators.BasePageLocators()
    url = 'https://ads.vk.com/'

    def is_opened(self, timeout=15):
        return
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=30):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Элемент {locator} не найден в течении {timeout} секунд") from e

    def is_abscent(self, locator):
        try:
            WebDriverWait(self.driver).until(
                EC.presence_of_element_located(locator)
            )
            return False
        except TimeoutException:
            return True

    def hover(self, element: WebElement):
        ActionChains(self.driver).move_to_element(element).perform()

    # @allure.step('Search')
    # def search(self, query):
    #     elem = self.find(self.locators.QUERY_LOCATOR_ID)
    #     elem.send_keys(query)
    #     go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
    #     go_button.click()
    #     self.my_assert()

    @allure.step("Step 1")
    def my_assert(self):
        assert 1 == 1


    @allure.step('Click')
    def click(self, locator, timeout=10) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

