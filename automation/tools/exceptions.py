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
