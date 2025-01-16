import allure
import pytest

#########################################################

@allure.feature("Memes")
@allure.story("Get api")
@allure.title("Unauthorized User can not get list of mems")
def test_unauthorized_user_does_not_get_memes(list_memes_endpoint):
    list_memes_endpoint.get_list_of_memes_by_unauthorized_user()
    list_memes_endpoint.check_response_code_is_(401)

#########################################################

@allure.feature("Memes")
@allure.story("Get by id api")
@allure.title("Unauthorized User can not get meme by id")
def test_unauthorized_user_does_not_get_meme_by_id(get_meme_by_id_endpoint, mem_id):
    get_meme_by_id_endpoint.get_meme_by_id_by_unauthorized_user(mem_id)
    get_meme_by_id_endpoint.check_response_code_is_(401)

#########################################################

@allure.feature("Memes")
@allure.story("Create a meme")
@allure.title("Unauthorized User can not create a meme")
def test_meme_is_not_created_by_unauthorized_user(post_meme_endpoint):
    post_meme_endpoint.create_meme_as_unauthorized_user()
    post_meme_endpoint.check_response_code_is_(401)
