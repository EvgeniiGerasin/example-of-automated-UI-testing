import traceback

class Logger:

    _TEXT_LOGGER = ''

    @classmethod
    def put_to_logger(cls, text: str):
        a = traceback.format_stack(limit=3)[0]
        cls._TEXT_LOGGER += text + '\n' + '\t' + a + '\n'

    @classmethod
    def get_from_logger(cls) -> str:
        return cls._TEXT_LOGGER
