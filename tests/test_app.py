from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_root(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/")
    assert response.json() == {"users": [user_schema]}


def test_update_user(client, user):
    response = client.put(
        "/users/1",
        json={
            "username": "maria.coelho",
            "email": "maria.coelho@example.com",
            "password": "newpassword",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "maria.coelho",
        "email": "maria.coelho@example.com",
        "id": 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        "/users/2",
        json={
            "username": "lucas",
            "email": "lucas@example.com",
            "password": "newpassword",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_update_integrity_error(client, user):
    client.post(
        "/users/",
        json={
            "username": "joao",
            "email": "joao@example.com",
            "password": "secret",
        },
    )

    response_update = client.put(
        f"/users/{user.id}",
        json={
            "username": "joao",
            "email": "joao.claudio@example.com",
            "password": "newpassword",
        },
    )

    assert response_update.status_code == HTTPStatus.CONFLICT
    assert response_update.json() == {
        "detail": "Username or Email already exists"
    }


def test_delete_user(client, user):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted successfully"}


def test_delete_user_not_found(client):
    response = client.delete("/users/2")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
