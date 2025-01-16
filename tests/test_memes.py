import allure
import pytest

from data import create_payloads

#########################################################

@allure.feature("Memes")
@allure.story("Get api")
@allure.title("Get all memes")
def test_get_list_of_memes(login, list_memes_endpoint):
    list_memes_endpoint.get_list_of_memes(login)
    list_memes_endpoint.check_response_code_is_(200)
    list_memes_endpoint.check_response_is_not_empty()

#########################################################

@allure.feature("Memes")
@allure.story("Get by id api")
@allure.title("Get meme by id")
def test_get_meme_by_id(login, get_meme_by_id_endpoint, mem_id):
    get_meme_by_id_endpoint.get_meme_by_id(login, mem_id)
    get_meme_by_id_endpoint.check_response_code_is_(200)
    get_meme_by_id_endpoint.check_returned_mem_id_is(mem_id)


@pytest.mark.parametrize(
        "mem_id",
        [
            None,
            'letter',
            1289878
        ]
    )
@allure.feature("Memes")
@allure.story("Get by id api")
@allure.title("Error is returned for requesting invalid mem id")
def test_response_for_invalid_meme_by_id(login, get_meme_by_id_endpoint, mem_id):
    get_meme_by_id_endpoint.get_meme_by_id(login, mem_id)
    get_meme_by_id_endpoint.check_response_code_is_(404)


@allure.feature("Memes")
@allure.story("Create a meme")
@allure.title("Post a new meme")
def test_create_a_meme(login, post_meme_endpoint):
    post_meme_endpoint.create_meme(login)
    post_meme_endpoint.check_response_code_is_(200)
    post_meme_endpoint.check_fields_of_created_meme()


@pytest.mark.parametrize(
        "payload",
        [
            create_payloads.PAYLOAD_WITHOUT_URL,
            create_payloads.PAYLOAD_WITHOUT_INFO,
            create_payloads.PAYLOAD_WITHOUT_TAGS,
            create_payloads.PAYLOAD_WITHOUT_TEXT
        ]
    )
@allure.feature("Memes")
@allure.story("Create a meme")
@allure.title("Mem is not created if required fields are missing")
def test_fields_validation_error_for_meme_creation(login, post_meme_endpoint, payload):
    post_meme_endpoint.create_meme(login, payload)
    post_meme_endpoint.check_response_code_is_(400)

#########################################################

@allure.feature("Memes")
@allure.title("Update a meme")
@allure.step("Update text field for existing meme")
@pytest.mark.parametrize(
    "text", [
        "This is a long text for text field check"
        ]
)
@allure.step("Update info field for existing meme")
@pytest.mark.parametrize(
    "info", [
        {"colors": "blue", "objects": "some"},
        {"objects": 89898}
        ]
)
@allure.step("Update url field for existing meme")
@pytest.mark.parametrize(
    "url", [
        "www.onliner.by"
        ]
)
@allure.step("Update tags field for existing meme")
@pytest.mark.parametrize(
    "tags", [
        ["laugh", "smile"]]
)
def test_update_meme(login, put_meme_endpoint, mem_id, text, info, tags, url):
    put_meme_endpoint.update_meme(login, mem_id,
        {"id": mem_id,
         "text": text,
         "url": url,
         "tags": tags,
         "info": info
    })
    put_meme_endpoint.check_response_code_is_(200)
    put_meme_endpoint.check_response_is_equal_to_payload("text", text)
    put_meme_endpoint.check_response_is_equal_to_payload("url", url)
    put_meme_endpoint.check_response_is_equal_to_payload("tags", tags)
    put_meme_endpoint.check_response_is_equal_to_payload("info", info)

#########################################################

@allure.feature("Memes")
@allure.story("Delete a meme")
@allure.title("Delete an existing meme")
def test_delete_meme(login, delete_meme_endpoint, get_meme_by_id_endpoint, mem_id):
    delete_meme_endpoint.delete_meme(login, mem_id)
    delete_meme_endpoint.check_response_code_is_(200)
    get_meme_by_id_endpoint.get_meme_by_id(login, mem_id)
    get_meme_by_id_endpoint.check_response_code_is_(404)


@allure.feature("Memes")
@allure.story("Delete a meme")
@allure.title("User can not delete same meme twice")
def test_meme_can_not_be_deleted_twice(delete_meme_endpoint, login, mem_id):
    delete_meme_endpoint.delete_meme(login, mem_id)
    delete_meme_endpoint.check_response_code_is_(200)
    delete_meme_endpoint.delete_meme(login, mem_id)
    delete_meme_endpoint.check_response_code_is_(404)


@allure.feature("Memes")
@allure.story("Delete a meme")
@allure.title("User can not delete meme with invalid id")
def test_meme_with_invalid_id_is_not_deleted(delete_meme_endpoint, login):
    delete_meme_endpoint.delete_meme(login, 'absbcb')
    delete_meme_endpoint.check_response_code_is_(404)
