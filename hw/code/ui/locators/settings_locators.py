from selenium.webdriver.common.by import By

class SettingsLocators:
    PHONE_INPUT = (By.CSS_SELECTOR, "input[data-testid='general-phone']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='settings-save']")
    ADD_EMAIL_BUTTON = (By.XPATH, "//span[normalize-space(text())='Добавить email']")
    DELETE_EMAIL_BUTTON = (By.XPATH, "//button[.//span[normalize-space(text())='Удалить']]")
    INN_INPUT = (By.CSS_SELECTOR, "input[data-testid='general-ord-inn']")
    INN_ERROR = (By.XPATH, "//div[normalize-space(text())='Некорректный ИНН']")
    INN_EMPTY = (By.XPATH, "//div[normalize-space(text())='Нужно заполнить']")
    INN_LESS = (By.XPATH, "//div[normalize-space(text())='Длина ИНН должна быть 12 символов']")
    SAVE_BUTTON_CLICK = (By.CSS_SELECTOR, "button[data-testid='settings-save']")
    FULL_NAME_INPUT = (By.CSS_SELECTOR, "input[data-testid='general-ord-name']")
    FULL_NAME_ERROR_EMPTY = (By.XPATH, "//div[normalize-space(text())='Нужно заполнить']")
    LIST_HOT_KEYS_LINK = (By.CSS_SELECTOR, "//button[.//span[normalize-space(text())='Список горячих клавиш']]")
    LIST_HOT_KEYS_MODAL = (By.XPATH, "//span[normalize-space(text())='Горячие клавиши']]")
    MYTARGET_BIND_BUTTON = (By.XPATH, "//span[normalize-space(text())='Привязать кабинет myTarget']")
    MYTARGET_MODAL = ( By.XPATH, "//section[.//span[normalize-space(text())='Привязать кабинет myTarget']]")
    
