import requests
from pytest_check import check


def test_valid(env_config, user_config):  # w atrybucie nazwa fixture
    url: str = f"{env_config.url}/auth"
    # json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password)}
    response: requests.Response = requests.post(url=url, json=user_config.model_dump())

    with check:
        assert "token" in response.json()

    with check:
        assert response.status_code == 200  # == HTTPStatus.OK
    # print(response.json())


# print(env_config.url)
