import allure
import pytest

#########################################################

@allure.feature("Memes")
@allure.title("Update a meme")
@allure.step("Update text field for existing meme with invalid data")
@pytest.mark.parametrize(
    "text", [
        "",
        "        ",
        None
        ]
)
@allure.step("Update info field for existing meme with invalid data")
@pytest.mark.parametrize(
    "info", [
        None
        ]
)
@allure.step("Update url field for existing meme with invalid data")
@pytest.mark.parametrize(
    "url", [
        "         ",
        None,
        ]
)
@allure.step("Update tags field for existing meme with invalid data")
@pytest.mark.parametrize(
    "tags", [
        None,
        "         "]
)
def test_memes_are_not_updated(login, put_meme_endpoint, mem_id, text, info, tags, url):
    put_meme_endpoint.update_meme(login, mem_id,
        {"id": mem_id,
         "text": text,
         "url": url,
         "tags": tags,
         "info": info
    })
    put_meme_endpoint.check_response_code_is_(400)
