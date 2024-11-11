import requests
import allure

from endpoints.base_api import BaseApi
from data.constants import BASE_URL
from data.test_data import CREATE_MEME
from models.memes_object import MemeJson


class CreateMeme(BaseApi):
    def create_meme(self, payload=None):
        header = {'Authorization': self.token}
        payload = payload if payload else CREATE_MEME
        self.response = requests.post(f'{BASE_URL}', json=payload, headers=header)

    @property
    def data(self):
        return MemeJson(**self.response_json)

    @allure.step('Check fields of created meme')
    def check_fields_of_created_meme(self, payload=None):
        payload = payload if payload else CREATE_MEME
        assert self.data.tags == payload['tags']
        assert self.data.url == payload['url']
        assert self.data.info == payload['info']
        assert self.data.text == payload['text']
