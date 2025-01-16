import requests
import allure

from endpoints.base_api import BaseApi
from data.constants import BASE_URL, MEME_POSTFIX
from models.memes_object import MemesListJson
from data.test_data import CREATE_MEME


class UpdateMeme(BaseApi):
    def update_meme(self, token, mem_id, payload):
        header = {"Authorization": f"{token}"}
        self.response = requests.put(f'{BASE_URL}{MEME_POSTFIX}{mem_id}', json=payload, headers=header)

    @property
    def data(self):
        return MemesListJson(**self.response_json)

    @allure.step('Check response is equal to payload for update')
    def check_response_is_equal_to_payload(self, field, value):
        assert self.response_json[field] == value
