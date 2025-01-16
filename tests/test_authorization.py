import allure
import pytest

@allure.feature("Memes")
@allure.story("Authorize")
@allure.title("Check token status")
def test_get_token_status(login, get_auth_token_status_api):
    get_auth_token_status_api.get_auth_token_status(login)
    get_auth_token_status_api.check_token()

@allure.feature("Memes")
@allure.story("Authorize")
@allure.title("Negative test for token creation")
@pytest.mark.parametrize(
        "name",
        [
            "   ",
            "a"
        ]
    )
def test_create_token_with_invalid_name(auth_api, name):
    auth_api.auth_request_endpoint(name)
    auth_api.check_response_code_is_(400)
