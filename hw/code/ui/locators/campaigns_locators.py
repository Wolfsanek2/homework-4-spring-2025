from selenium.webdriver.common.by import By

class CampaignsLocators: 
    CREATE_CAMPAIGN = (By.XPATH, "//span[text()='Создать кампанию']")

    SITE_CONVERSIONS_OPTION = (By.XPATH, "//span[text()='Сайт']")

    WEBSITE_INPUT = (By.CSS_SELECTOR, 'input[data-testid="site-select-input"]')
    WEBSITE_ERROR = (By.XPATH, "//div[text()='Неверный формат URL']")
    CREATE_CONTINUE_BTN = (By.XPATH, "//button[.//span[text()='Продолжить']]")

    IMPORTANT_DETAILS = (By.XPATH, "//h2[contains(., 'Важные детали')]")
    BUDGET_OPTIMIZATION_TOGGLE = (By.CSS_SELECTOR, "input[data-testid='budget-optimization']") #??
    BUDGET_INPUT = (By.XPATH, '//div[contains(@class, "Budget_budgetControlsWrapper__ITCir")]//input[@data-testid="targeting-not-set"]')

    ONE_ERROR = (By.XPATH, '//span[text()="1 ошибка"]')

    UTM_RADIO = (By.XPATH, '//label[.//span[text()="Добавлять UTM-метки вручную"]]')
    INVALID_UTM = (By.XPATH, '//input[@type="radio" and @value="manual"]')