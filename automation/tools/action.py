from time import sleep
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as e

from tools.wait import CastomWait, WaitElement
from config.config import Browser
from tools.logger import Logger



class Action:
    """Содержит методы для применения к объяктам страницы
    """

    def __init__(self, driver) -> None:
        self._driver = driver


class ActionCommon(Action):
    """Действия над элементами страницы Электронной школы
    """

    def click(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> None:
        """Нажатие на элемент

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        Logger.put_to_logger(locator + '\n')
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            self._driver.find_element_by_xpath(locator).click()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='click'
            )

    def click_double(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> None:
        """Двоейное нажатие на элемент

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem = self._driver.find_element_by_xpath(locator)
            action = ActionChains(self._driver)
            action.double_click(elem).perform()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='click double'
            )

    def search(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> list:
        """Поиск на странице группу элементов

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        :Return:
        - result_search (list: object): список найденых на странице объектов
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            result_search: list = self._driver.find_elements(
                By.XPATH, locator
            )
            return result_search
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='search'
            )

    def len_elements(
        self,
        locator: str,
        timeout: int = None,
        element: bool = False,
    ) -> int and list:
        """Функция получает количество найденых элементов. Если
        элементов нет, возвращает [0, None] иначе количество элементов и
        список элементов для взаимодействия

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        :Return:
        -   number_element(int):количество найденых элементов
        - result_search (list: object): список найденых на странице объектов
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            result_search: list[object] = self._driver.find_elements(
                By.XPATH, locator)
            number_elements_search: int = len(result_search)
            if number_elements_search == 0:
                return 0, None
            else:
                return number_elements_search, result_search
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='len elements'
            )

    def text(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> str:
        """Извлечение текста из элемента

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        :Return:
        - text (str): извлеченный текст
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            text = self._driver.find_element_by_xpath(locator).text
            return text
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='text'
            )

    def keys(
        self,
        locator: str,
        text: str,
        timeout: int = None,
        element: bool = True,
    ) -> None:
        """Ввод теста в поле элемента на странице

        :Args:
        - locator (str): Locator элемента
        - text (str): вводимы текст
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - list_ (bool): ожидания загрузки выпадающего списка
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        Logger.put_to_logger(locator + '\n')
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            self._driver.find_element_by_xpath(locator).send_keys(text)
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='keys',
                text=text
            )

    def keys_chains(
        self,
        locator: str,
        text: str,
        timeout: int = None,

        element: bool = True,
    ) -> None:
        """Выделяет поле для ввода, удаляет содержимое и
        вставляет текст

        :Args:
        - locator (str): Locator элемента
        - text (str): вводимы текст
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem = self._driver.find_element_by_xpath(locator)
            chains = ActionChains(self._driver)
            chains.double_click(elem)
            chains.double_click(elem)
            chains.double_click(elem)
            chains.send_keys(Keys.DELETE)
            chains.send_keys(text)
            chains.send_keys(Keys.ENTER)
            chains.perform()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='keys chains',
                text=text
            )

    def click_hold(
        self,
        locator: str,
        time_hold: int,
        timeout: int = None,
        element: bool = True,
    ) -> None:
        """Удерживает нажатие левую кнопку мыши, указанное время

        :Args:
        - locator (str): Locator элемента
        - time_hold (int): время удерживания
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem = self._driver.find_element_by_xpath(locator)
            chains = ActionChains(self._driver)
            chains.click_and_hold(elem)
            chains.pause(time_hold)
            chains.perform()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='click and hold',
                time_hold=time_hold
            )

    def move_to(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> None:
        """Переход к элементу страницы

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem = self._driver.find_element_by_xpath(locator)
            chains = ActionChains(self._driver)
            chains.move_to_element(elem)
            chains.pause(1)
            chains.perform()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='move to'
            )

    def clear(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> None:
        """Очистка поля

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            self._driver.find_element_by_xpath(locator).clear()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='clear'
            )

    def get_attribute(
        self,
        locator: str,
        attribute: str,
        timeout: int = None,
        element: bool = True,
    ) -> str:
        """Очистка поля

        :Args:
        - locator (str): Locator элемента
        - attribute (str): атрибут
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        :Return:
        - text (str): извлеченный текст
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            text_atr: str = self._driver.find_element_by_xpath(
                locator
            ).get_attribute(attribute)
            return text_atr
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='get attribute',
                attribute=attribute
            )

    def is_selected(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> bool:
        """Получение выбран ли элемент

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        Returns:
        - bool: True or False
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem: object = self._driver.find_element_by_xpath(
                locator
            )
            return elem.is_selected()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='is selected'
            )

    def is_enabled(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> bool:
        """Получение статуса доступности элемента

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        Returns:
        - bool: True or False
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem: object = self._driver.find_element_by_xpath(
                locator
            )
            return elem.is_enabled()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='is enabled'
            )

    def get_element_object(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> bool:
        """Получение статуса доступности элемента

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        Returns:
        - bool: True or False
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            return self._driver.find_element_by_xpath(locator)
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='get element object'
            )

    def shot(self, description: str, delay: float = None):
        """Метод для генерации скриншота в отчет. Как для ошибки,
        так и для правильного результата

        Args:
        - description (str): описание для имени сриншота.
        - delay (float): задержка перед скриншотом
        """
        if delay:
            sleep(delay)
        scr = self._driver.get_screenshot_as_png()
        allure.attach(
            body=scr,
            name=f'{description}',
            attachment_type=allure.attachment_type.PNG
        )

    def scroll(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    )-> None:
        """Метод для скролинга страницы вправо
        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:    
            self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            horizontal_bar_width = self._driver.find_element_by_xpath(locator).rect['width']
            slider = self._driver.find_element_by_xpath(locator)
            ActionChains(self._driver).click_and_hold(slider).move_by_offset(horizontal_bar_width, 0).release().perform()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='scroll'
            )    

    def is_displayed(
        self,
        locator: str,
        timeout: int = None,
        element: bool = True,
    ) -> bool:
        """Получение ифнормации о видимости элемента для пользователя

        :Args:
        - locator (str): Locator элемента
        - timeout (int): время ожидания
        - loading (bool): ожидания загрузки
        - mask (bool): ожидания пропадания маски
        - element (bool): ожидания ожидания элемента по Locatorу

        Returns:
        - bool: True or False
        """
        CastomWait.run(timeout)
        if element:
            WaitElement.xpath(self._driver, locator, timeout)
        try:
            elem: object = self._driver.find_element_by_xpath(
                locator
            )
            return elem.is_displayed()
        except:
            ExceptionHandler(self._driver)._retry_action(
                locator=locator,
                action='is displayed'
            )

class ExceptionHandler(Action):

    def _retry_action(
        self, locator: str,
        action: str,
        text: str = None,
        time_hold: int = None,
        attribute: str = None,
    ):

        sleep(2)
        try:
            if action == 'click':
                self._driver.find_element_by_xpath(locator).click()
            elif action == 'click double':
                elem = self._driver.find_element_by_xpath(locator)
                action = ActionChains(self._driver)
                action.double_click(elem).perform()
            elif action == 'search':
                result_search: list = self._driver.find_elements(
                    By.XPATH, locator
                )
                return result_search
            elif action == 'len elements':
                result_search: list[object] = self._driver.find_elements(
                    By.XPATH, locator)
                number_elements_search: int = len(result_search)
                if number_elements_search == 0:
                    return None, None
                else:
                    return number_elements_search, result_search
            elif action == 'text':
                text = self._driver.find_element_by_xpath(locator).text
                return text
            elif action == 'keys':
                self._driver.find_element_by_xpath(locator).send_keys(text)
            elif action == 'keys chains':
                elem = self._driver.find_element_by_xpath(locator)
                chains = ActionChains(self._driver)
                chains.double_click(elem)
                chains.double_click(elem)
                chains.double_click(elem)
                chains.send_keys(Keys.DELETE)
                chains.send_keys(text)
                chains.send_keys(Keys.ENTER)
                chains.perform()
            elif action == 'click and hold':
                elem = self._driver.find_element_by_xpath(locator)
                chains = ActionChains(self._driver)
                chains.click_and_hold(elem)
                chains.pause(time_hold)
                chains.perform()
            elif action == 'move to':
                elem = self._driver.find_element_by_xpath(locator)
                chains = ActionChains(self._driver)
                chains.move_to_element(elem)
                chains.pause(1)
                chains.perform()
            elif action == 'clear':
                self._driver.find_element_by_xpath(locator).clear()
            elif action == 'get attribute':
                text_atr: str = self._driver.find_element_by_xpath(
                    locator
                ).get_attribute(attribute)
                return text_atr
            elif action == 'is selected':
                elem: object = self._driver.find_element_by_xpath(
                    locator
                )
                return elem.is_selected()
            elif action == 'is enabled':
                elem: object = self._driver.find_element_by_xpath(
                    locator
                )
                return elem.is_enabled()
            elif action == 'is displayed':
                elem: object = self._driver.find_element_by_xpath(
                    locator
                )
                return elem.is_displayed()                
            elif action == 'get element object':
                return self._driver.find_element_by_xpath(locator)
            elif action == 'scroll':
                self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                horizontal_bar_width = self._driver.find_element_by_xpath(locator).rect['width']
                slider = self._driver.find_element_by_xpath(locator)
                ActionChains(self._driver).click_and_hold(slider).move_by_offset(horizontal_bar_width/2, 0).release().perform()       
        except e.ElementClickInterceptedException as error:
            raise e.ElementClickInterceptedException(
                msg=f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.ElementNotInteractableException as error:
            raise e.ElementNotInteractableException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.ElementNotSelectableException as error:
            raise e.ElementNotSelectableException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.ElementNotVisibleException as error:
            raise e.ElementNotVisibleException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.ImeActivationFailedException as error:
            raise e.ImeActivationFailedException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.ImeNotAvailableException as error:
            raise e.ImeNotAvailableException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InsecureCertificateException as error:
            raise e.InsecureCertificateException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidArgumentException as error:
            raise e.InvalidArgumentException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidCookieDomainException as error:
            raise e.InvalidCookieDomainException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidCoordinatesException as error:
            raise e.InvalidCoordinatesException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidElementStateException as error:
            raise e.InvalidElementStateException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidSelectorException as error:
            raise e.InvalidSelectorException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidSwitchToTargetException as error:
            raise e.InvalidSwitchToTargetException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.InvalidSessionIdException as error:
            raise e.InvalidSessionIdException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.JavascriptException as error:
            raise e.JavascriptException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.MoveTargetOutOfBoundsException as error:
            raise e.MoveTargetOutOfBoundsException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.NoAlertPresentException as error:
            raise e.NoAlertPresentException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.NoSuchCookieException as error:
            raise e.NoSuchCookieException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.NoSuchElementException as error:
            raise e.NoSuchElementException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.NoSuchFrameException as error:
            raise e.NoSuchFrameException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.NoSuchWindowException as error:
            raise e.NoSuchWindowException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.RemoteDriverServerException as error:
            raise e.RemoteDriverServerException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.ScreenshotException as error:
            raise e.ScreenshotException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.SessionNotCreatedException as error:
            raise e.SessionNotCreatedException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.NoSuchWindowException as error:
            raise e.NoSuchWindowException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.StaleElementReferenceException as error:
            raise e.StaleElementReferenceException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.UnableToSetCookieException as error:
            raise e.UnableToSetCookieException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.TimeoutException as error:
            raise e.TimeoutException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.UnexpectedAlertPresentException as error:
            raise e.UnexpectedAlertPresentException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.UnexpectedTagNameException as error:
            raise e.UnexpectedTagNameException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.UnknownMethodException as error:
            raise e.UnknownMethodException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
        except e.WebDriverException as error:
            raise e.WebDriverException(
                f'Locator: {locator} | {error.msg}', stacktrace=error.stacktrace
            )
