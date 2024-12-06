import requests
from pytest_check import check


def test_id(book_url):
    # url: str = f"{env_config.url}/booking"
    # json: dict[str, str] = {"username": user_config.username, "password": str(user_config.password)}
    response: requests.Response = requests.get(url=book_url)

    with check:
        assert response.status_code == 200  # == HTTPStatus.OK

    with check:
        assert type(response.json()[0]["booking_id"], int)

    with check:
        assert (len(response.json)()) > 0

    with check:
        assert "booking_id" in response.json()
