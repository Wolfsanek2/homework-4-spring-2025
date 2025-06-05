from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    """Базовый класс для всех страниц"""
    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def is_element_present(self, locator) -> bool:
        """Проверяет наличие элемента на странице"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator) -> bool:
        """Проверяет видимость элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        """Кликает по элементу с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, text: str):
        """Вводит текст в поле"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:
        """Возвращает текст элемента"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_title(self) -> str:
        """Возвращает заголовок страницы"""
        return self.driver.title

    def get_url(self) -> str:
        """Возвращает текущий URL"""
        return self.driver.current_url

    def open(self, url: str):
        """Открывает указанный URL"""
        self.driver.get(url)

    def switch_to_frame(self, locator):
        """Переключается в iframe"""
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        return frame

    def switch_to_default_content(self):
        """Возвращается из iframe в основной контент"""
        self.driver.switch_to.default_content()

    def is_radio_selected(self, locator) -> bool:
        """Проверяет, выбран ли radio button"""
        return self.driver.find_element(*locator).is_selected()

    def select_radio(self, locator):
        """Выбирает radio button, если не выбран"""
        if not self.is_radio_selected(locator):
            self.click(locator)