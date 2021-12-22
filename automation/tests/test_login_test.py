import pytest
import allure

from source.authorization.task import TaskAuthorizationPage
from config.config import CommonTestData


@allure.epic('Authorization')
class TestAutorization:

    @pytest.mark.parametrize(
        'username', CommonTestData.USERNAMES
    )
    @allure.title('Enter "standard_user"')
    def test_authorization(self, web_driver, username):
        with allure.step('Arrange'):
            job = TaskAuthorizationPage(web_driver)
        with allure.step('Act'):
            job.act_loging(username)
        with allure.step('Assert'):
            job.assert_logging()
