from selenium.webdriver.common.by import By


class NotificLocators:
    FINANCE_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Финансы')]/ancestor::label//input[@type='checkbox']")
    MODERATION_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Модерация')]/ancestor::label//input[@type='checkbox']")
    AD_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Рекламные кампании')]/ancestor::label//input[@type='checkbox']")
    RULES_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Правила для объявлений')]/ancestor::label//input[@type='checkbox']")
    EDIT_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Изменения в API')]/ancestor::label//input[@type='checkbox']")
    NEWS_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Новости')]/ancestor::label//input[@type='checkbox']")
    EVENTS_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Мероприятия')]/ancestor::label//input[@type='checkbox']")
    SALES_CHECKBOCKS = (
        By.XPATH, "//div[contains(text(), 'Акции, спецпредложения и прочие')]/ancestor::label//input[@type='checkbox']")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='settings-save']")

    def switch_by_email(email):
        return (By.XPATH, f"//span[contains(@class, 'vkuiSimpleCell__children') and text()='{email}']/ancestor::div[contains(@class, 'vkuiSimpleCell')]//label[contains(@class, 'vkuiSwitch')]")
