import requests
from endpoints.base_api import BaseApi
from data.constants import AUTH_URL, HEADERS
from models.memes_object import MemeJson


class GetAuthTokenStatus(BaseApi):

    def get_auth_token_status(self, token):
        self.response = requests.get(f'{AUTH_URL}/{token}', headers=HEADERS)

    @property
    def data(self):
        return MemeJson(**self.response_json)

    def check_token(self):
        assert self.response.text == 'Token is alive. Username is Dasha'
