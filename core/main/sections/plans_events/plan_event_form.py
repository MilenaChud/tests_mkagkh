import time
from selenium.webdriver.common.by import By
from core.helpers.app_sections_helper import AppSectionsHelper


class PlansEventsForm(AppSectionsHelper):
    TITLE = (By.XPATH, "//h1[contains(text(), 'Планы мероприятий по устранению последствий аварий и инцидентов')]")
    BUTTON_ADD = (By.XPATH, "//span[contains(text(), 'Добавить')]/parent::button")
    TITLE_CARD = (By.XPATH, "//h1[contains(text(), 'Карточка учета информации о планах мероприятий')]")
    BUTTON_EVENT = (By.XPATH, "//label[contains(text(), 'Событие')]/..//span[2]")
    TITLE_CHOOSE_EVENT = (By.XPATH, "//h6[contains(text(), 'Выбор события')]")
    CARDS = (By.XPATH, "//div[@class='solo_event_data_block__Header description']")
    EVENT = (By.XPATH, "//label[contains(text(), 'Событие')]/..//input")
    BUTTON_FILL = (By.XPATH,
                   "//h1[contains(text(), 'Карточка учета информации о планах мероприятий')]/../..//span[contains(text(), 'Заполнить на основе типового')]")
    FILL_SAME = (By.XPATH, "//div[contains(text(), 'Наименование мероприятия')]/div")

    CANCEL = (By.XPATH, "//span[contains(text(), 'Отмена')]")
    CURRENT_STATUS = (By.XPATH,
                      "//label[contains(text(), 'Текущий статус проведения мероприятия')]/..//div[@id='mui-component-select-type']")
    TYPE_STATUS = (By.XPATH, "//div[@id='menu-type']//li")
    BUTTON_ADD_SIS = (By.XPATH, "//span[contains(text(), 'Добавить СиС')]")
    SIS = (By.XPATH, "//label[contains(text(), 'Подразделения')]/..//div[@aria-haspopup='listbox']")
    TYPE_SIS = (By.XPATH, "//div[@id='menu-']//li")
    NAME_LIST = (By.XPATH, "//label[contains(text(), 'Наименование')]//..//div[@aria-haspopup='listbox']")
    BACK = (By.XPATH, "//span[contains(text(), 'Назад')]")
    CONFIRM_BACK = (By.XPATH, "//h2[contains(text(), 'Вы собираетесь покинуть страницу. Внесенные изменения не будут сохранены')]")
    GO_OUT_BUTTON = (By.XPATH, "//span[contains(text(), 'Уйти со страницы')]/parent::button")
    BUTTON_NEXT = (By.XPATH, "//span[contains(text(), 'Далее')]")
    ROW_TABLE = (By.XPATH, "//div[contains(text(), 'Состав мероприятия *')]/../../..//td[2]")
    ROW_TABLE_1 = (By.XPATH, "//div[contains(text(), 'Состав мероприятия *')]/../../..//td[2]/div")
    EDITE_WINDOW = (By.XPATH, "//h2[contains(text(), 'Редактировать ')]")
    CURRENT_STATUS_EVENT = (By.XPATH, "//label[contains(text(), 'Текущий статус проведения')]/..//select")
    TITLE_MAIN_PEOPLE = (By.XPATH, "//div[contains(text(), 'Ответственные лица')]")
    BUTTON_SAVE = (By.XPATH, "//div[@id='form-dialog-title']/..//span[contains(text(), 'Сохранить')]")
    MAIN_PEOPLE = (By.XPATH, "//h6[contains(text(), 'Ответственные лица')]/../..//select")
    TITLE_EMPLOYERS = (By.XPATH, "//div[contains(text(), 'Выберите сотрудника')]")
    FUNCTION = (By.XPATH, "//div[contains(text(), 'Выберите сотрудника')]/../../..//tbody//td[1]")
    CLOSE = (By.XPATH, "//h6[contains(text(), 'Ответственные лица')]/..//span[@class='MuiTouchRipple-root']")
    SAVE_CARD = (By.XPATH, "//div[@class='buttons-container']//span[contains(text(), 'Сохранить')]")
    NAME_EVENT = (By.XPATH, "//label[contains(text(), 'Наименование мероприятия')]/..//input")
    SOURCES_FINANCE = (By.XPATH, "//label[contains(text(), 'Источники финансирования')]/..//input")
    PRICE_PROJECT = (By.XPATH, "//label[contains(text(), 'Стоимость работ, тыс.руб.')]/..//input")
    PERIOD = (By.XPATH, "//label[contains(text(), 'Плановый срок проведения мероприятия')]/..//input")
    TYPE_PLAN = (By.XPATH, "//label[contains(text(), 'Тип плана мероприятия')]/..//input")
    RESULT_TABLE = (By.XPATH, "//div[contains(text(), 'Ответственные лица')]/../../..//td[2]")
    BUTTON_EDITE = (By.XPATH, "//span[contains(text(), 'Редактировать')]/parent::button")
    TITLE_EXTRA_FILES = (By.XPATH, "//h3[contains(text(), 'Дополнительные файлы')]")
    FILE_INPUT = (By.XPATH, "//label[@class='dzu-inputLabel']//input")
    ADDED_FILES = (By.XPATH, "//button[@class='RenderAttachment_onRemoveButton__ZvKOU']")
    ALARM_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заполните все обязательные поля')]")
    ALARM_MESSAGE_EXTRA = (By.XPATH, "//span[contains(text(), 'Должен быть хотя бы ответственный!')]")
    TAB = (By.XPATH, "//span[contains(text(), 'Описание мероприятий')]")
    BUTTON_BACK = (By.XPATH, "//form[@id='eventSchedule']//span[contains(text(), 'Назад')]/parent::button")
    FILES = (By.XPATH, "//span[contains(text(), 'Файлы')]")
    EMPTY_FIELD = (By.XPATH, "//div[contains(text(), 'Для загрузки файла перетащите его в эту область')]")

    def _fill_plans(self, template: dict, save: bool = False):
        self._check_element_visible(locator=self.BUTTON_ADD)
        self._click_element(locator=self.BUTTON_ADD)
        self._check_element_visible(locator=self.TITLE_CARD)
        self._click_element(locator=self.BUTTON_EVENT)
        self._check_element_visible(locator=self.TITLE_CHOOSE_EVENT)
        cards = self._find_elements_visible(locator=self.CARDS)
        card = self._get_element_by_text(elements=cards, text=template['TypeEvents'], strict_mode=True)
        self._click_webelement(element=card)
        self._click_element(locator=self.BUTTON_FILL)
        cards = self._find_elements_visible(locator=self.FILL_SAME)
        card = self._get_element_by_text(elements=cards, text=template['TypeEvents'], strict_mode=True)
        self._click_webelement(element=card)
        self._check_element_clickable(locator=self.CURRENT_STATUS)
        self._click_element(locator=self.CURRENT_STATUS)
        elements = self._find_elements_visible(locator=self.TYPE_STATUS)
        element = self._get_element_by_text(elements=elements, text=template["TypeStatus"])
        self._click_webelement(element=element)
        # self._click_element(locator=self.BUTTON_ADD_SIS)
        # self._check_element_clickable(locator=self.SIS)
        # self._click_element(locator=self.SIS)
        # elements = self._find_elements_visible(locator=self.TYPE_SIS)
        # element = self._get_element_by_text(elements=elements, text=template["TypeSIS"])
        # self._click_webelement(element=element)
        # self._check_element_clickable(locator=self.NAME_LIST)
        # self._click_element(locator=self.NAME_LIST)
        # elements = self._find_elements_visible(locator=self.TYPE_SIS)
        # element = self._get_element_by_text(elements=elements, text=template["Crew"])
        # self._click_webelement(element=element)
        # self._click_element(locator=self.BUTTON_SAVE)
        self._press_keyboard_key(key="PAGE DOWN")
        self._click_element(locator=self.ROW_TABLE_1)
        self._check_element_visible(locator=self.EDITE_WINDOW)
        elements = self._find_element(self.CURRENT_STATUS_EVENT)
        self._select_option_by_text(selector=elements, text=template["CurrentStatus"])
        self._click_element(locator=self.BUTTON_SAVE)
        if save:
            self._click_element(self.SAVE_CARD)
            self._check_element_visible(locator=self.ALARM_MESSAGE)
            self._click_element(locator=self.BUTTON_NEXT)
            self._check_element_visible(locator=self.ALARM_MESSAGE_EXTRA)
        else:
            self._click_element(locator=self.CANCEL)
            self._check_element_visible(locator=self.EMPTY_FIELD)
            self._click_element(locator=self.GO_OUT_BUTTON)
            self._check_element_visible(locator=self.TITLE)

    def _check_describe_events(self, template: dict):
        row = self._find_element(locator=self.RESULT_TABLE)
        assert row.text == template['Function']
        time.sleep(1)
        self._click_element(locator=self.BUTTON_BACK)
        self._check_element_value(locator=self.EVENT, value=template['FullEvent'])
        self._check_element_value(locator=self.NAME_EVENT, value=template['TypeEvents'])
        self._check_element_value(locator=self.SOURCES_FINANCE, value=template['SourcesFinance'])
        self._check_element_value(locator=self.PRICE_PROJECT, value=template['PriceProject'])
        self._check_element_value(locator=self.TYPE_PLAN, value=template['TypePlan'])
        row = self._find_element(locator=self.ROW_TABLE)
        assert row.text == template['CompoundEvent']

    def _fill_extra_information(self, template: dict):
        time.sleep(1)
        self._click_element(locator=self.BUTTON_ADD)
        self._check_element_visible(locator=self.TITLE_MAIN_PEOPLE)
        elements = self._find_element(self.MAIN_PEOPLE)
        self._select_option_by_text(selector=elements, text=template["Organization"])
        self._check_element_visible(locator=self.TITLE_EMPLOYERS)
        elements_1 = self._find_elements_visible(locator=self.FUNCTION)
        self._click_element(locator=self.CLOSE)
        for i in range(len(elements_1)):
            FUNCTION = (
            By.XPATH, f"//div[contains(text(), 'Выберите сотрудника')]/../../..//tbody/tr[{i + 1}]/td[{i + 1}]")
            self._click_element(locator=self.BUTTON_ADD)
            self._check_element_visible(locator=self.TITLE_MAIN_PEOPLE)
            elements_2 = self._find_element(self.MAIN_PEOPLE)
            self._select_option_by_text(selector=elements_2, text=template["Organization"])
            self._check_element_visible(locator=self.TITLE_EMPLOYERS)
            self._click_element(locator=FUNCTION)
        self._click_element(self.SAVE_CARD)

    def _upload_files(self, filename: str, save: bool = True):
        self._click_element(locator=self.FILES)
        self._check_element_visible(locator=self.TITLE_EXTRA_FILES)
        self._click_element(locator=self.BUTTON_EDITE)
        file_input = self._find_element(locator=self.FILE_INPUT)  # Поговорить про нужность файла event_tabs_common,
        # его можно убрать и вынести все в app_section_helper
        file_input.send_keys(filename)
        time.sleep(1)
        self._press_keyboard_key(key="PAGE DOWN")
        if save:
            self._click_element(locator=self.SAVE_CARD)
            assert self._find_elements_visible(locator=self.ADDED_FILES)
        else:
            self._click_element(locator=self.CANCEL)
            self._click_element(locator=self.BACK)

    def _edite_card(self, template: dict):
        self._click_element(locator=self.TAB)
        self._click_element(locator=self.BUTTON_EDITE)
        source_finance = self._find_element(locator=self.SOURCES_FINANCE)
        self._click_webelement(element=source_finance)
        self._press_keyboard_key(key="CTRL + A, DEL")
        source_finance.send_keys(template["SourcesFinanceCh"])
        price_project = self._find_element(locator=self.PRICE_PROJECT)
        self._click_webelement(element=price_project)
        self._press_keyboard_key(key="CTRL + A, DEL")
        price_project.send_keys(template["PriceProjectCh"])
        self._click_element(self.SAVE_CARD)
        self._check_element_value(locator=self.SOURCES_FINANCE, value=template['SourcesFinanceCh'])
        self._check_element_value(locator=self.PRICE_PROJECT, value=template['PriceProjectCh'])
