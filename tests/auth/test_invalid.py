import requests
from pytest_check import check


def test_valid(env_config, user_config):  # w atrybucie nazwa fixture
    url: str = f"{env_config.url}/auth"
    json: dict[str, str] = {"username": user_config.username, "password": "wrong_password"}
    response: requests.Response = requests.post(url=url, json=user_config.model_dump())

    with check:
        assert "token" in response.json()

    with check:
        assert response.status_code == 200
    # print(response.json())


# print(env_config.url)


# json = user_config.model_dump(exclude={"password"})


def test_valid_with_extra_field(env_config, user_config):  # w atrybucie nazwa fixture
    url: str = f"{env_config.url}/auth"
    json = user_config.model_dump()
    json["extra"] = "some_value"
    response: requests.Response = requests.post(url=url, json=json)

    with check:
        assert "token" in response.json()

    with check:
        assert response.status_code == 200


# def test_wrong_no_password_include(env_config, user_config):  # w atrybucie nazwa fixture
#     url: str = f"{env_config.url}/auth"
#     json = user_config.model_dump(include={"username"})
#     response: requests.Response = requests.post(url=url, json=json)
#
#     with check:
#         assert "token" in response.json()
#
#     with check:
#         assert response.status_code == 200


WRONG_PASSWORD = "wrong_password"


def test_valid_wrong_password(auth_url, user_config):  # w atrybucie nazwa fixture
    json: dict[str, str] = {"username": user_config.username, "password": WRONG_PASSWORD}
    response: requests.Response = requests.post(url=auth_url, json=json)

    with check:
        assert "reason" in response.json()

    with check:
        assert response.status_code == 200
