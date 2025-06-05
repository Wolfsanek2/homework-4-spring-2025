from selenium.webdriver.common.by import By

class LeadformsPageLocators:
    CREATE_LEADFORM_BTN = (By.XPATH, '//span[text()="Создать лид-форму"]')
    CREATE_LEADFORM_WINDOW_TITLE = (By.XPATH, '//h2[text()="Новая лид-форма"]')
    LEADFORM = (By.XPATH, '//span[contains(text(), "Лид-форма")]')
    LEADFORM_EDIT_BTN = (By.XPATH, '//span[text()="Редактировать"]')
    EDIT_LEADFORM_WINDOW_TITLE = (By.XPATH, '//h2[text()="Редактирование лид-формы"]')

class CreateLeadformPageLocators:
    CREATE_LEADFORM_WINDOW_TITLE = (By.XPATH, '//h2[text()="Новая лид-форма"]')
    CLOSE_WINDOW_BTN = (By.XPATH, '//button[@aria-label="Close"]')
    CONTINUE_BTN = (By.XPATH, '//span[text()="Продолжить"]')
    EMPTY_INPUT_ERROR = (By.XPATH, '//div[text()="Нужно заполнить"]')
