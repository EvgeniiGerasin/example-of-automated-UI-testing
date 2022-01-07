class Logger:

    _TEXT_LOGGER = ''

    @classmethod
    def put_to_logger(cls, text: str):
        cls._TEXT_LOGGER += text + '\n'

    @classmethod
    def get_from_logger(cls) -> str:
        return cls._TEXT_LOGGER
