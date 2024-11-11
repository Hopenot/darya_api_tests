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

    @allure.step('Make authorization')
    def make_authorize(self):
        payload = test_data.NAME
        headers = {"Content-Type": 'application/json'}
        response = requests.post(
            f"{AUTH_URL}",
            json=payload,
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        self.token = data["token"]

    @allure.title('Check is token alive')
    def check_if_token_alive(self):
        headers = {"Content-Type": 'application/json'}
        response = requests.get(
            f"{AUTH_URL}/{self.token}",
            headers=headers
        )
        return response.status_code == 200

    @allure.step('Do authorization')
    def do_authorize(self):
        if self.token is not None:
            is_alive_token = self.check_if_token_alive()
            if is_alive_token == True:
                return

        self.make_authorize()

    @allure.step("Check response status code")
    def check_response_code_is_(self, code):
        assert self.response.status_code == code

    # property привращает результат функции в переменную
    # проверят вычитку респонса
    @property
    def response_json(self):
        return self.response.json()

    @allure.step('Check response is not empty')
    def check_response_is_not_empty(self):
        assert self.response.json() != {}

    @property
    @abstractmethod
    # означает что во всех подклассах должна быть реализванно
    def data(self):
        pass
