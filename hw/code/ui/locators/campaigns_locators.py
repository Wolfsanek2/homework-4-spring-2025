from selenium.webdriver.common.by import By

class CampaignsLocators: 
    # Селекторы неправильные
    CREATE_CAMPAIGN = (By.XPATH, "//button[.//span[normalize-space(text())='Создать кампанию']]")

    SITE_CONVERSIONS_OPTION = (By.CSS_SELECTOR, 'div[data-id="site_conversions"]')

    WEBSITE_INPUT = (By.CSS_SELECTOR, 'input[data-testid="site-select-input"]')
    WEBSITE_ERROR = (By.XPATH, "//div[normalize-space(text())='Не удалось подгрузить данные ссылки']")
    CREATE_CONTINUE_BTN = (By.XPATH, "//span[contains(@class,'vkuiButton__content') and normalize-space(text())='Продолжить']")

    ## Следующие значения локаторов точно неправильные, предыдущие еще не успел проверить

    DIFFERENCES_INPUT = (By.CSS_SELECTOR, "textarea[data-testid='campaign-differences']")
    DIFFERENCES_ERROR = (By.XPATH, "//div[contains(text(), 'Превышен лимит символов')]")
    
    BUDGET_OPTIMIZATION_TOGGLE = (By.CSS_SELECTOR, "input[data-testid='budget-optimization-toggle']")
    BIDDING_STRATEGY_INPUT = (By.CSS_SELECTOR, "select[data-testid='bidding-strategy']")
    BUDGET_INPUT = (By.CSS_SELECTOR, "input[data-testid='campaign-budget']")
    MAX_CLICK_COST_INPUT = (By.CSS_SELECTOR, "input[data-testid='max-click-cost']")
    
    OFFLINE_CONVERSIONS_CHECKBOX = (By.CSS_SELECTOR, "input[data-testid='offline-conversions']")
    
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='campaign-continue']")
    CONTINUE_ERROR = (By.XPATH, "//div[contains(text(), 'Заполните обязательные поля')]") 