class BaseException(Exception):
    """Базовый класс для исключений
    """
    pass


class InvalidTestConditionsException(BaseException):
    """Вызов исключений при некорректном состоянии системы
    """

    def __init__(self, message):
        """Исключение для систуации, когда система находится
        в некорректном состоянии

        Args:
            message (str): текст исключения
        """
        self.message = message

    def __str__(self):
        return self.message


class BadElementException(BaseException):
    """Для вызова в случае если элемент на
    странице не найден
    """

    def __init__(self, message: str):
        """инициализация сообщения

        Args:
        - message (str): описание элемента
        """
        self.message = message

    def __str__(self):
        return self.message
