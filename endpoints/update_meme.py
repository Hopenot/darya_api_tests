import requests
import allure

from endpoints.base_api import BaseApi
from data.constants import BASE_URL, MEME_POSTFIX
from models.memes_object import MemesListJson


class UpdateMeme(BaseApi):
    def update_meme(self, payload, mem_id):
        header = {'Authorization': self.token}
        self.response = requests.put(f'{BASE_URL}{MEME_POSTFIX}{mem_id}', json=payload, headers=header)

    @property
    def data(self):
        return MemesListJson(**self.response_json)

    @allure.step('Check response is equal to payload for update')
    def check_response_is_equal_to_payload(self, field, value):
        assert self.response_json[field] == value
