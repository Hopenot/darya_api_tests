import requests
from endpoints.base_api import BaseApi
from data.constants import AUTH_URL, HEADERS
from models.authorization import AuthResponse


class AuthRequest(BaseApi):

    def auth_request_endpoint(self, payload):
        self.response = requests.post(f'{AUTH_URL}', json=payload, headers=HEADERS)

    @property
    def data(self):
        return AuthResponse(**self.response_json)
