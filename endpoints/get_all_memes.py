import requests
import allure

from endpoints.base_api import BaseApi
from data.constants import BASE_URL
from models.memes_object import MemesListJson


class GetMemeList(BaseApi):
    @allure.step("Get all memes")
    def get_list_of_memes(self):
        header = {'Authorization': self.token}
        self.response = requests.get(f'{BASE_URL}', headers=header)

    @property
    def data(self):
        return MemesListJson(**self.response_json)

