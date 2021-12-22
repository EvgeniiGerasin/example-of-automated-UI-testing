from threading import Condition
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

from tools.helper import Screenshot


class BadElementException(Exception):
    """Для вызова в случае если элемент на
    странице не найден
    """

    def __init__(self, message: str):
        """инициализация сообщения

        Args:
        - message (str): описание элемента
        """
        self.message = message


# *********************************************************
class WaitElement:
    """Содержит методы для ожидания элементов страницы
    """
    @staticmethod
    def xpath(driver, locator, timeout) -> None:
        """Waiting for the xpath element
        to appear on the page

        Args:
        - driver (object): instance webdriver
        - locator (str): xpath
        - timeout (int): time to wait for the element 
        (default 10 sec)
        """
        if timeout == None:
            timeout = 10
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        except:
            Screenshot().shot(driver, f'Wait error: {locator}')
            text_exception = f'Wait element: {locator}'
            raise BadElementException(text_exception)

class CastomWait:
    
    CONDITION = True

    @classmethod
    def run(cls, timeout) -> None:
        if cls.CONDITION:
            pass