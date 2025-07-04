from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_items():
    client = TestClient(app)
    response = client.get("/items")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"items": ["item1", "item2", "item3"]}
