from selenium.webdriver.common.by import By


class LoginPageLocators:
    PHONE_INPUT = (By.CLASS_NAME, "vkuiUnstyledTextField__host")
    PHONE_BTN = (By.XPATH, "//button[.//span[text()='Продолжить']]")
    WARNING_TEXT = (By.XPATH, "")
    CLOSE_WARNING_BTN = (By.XPATH, "//span[text()='Скрыть']")
    CONFIRM_BY_PHONE = (By.XPATH, "//span[text()='Введите код из уведомления']")
    CONFIRN_ANOTHER_WAY_BTN = (By.XPATH, "//span[text()='Подтвердить другим способом']")
    CHOOSE_PASSWORD_BTN = (By.XPATH, "//span[text()='Пароль']")
    PASSWORD_INPUT = (By.NAME, "password")
    SEND_PASSWORD_BTN = (By.XPATH, "//span[text()='Продолжить']")
    BUISNESS_PROFILE_BTN = (By.XPATH, "//span[text()='Физическое лицо']")
