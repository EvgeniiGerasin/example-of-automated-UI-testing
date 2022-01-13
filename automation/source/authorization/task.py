import allure
from docs.descriptions import BaseDescription

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
        report = BaseDescription.create(
            {
                'stand': CommonTestData.URL_STAND,
                'username': username,
                'password': password
            }
        )
        allure.dynamic.description_html(report)
        FieldUsername(self.driver).enter_username(
            text=username
        )
        FieldPassword(self.driver).enter_password(
            text=password
        )
        ButtonLogin(self.driver).push_login()

    def assert_logging(self):
        self.asserts.is_disenabled(
            Locator.LEBEL_ERROR,
            text_error='Logging error',
            text_scr='Logging scr'
        )
