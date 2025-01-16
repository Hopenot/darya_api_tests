import requests
import allure

from endpoints.base_api import BaseApi
from data.constants import MEME_POSTFIX, BASE_URL
from models.memes_object import MemeJson


class GetMemeId(BaseApi):
    @allure.step("Get certain meme by id")
    def get_meme_by_id(self, token, mem_id):
        header = {"Authorization": f"{token}"}
        self.response = requests.get(f'{BASE_URL}{MEME_POSTFIX}{mem_id}', headers=header)

    def get_meme_by_id_by_unauthorized_user(self, mem_id):
        self.response = requests.get(f'{BASE_URL}{MEME_POSTFIX}{mem_id}', headers={})

    @allure.step("Check requested meme is returned")
    def check_returned_mem_id_is(self, mem_id):
        assert self.data.id == mem_id

    @allure.step("Check meme is deleted")
    def check_meme_is_deleted(self, mem_id):
        self.get_meme_by_id(mem_id)
        assert self.response.status_code == 404

    @property
    def data(self):
        return MemeJson(**self.response_json)
