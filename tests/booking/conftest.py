import pytest


@pytest.fixture(scope="session")
def book_id(env_config) -> str:
    return f"{env_config.url}/booking"
