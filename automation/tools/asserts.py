class Asserts:

    def __init__(self, action) -> None:
        self._action = action

    def is_enabled(
        self,
        locator_element: str,
        text_error: str,
        text_scr: str = None
    ) -> None:
        """Проверка статуса доступности элемента

        :Args:
        - locator_element(str): локатор элемента
        - text_error(str): текст ошибки
        - text_scr(str): текст скриншота
        """
        try:
            assert self._action.len_elements(locator_element)[0]
        except:
            assert False, text_error
        finally:
            if text_scr:
                self._action.shot(text_scr)

    def equality(
        self,
        variable_first,
        variable_second,
        text_error: str,
        text_scr: str = None
    ) -> None:
        """Проверка на равенство значений двух полей(одного типа данных)

        :Args:
        - variable_first(any): значение первого поля
        - variable_second(any): значение второго поля
        - text_error(str): текст ошибки
        - text_scr(str): текст скриншота
        """
        try:
            assert variable_first == variable_second
        except:
            assert False, text_error
        finally:
            if text_scr:
                self._action.shot(text_scr)

    def inequality(
        self,
        variable_first,
        variable_second,
        text_error: str,
        text_scr: str = None
    ) -> None:
        """Проверка на неравенство значений двух полей(одного типа данных)

        :Args:
        - variable_first(any): значение первого поля
        - variable_second(any): значение второго поля
        - text_error(str): текст ошибки
        - text_scr(str): текст скриншота
        """
        try:
            assert variable_first != variable_second
        except:
            assert False, text_error
        finally:
            if text_scr:
                self._action.shot(text_scr)

    def count_compration(
        self,
        variable_large,
        variable_smaller,
        text_error: str,
        text_scr: str = None
    ) -> None:
        """Сравнение двух числовых значений

        :Args:
        - variable_large(any): значение большего числа
        - variable_smaller(any): значение меньшего поля
        - text_error(str): текст ошибки
        - text_scr(str): текст скриншота
        """
        try:
            assert variable_large > variable_smaller
        except:
            assert False, text_error
        finally:
            if text_scr:
                self._action.shot(text_scr)

    def contains(
        self,
        variable_what,
        variable_where,
        text_error: str,
        text_scr: str = None
    ) -> None:
        """Проверка содержания в чем либо (a in b)

        :Args:
        - variable_what(any): что должно содержаться
        - variable_where(any): где это должно содержаться
        - text_error(str): текст ошибки
        - text_scr(str): текст скриншота
        """
        try:
            assert variable_what in variable_where
        except:
            assert False, text_error
        finally:
            if text_scr:
                self._action.shot(text_scr)
