import allure
import pytest

from data import create_payloads

#########################################################

@allure.feature("Memes")
@allure.story("Get api")
@allure.title("Get all memes")
def test_list_of_memes(list_memes_endpoint):
    list_memes_endpoint.do_authorize()
    list_memes_endpoint.get_list_of_memes()
    list_memes_endpoint.check_response_code_is_(200)
    list_memes_endpoint.check_response_is_not_empty()


@allure.feature("Memes")
@allure.story("Get api")
@allure.title("Unauthorized User can not get list of mems")
def test_list_of_memes(list_memes_endpoint):
    list_memes_endpoint.get_list_of_memes()
    list_memes_endpoint.check_response_code_is_(401)

#########################################################

@allure.feature("Memes")
@allure.story("Get by id api")
@allure.title("Get meme by id")
def test_get_meme_by_id(get_meme_by_id_endpoint, mem_id):
    get_meme_by_id_endpoint.do_authorize()
    get_meme_by_id_endpoint.get_meme_by_id(mem_id)
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
def test_get_meme_by_id(get_meme_by_id_endpoint, mem_id):
    get_meme_by_id_endpoint.do_authorize()
    get_meme_by_id_endpoint.get_meme_by_id(mem_id)
    get_meme_by_id_endpoint.check_response_code_is_(404)


@allure.feature("Memes")
@allure.story("Get by id api")
@allure.title("Unauthorized User can not get meme by id")
def test_get_meme_by_id(get_meme_by_id_endpoint, mem_id):
    get_meme_by_id_endpoint.get_meme_by_id(mem_id)
    get_meme_by_id_endpoint.check_response_code_is_(401)

#########################################################

@allure.feature("Memes")
@allure.story("Create a meme")
@allure.title("Post a new meme")
def test_meme_creation(post_meme_endpoint):
    post_meme_endpoint.do_authorize()
    post_meme_endpoint.create_meme()
    post_meme_endpoint.check_response_code_is_(200)
    post_meme_endpoint.check_fields_of_created_meme()


@allure.feature("Memes")
@allure.story("Create a meme")
@allure.title("Unauthorized User can not create a meme")
def test_meme_creation(post_meme_endpoint):
    post_meme_endpoint.create_meme()
    post_meme_endpoint.check_response_code_is_(401)


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
def test_meme_creation(post_meme_endpoint, payload):
    post_meme_endpoint.do_authorize()
    post_meme_endpoint.create_meme(payload)
    post_meme_endpoint.check_response_code_is_(400)

#########################################################

@allure.feature("Memes")
@allure.title("Update a meme")
@allure.step("Update text field for existing meme")
@pytest.mark.parametrize(
    "text", [
        "This is a long text for text field check",
        "",
        "        ",
        None
        ]
)
@allure.step("Update info field for existing meme")
@pytest.mark.parametrize(
    "info", [
        {"colors": "blue", "objects": "some"},
        {"objects": 89898},
        None,
        ]
)
@allure.step("Update url field for existing meme")
@pytest.mark.parametrize(
    "url", [
        "www.onliner.by",
        "         ",
        None,
        ]
)
@allure.step("Update tags field for existing meme")
@pytest.mark.parametrize(
    "tags", [
        ["laugh", "smile"],
        None,
        "         "]
)
def test_update_meme(put_meme_endpoint, mem_id, text, info, tags, url):
    put_meme_endpoint.do_authorize()
    put_meme_endpoint.update_meme(
        {"id": mem_id,
         "text": text,
         "url": url,
         "tags": tags,
         "info": info
    }, mem_id)
    put_meme_endpoint.check_response_code_is_(200)
    put_meme_endpoint.check_response_is_equal_to_payload("text", text)
    put_meme_endpoint.check_response_is_equal_to_payload("url", url)
    put_meme_endpoint.check_response_is_equal_to_payload("tags", tags)
    put_meme_endpoint.check_response_is_equal_to_payload("info", info)

#########################################################

@allure.feature("Memes")
@allure.story("Delete a meme")
@allure.title("Delete an existing meme")
def test_delete_meme(delete_meme_endpoint, mem_id):
    delete_meme_endpoint.do_authorize()
    delete_meme_endpoint.delete_meme(mem_id)
    delete_meme_endpoint.check_response_code_is_(200)


@allure.feature("Memes")
@allure.story("Delete a meme")
@allure.title("User can not delete same meme twice")
def test_delete_meme(delete_meme_endpoint, mem_id):
    delete_meme_endpoint.do_authorize()
    delete_meme_endpoint.delete_meme(mem_id)
    delete_meme_endpoint.check_response_code_is_(200)
    delete_meme_endpoint.delete_meme(mem_id)
    delete_meme_endpoint.delete_meme(404)


@allure.feature("Memes")
@allure.story("Delete a meme")
@allure.title("User can not delete meme with invalid id")
def test_delete_meme(delete_meme_endpoint):
    delete_meme_endpoint.do_authorize()
    delete_meme_endpoint.delete_meme('absbcb')
    delete_meme_endpoint.check_response_code_is_(404)
