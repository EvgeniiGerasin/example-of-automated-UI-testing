class Path:

    ROOT_DIR = None
    DOWNLOAD_DIR = None
    DRIVER = './'


class Browser:

    PREFS = {
        'download.default_directory': Path.DOWNLOAD_DIR
    }
    # Запуск тестов локально
    LOCAL = False
    # пути драйверов
    CHROMEDRIVER_PATH = (f'{Path.DRIVER}chromedriver')
    # FIREFOXDRIVER_PATH = (f'{Path.DRIVER}geckodriver')

    # параметры дефолтного браузера
    DEFAULT_BROWSER = 'chrome'
    DEFAULT_VERSION_BROWSER = ''

    # # версии Firefox
    # FIREFOX = 'firefox'
    # FIREFOX_DEFAULT_VERSION = '81.0'

    # версии Chrome
    CHROME = 'chrome'
    CHROME_DEFAULT_VERSION = '80.0'
    # remote
    CAPABILITIES = {
        'browserName': '',
        'browserVersion': '',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': False,
            'name': 'Unknown Name'
        }
    }
    XPATH_LOG = str()


class CommonTestData:

    URL_STAND = 'https://www.saucedemo.com/'
    USERNAMES = (
        'standard_user',
        'locked_out_user',
        'problem_user',
        'performance_glitch_user',
    )
    PASSWORD = 'secret_sauce'
