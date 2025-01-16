import pytest
import requests

from data.constants import AUTH_URL
from endpoints.authorization import AuthRequest
from endpoints.get_all_memes import GetMemeList
from endpoints.get_meme_by_id import GetMemeId
from endpoints.delete_meme import DeleteMeme
from endpoints.create_meme import CreateMeme
from endpoints.token_status import GetAuthTokenStatus
from endpoints.update_meme import UpdateMeme
from data.test_data import NAME, CREATE_MEME

@pytest.fixture(scope='session')
def login(auth_api):
    payload = NAME
    auth_api.auth_request_endpoint(payload)
    return auth_api.data.token

@pytest.fixture(scope='function')
def mem_id(login, post_meme_endpoint, delete_meme_endpoint):
    payload = CREATE_MEME
    post_meme_endpoint.create_meme(login, payload)
    mem_id = post_meme_endpoint.response_json['id']
    yield mem_id
    delete_meme_endpoint.delete_meme(login, mem_id)

@pytest.fixture(scope="session")
def auth_api():
    return AuthRequest()

@pytest.fixture(scope="session")
def get_auth_token_status_api():
    return GetAuthTokenStatus()

@pytest.fixture(scope="session")
def list_memes_endpoint():
    return GetMemeList()

@pytest.fixture(scope="session")
def get_meme_by_id_endpoint():
    return GetMemeId()

@pytest.fixture(scope="session")
def post_meme_endpoint():
    return CreateMeme()

@pytest.fixture(scope="session")
def delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture(scope="session")
def put_meme_endpoint():
    return UpdateMeme()
