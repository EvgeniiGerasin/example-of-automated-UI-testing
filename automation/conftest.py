from pytest import fixture, UsageError
import allure

from tools.helper import Screenshot
from tools.driver import BrowserSelect
from config.config import Browser
from config.config import CommonTestData
from tools.logger import Logger


def pytest_addoption(parser):
    """Parser command line args
    """
    parser.addoption(
        '--browser_version',
        action='store',
        default=Browser.DEFAULT_VERSION_BROWSER,
        help="Choose version"
    )
    parser.addoption(
        '--local',
        action='store',
        default="False",
        help="Choose how perform tests"
    )
    parser.addoption(
        '--stand',
        action='store',
        default=CommonTestData.URL_STAND
    )


@fixture(scope='function')
def web_driver(request) -> object:
    # get command line args
    browser_version = request.config.getoption("browser_version")
    local_perform = request.config.getoption("local")
    CommonTestData.URL_STAND = request.config.getoption("stand")
    # check local run
    if local_perform == "False":
        local_perform = False
    elif local_perform == "True":
        local_perform = True
    else:
        raise UsageError("--local should be True or False")

    # getting instance webdriver
    capabilities = Browser.CAPABILITIES
    capabilities['name'] = request.node.nodeid
    driver = BrowserSelect(
        local=local_perform,
        browser_version=browser_version
    ).get_driver(capabilities)
    # set time response from server
    driver.set_page_load_timeout(25)
    # set max size windows browser
    driver.maximize_window()
    yield driver
    # screenshot of the screen before finishing work
    Screenshot().shot(driver, 'Окно после завершения теста')
    # logging
    allure.attach(
        Logger.get_from_logger(),
        'logs',
        allure.attachment_type.TEXT
    )
    # closing connection
    driver.quit()
