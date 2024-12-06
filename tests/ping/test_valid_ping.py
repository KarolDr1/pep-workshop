import requests


def test_valid_ping(ping_url):
    response: requests.Response = requests.get(url=ping_url)
    assert response.status_code == 201
