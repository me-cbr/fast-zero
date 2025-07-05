from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username="maria", email="maria@example", password="maria123"
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == "maria"))

    assert asdict(user) == {
        "id": 1,
        "username": "maria",
        "email": "maria@example",
        "password": "maria123",
        "created_at": time,
    }
