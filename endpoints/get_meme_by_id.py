import requests
import allure


from endpoints.base_api import BaseApi
from data.constants import MEME_POSTFIX, BASE_URL
from models.memes_object import MemeJson


class GetMemeId(BaseApi):
    @allure.step("Get certain meme by id")
    def get_meme_by_id(self, mem_id):
        header = {'Authorization': self.token}
        self.response = requests.get(f'{BASE_URL}{MEME_POSTFIX}{mem_id}', headers=header)

    @allure.step("Check requested meme is returned")
    def check_returned_mem_id_is(self, mem_id):
        assert self.data.id == mem_id

    @property
    def data(self):
        return MemeJson(**self.response_json)

