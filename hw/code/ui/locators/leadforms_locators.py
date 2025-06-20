from selenium.webdriver.common.by import By

class LeadformsPageLocators:
    CREATE_LEADFORM_BTN = (By.XPATH, '//span[text()="Создать лид-форму"]')
    CREATE_LEADFORM_WINDOW_TITLE = (By.XPATH, '//h2[text()="Новая лид-форма"]')
    LEADFORM = (By.XPATH, '//span[contains(text(), "Лид-форма")]')
    LEADFORM_EDIT_BTN = (By.XPATH, '//span[text()="Редактировать"]')
    LEADFORM_ARCHIVE_BTN = (By.XPATH, '//span[text()="Архивировать"]')
    LEADFORM_ARCHIVE_CONFIRM_BTN = (By.XPATH, '//div[@data-testid="modal-confirm"]//span[text()="Архивировать"]')

    LEADFORM_SECTIONS = (By.XPATH, '//span[text()="Активные" or text()="В архиве"]//ancestor::div[@class="vkuiCustomSelectInput__input-group"]//input')
    ARCHIVE_SECTION = (By.XPATH, '//*[contains(@class, "vkuiCustomSelectOption") and text()="В архиве"]')

    def LEADFORM_ID_LOCATOR(self, leadform_id):
        return (By.XPATH, f'//span[text()="{leadform_id}"]')

    def LEADFORM_BY_NAME(self, leadform_name):
        return (By.XPATH, f'//span[contains(text(), "{leadform_name}")]//ancestor::div[@data-entityid]')

class LeadformFormPageLocators:
    CLOSE_WINDOW_BTN = (By.XPATH, '//button[@aria-label="Close"]')
    CONTINUE_BTN = (By.XPATH, '//span[text()="Продолжить"]//ancestor::button')
    EMPTY_INPUT_ERROR = (By.XPATH, '//div[text()="Нужно заполнить"]')
    COMPANY_NAME_INPUT = (By.XPATH, '//input[@placeholder="Название компании"]')
    COMPANY_NAME_ERROR = (By.XPATH, "//*[contains(text(), 'Название компании')]/ancestor::div[contains(@class, 'vkuiFormItem')]//div[text()='Нужно заполнить']")
    UPLOAD_LOGO_TITLE = (By.XPATH, '//span[text()="Загрузить логотип"]')
    SELECT_LOGO_INPUT = (By.XPATH, '//span[text()="Загрузить логотип"]')
    CHANGE_LOGO_INPUT = (By.XPATH, '//span[text()="Заменить"]')
    LOGO_ERROR = (By.XPATH, "//div[contains(@class, 'vkuiFormItem') and .//span[contains(text(), 'Логотип')]]//span[@role='alert']/div[text()='Нужно заполнить']")
    LOGO_IN_MEDIA = (By.CSS_SELECTOR, "div[class*='ItemList_item']")
    SAVE_LOGO_BTN = (By.XPATH, '//span[text()="Сохранить"]')
    IMAGE_CROPPER = (By.XPATH, '//div[contains(@class, "ImageCropper")]')
    TITLE_INPUT = (By.XPATH, '//input[@placeholder="Текст заголовка"]')
    DESCRIPTION_INPUT = (By.XPATH, '//input[@placeholder="Введите описание"]')
    ACTIVE_SECTION_TITLE = (By.CSS_SELECTOR, 'div[class*="CreateLeadFormModal_activeStep"]')

    DESCRIPTION_COUNTER = (By.XPATH, '//input[@placeholder="Введите описание"]//ancestor::div[contains(@class, "vkuiFormItem")]//div[@class=""]')
    
    MAX_LENGTH_ERROR = (By.XPATH, '//div[text()="Сократите текст"]')
    
    BACK_BTN = (By.XPATH, '//span[text()="Назад"]')
    
    ADD_QUESTION_BTN = (By.XPATH, '//span[text()="Добавить вопрос"]')
    QUESTION_CONTAINER = (By.XPATH, '//div[contains(@class, "Question_question__")]')
    QUESTION_INPUT = (By.XPATH, '//textarea[@placeholder="Напишите вопрос"]')
    EMPTY_QUESTION_ERROR = (By.XPATH, '//div[text()="Нужно заполнить"]')

    ANSWER_INPUT = (By.XPATH, '//input[@placeholder="Введите ответ"]')
    
    RESULT_TITLE = (By.XPATH, '//span[text()="Заголовок"]//ancestor::div[contains(@class, "vkuiFormItem")]//input')
    RESULT_DESCRIPTION = (By.XPATH, '//span[text()="Описание"]//ancestor::div[contains(@class, "vkuiFormItem")]//input')
    
    LEADFORM_NAME_INPUT = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    SAVE_BTN = (By.XPATH, '//span[text()="Сохранить"]')
    SETTINGS_ERROR = (By.XPATH, '//div[text()="Нужно заполнить"]')
    
    CREATED_FORM_TITLE = (By.XPATH, '//span[contains(text(), "Лид-форма") and contains(text(), "{0}")]')

    USER_NAME_INPUT = (By.XPATH, '//input[@placeholder="Введите фамилию, имя и отчество"]')

    ADRESS_INPUT = (By.XPATH, '//input[@placeholder="Введите адрес"]')

class CreateLeadformPageLocators(LeadformFormPageLocators):
    CREATE_LEADFORM_WINDOW_TITLE = (By.XPATH, '//h2[text()="Новая лид-форма"]')

class EditLeadFormPageLocators(LeadformFormPageLocators):
    EDIT_LEADFORM_WINDOW_TITLE = (By.XPATH, '//h2[text()="Редактирование лид-формы"]')
