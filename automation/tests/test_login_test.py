import pytest
import allure

from source.authorization.task import TaskAuthorizationPage
from config.config import CommonTestData
from docs.links import Links


@allure.epic('Authorization')
class TestAutorization:

    @pytest.mark.parametrize(
        'username', CommonTestData.USERNAMES
    )
    @allure.title('Enter "standard_user"')
    @allure.link(Links.TEST_URL, name='Test case')
    def test_authorization(self, web_driver, username):
        with allure.step('Arrange'):
            job = TaskAuthorizationPage(web_driver)
        with allure.step('Act'):
            job.act_loging(username)
        with allure.step('Assert'):
            job.assert_logging()
