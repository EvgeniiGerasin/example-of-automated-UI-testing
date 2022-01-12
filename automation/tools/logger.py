import traceback
import time


class Logger:

    _TEXT_LOGGER = ''
    _COUNTER = 0
    _TIME_START = time.time()
    _TIME = 0

    @classmethod
    def setup_logger(cls):
        cls._TEXT_LOGGER = ''
        cls._COUNTER = 0
        cls._TIME_START = time.time()

    @classmethod
    def put_to_logger(cls, text: str):
        a = traceback.format_stack(limit=3)[0]
        cls._TEXT_LOGGER += text + '\n' + '\t' + a + '\n'

    @classmethod
    def get_from_logger(cls) -> str:
        return cls._TEXT_LOGGER

    @classmethod
    def record(cls, text: str = '', **kwargs):
        traceback = cls._get_traceback()
        action_type = traceback[2].split(' ')[7].rstrip()
        TIME = round((time.time() - cls._TIME_START), 2)
        cls._COUNTER += 1
        cls._TEXT_LOGGER += (
            f'<{cls._COUNTER}><time {TIME} s>-------------------\n\n'
        )
        cls._TEXT_LOGGER += 'action -> ' + action_type + '\n'
        if 'data' in kwargs:  # check data field
            cls._TEXT_LOGGER += 'data -> ' + kwargs['data'] + '\n'
        cls._TEXT_LOGGER += 'description -> ' + text + '\n\n'
        cls._TEXT_LOGGER += 'traceback -> ' + cls._get_traceback()[1]
        cls._TEXT_LOGGER += '\n'

    @staticmethod
    def _get_traceback() -> str:
        return traceback.format_stack(limit=5)
