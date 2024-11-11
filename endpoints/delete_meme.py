import requests
import allure

from endpoints.base_api import BaseApi
from data.constants import BASE_URL, MEME_POSTFIX
from models.memes_object import DeleteMemeModel


class DeleteMeme(BaseApi):
    def delete_meme(self, mem_id):
        header = {'Authorization': self.token}
        self.response = requests.delete(f'{BASE_URL}/{MEME_POSTFIX}/{mem_id}', headers=header)

    @property
    def data(self):
        return DeleteMemeModel(**self.response_json)
