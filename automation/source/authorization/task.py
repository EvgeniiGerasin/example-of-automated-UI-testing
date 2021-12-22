import allure

from source.authorization import Locator
from config.config import CommonTestData
from tools.helper import Report
from tools.action import ActionCommon
from tools.asserts import Asserts


class BasePage:

    def __init__(self, driver) -> None:

        self.driver = driver
        self.action = ActionCommon(self.driver)
        self.report = Report()
        self.asserts = Asserts(self.action)


class FieldUsername(BasePage):

    @allure.step('Enter username')
    def enter_username(self, text: str):
        self.action.keys(
            locator=Locator.FIELD_USERNAME,
            text=text
        )


class FieldPassword(BasePage):

    @allure.step('Enter password')
    def enter_password(self, text: str):
        self.action.keys(
            locator=Locator.FIELD_PASSWORD,
            text=text
        )


class ButtonLogin(BasePage):

    @allure.step('Push button login')
    def push_login(self):
        self.action.click(
            locator=Locator.BUTTON_LOGIN
        )


class TaskAuthorizationPage(BasePage):

    def __init__(self, driver) -> None:
        driver.implicitly_wait(0.5)
        driver.get(CommonTestData.URL_STAND)
        super().__init__(driver)

    def act_loging(
        self,
        username=CommonTestData.USERNAMES[0],
        password=CommonTestData.PASSWORD,
    ):
        FieldUsername(self.driver).enter_username(
            text=username
        )
        FieldPassword(self.driver).enter_password(
            text=password
        )
        ButtonLogin(self.driver).push_login()

    def assert_logging(self):
        check, _ = self.action.len_elements(
            locator=Locator.LEBEL_ERROR
        )
        try:
            assert check == 0
        except:
            assert False, 'Login error'
        finally:
            self.action.shot('After loging')
