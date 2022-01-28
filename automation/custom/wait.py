class CustomWait:

    _condition_1 = True
    _condition_2 = True
    _condition_3 = True

    @classmethod
    def set_wait(cls, **kwargs) -> dict:
        if kwargs:
            for condition, value in kwargs.items():
                if condition == 'condition_1':
                    cls._condition_1 = bool(value)
                if condition == 'condition_2':
                    cls._condition_2 = bool(value)
                if condition == 'condition_3':
                    cls._condition_3 = bool(value)
        return {
            'condition_1': cls._condition_1,
            'condition_2': cls._condition_3,
            'condition_3': cls._condition_3,
        }

    @classmethod
    def set_default_wait(cls) -> dict:
        cls._condition_1 = True
        cls._condition_2 = True
        cls._condition_3 = True
        return {
            'condition_1': cls._condition_1,
            'condition_2': cls._condition_3,
            'condition_3': cls._condition_3,
        }
    
    @classmethod
    def run(cls, driver: object, timeout:float = 10, default: bool = True):
        if cls._condition_1:
            print('run 1')
        if cls._condition_2:
            print('run 2')
        if cls._condition_3:
            print('run 3')
        if default:
            cls.set_default_wait()
