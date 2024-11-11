import pytest
import requests

from data.constants import AUTH_URL
from endpoints.get_all_memes import GetMemeList
from endpoints.get_meme_by_id import GetMemeId
from endpoints.delete_meme import DeleteMeme
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from data.test_data import NAME, CREATE_MEME


@pytest.fixture(scope='function')
def mem_id(post_meme_endpoint, delete_meme_endpoint):
    post_meme_endpoint.do_authorize()
    post_meme_endpoint.create_meme(CREATE_MEME)
    mem_id = post_meme_endpoint.response_json['id']
    yield mem_id
    delete_meme_endpoint.delete_meme(mem_id)

@pytest.fixture()
def list_memes_endpoint():
    return GetMemeList()

@pytest.fixture()
def get_meme_by_id_endpoint():
    return GetMemeId()

@pytest.fixture()
def post_meme_endpoint():
    return CreateMeme()

@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture()
def put_meme_endpoint():
    return UpdateMeme()

@pytest.fixture(scope="session")
def authorize():
    payload = NAME
    headers = {"Content-Type": 'application/json'}
    response = requests.post(
        f'{AUTH_URL}',
        json=payload,
        headers=headers
    )
    data = response.json()
    my_token = data["token"]
    print(f"Received token: {my_token}")
    return my_token
