from selenium.webdriver.common.by import By


class BasePageLocators:
    pass
    # QUERY_LOCATOR = (By.NAME, 'q')
    # QUERY_LOCATOR_ID = (By.ID, 'id-search-field')
    # GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    # START_SHELL = (By.ID, 'start-shell')
    # PYTHON_CONSOLE = (By.ID, 'hterm:row-nodes')


class MainPageLocators(BasePageLocators):
    pass
    # COMPREHENSIONS = (
    #     By.XPATH,
    #     '//code/span[@class="comment" and contains(text(), "comprehensions")]'
    # )
    # EVENTS = (By.ID, 'events')
    # READ_MORE = (By.CSS_SELECTOR, 'a.readmore')


class EventsPageLocators(BasePageLocators):
    pass
