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
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.is_opened()

    def find(self, locator, timeout=10):
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            raise TimeoutException(f"Элемент {locator} не найден в течении {timeout} секунд") from e
    
    def find_all(self, locator, timeout=10):
        try:
            return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            raise TimeoutException(f"Элементы {locator} не найдены в течении {timeout} секунд") from e

    def has_element(self, locator, timeout=10):
        self.find(locator, timeout)
        return True

    def is_abscent(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def hover(self, element: WebElement):
        ActionChains(self.driver).move_to_element(element).perform()

    def click(self, locator, timeout=10) -> WebElement:
        self.find(locator, timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def is_element_present(self, locator) -> bool:
        try:
            self.wait().until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator) -> bool:
        try:
            self.wait().until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def fill(self, locator, text: str):
        element = self.wait().until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        element = self.wait().until(EC.visibility_of_element_located(locator))
        return element.text

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.current_url

    def open(self, url: str):
        self.driver.get(url)

    def switch_to_frame(self, locator):
        frame = self.wait().until(EC.frame_to_be_available_and_switch_to_it(locator))
        return frame

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def is_radio_selected(self, locator) -> bool:
        return self.driver.find_element(*locator).is_selected()

    def select_radio(self, locator):
        if not self.is_radio_selected(locator):
            self.click(locator)
