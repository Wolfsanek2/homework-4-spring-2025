from selenium.webdriver.common.by import By
from ..locators.basic_locators import BasePageLocators


class SurveyLocators(BasePageLocators):
    CREATE_SURVEY_BUTTON = (By.XPATH, "//*[text()='Создать опрос']")
    SURVEY_CREATE_MODAL = (By.CLASS_NAME, "ModalSidebarPage_container__V2ccs")

    CROSS_BUTTON = (By.XPATH, "//button[@aria-label='close_button']")

    SURVEY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Введите название']")
    SURVEY_COMPANY_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Введите название компании']",
    )
    SURVEY_TITLE_INPUT = (By.XPATH, "//input[@placeholder='Введите заголовок']")
    SURVEY_DESCRIPTION_INPUT = (
        By.XPATH,
        "//textarea[@placeholder='Введите описание опроса']",
    )

    QUESTIONS_BUTTON = (By.XPATH, "(//*[text()='Вопросы'])")

    QUESTION_LIST = (By.XPATH, "//*[contains(@class, 'Question_question')]")

    LOAD_IMAGE_BUTTON = (By.XPATH, "//*[contains(@data-testid, 'set-global-image')]")
    LOAD_IMAGE_INPUT = (By.XPATH,  "//span[text()='Загрузите медиафайлы']")
    LOGO_IN_MEDIA = (By.CSS_SELECTOR, "div[class*='ItemList_item']")
    SAVE_LOGO_BTN = (By.XPATH, '//span[text()="Сохранить"]')
    UPLOADED_IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ItemList_item__')]")
    UPLOADED_IMAGE_NAME = (By.XPATH, "//*[contains(@class, 'ImageItem_name__')]")

    EDIT_IMAGES_BUTTON = (By.XPATH, "//button[contains(@aria-label, 'Edit')]")
    SELECT_ALL_IMAGES_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'EditControl_selection__')]//*[text()='Выбрать все']",
    )

    DELETE_IMAGES_BUTTON = (By.XPATH, "//button[contains(@data-testid, 'delete')]")
    CONFIRM_DELETE_BUTTON = (
        By.XPATH,
        "//*[contains(@class, 'vkuiButton__') and text()='Удалить']",
    )

    CONTINUE_BUTTON = (By.XPATH, "//span[text()='Вопросы']")

    TITLE_INPUT = (By.XPATH, "//input[@placeholder='Введите название']")
    COMPANY_INPUT = (By.XPATH, "//input[@placeholder='Введите название компании']")
    HEADER_INPUT = (By.XPATH, "//input[@placeholder='Введите заголовок']")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Введите описание опроса']")

    ERROR_1_TITLE = (By.XPATH, "(//span[contains(@role, 'alert')])[1]")
    ERROR_1_COMPANY = (By.XPATH, "(//span[contains(@role, 'alert')])[3]")
    ERROR_1_HEADER = (By.XPATH, "(//span[contains(@role, 'alert')])[4]")
    ERROR_1_DESCRIPTION = (By.XPATH, "(//span[contains(@role, 'alert')])[5]")

    QUESTION_TITLE_INPUT = (By.XPATH, "//textarea[@placeholder='Текст вопроса']")
    ANSWER_1_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[1]")
    ANSWER_2_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[2]")
    ANSWER_3_INPUT = (By.XPATH, "(//input[@placeholder='Введите ответ'])[3]")

    ADD_ANSWER_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить вариант')]")
    ADD_QUESTION_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить вопрос')]")

    SELECTOR_INPUT = (
        By.XPATH,
        "//div[contains(@class, 'HintSelector_hintSelectorButton')]",
    )
    SELECTOR_MANY = (By.XPATH, "//span[contains(text(), 'Несколько из списка')]")
    SELECTOR_ANSWER = (By.XPATH, "//span[contains(text(), 'Ответ в свободной форме')]")
    SELECTOR_SCALE = (By.XPATH, "//span[contains(text(), 'Шкала')]")

    ADD_STOP_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить стоп-экран')]")
    STOP_HEADING_INPUT = (By.XPATH, "//input[@placeholder='Введите заголовок']")
    STOP_DESCRIPTION_INPUT = (
        By.XPATH,
        "//input[@placeholder='Введите описание опроса']",
    )

    ERROR_2_QUESTION = (
        By.XPATH,
        "//div[contains(@class, 'vkuiDiv Question_errorFooter')]",
    )

    ADD_LINK_BUTTON = (By.XPATH, "//span[contains(text(), 'Добавить ссылку')]")

    HEADER_3 = (By.XPATH, "//input[@placeholder='Введите заголовок']")
    DESCRIPTION_3 = (
        By.XPATH,
        "//input[@placeholder='Введите описание: например, поблагодарите за прохождение опроса']",
    )
    LINK_3 = (By.XPATH, "//input[@placeholder='Введите ссылку']")

    ERROR_3_HEADER = (By.XPATH, "(//span[contains(@role, 'alert')])[1]")
    ERROR_3_DESCRIPTION = (By.XPATH, "(//span[contains(@role, 'alert')])[2]")
    ERROR_3_LINK = (By.XPATH, "(//span[contains(@role, 'alert')])[1]")

    ARCHIVE_BUTTON = (By.XPATH, "//span[contains(text(), 'Архивировать')]")
    ARCHIVE_ACCEPT_BUTTON = (By.XPATH, "//span[contains(text(), 'Архивировать')]")

    FIRST_SURVAY_NAME = (
        By.XPATH,
        "(//h5[contains(@data-testid, 'lead_form_name__')])[1]",
    )

    UPLOAD_IMAGE_MODAL = (
        By.XPATH,
        "(//div[contains(@class, 'ModalSidebarPage_control')])[2]",
    )

    FIRST_LEAD_FORM_NAME = (
        By.XPATH,
        "(//h5[contains(@data-testid, 'lead_form_name__')])[1]",
    )

    SELECT_ALL_FORMS = (By.XPATH, "(//div[@data-key='checkbox']/input[contains(@class, 'simpleCheckbox_input')][0]")
    SELECT_ACTIONS_BUTTON = (By.XPATH, f'//input[@placeholder="Действия"]')
    DELETE_ACTION = (By.XPATH, "//div[contains(@class, 'vkuiCustomSelectOption__Children')]")