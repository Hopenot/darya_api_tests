import allure
import requests

from abc import abstractmethod
from requests import Response
from data import test_data
from data.constants import AUTH_URL


class BaseApi:
    response: Response

    def __init__(self):
        self.token = None

    # property привращает результат функции в переменную
    # проверят вычитку респонса
    @property
    def response_json(self):
        return self.response.json()

    @allure.step("Check response status code")
    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    @allure.step('Check response is not empty')
    def check_response_is_not_empty(self):
        assert self.response.json() != {}

    @property
    @abstractmethod
    # означает что во всех подклассах должна быть реализванно
    def data(self):
        pass
