from pytest import fixture
from starlette.testclient import TestClient

from src.main import app


@fixture(scope='session')
def wallet_dict() -> dict:
    return {}


@fixture(scope="session")
def client() -> TestClient:
    return TestClient(app=app)
