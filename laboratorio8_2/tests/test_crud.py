import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from laboratorio8_2.db.base import Base
from laboratorio8_2.db.models.user import User


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session


def test_create_user(session):
    user = User(name="Francisco", email="test@test.com")
    session.add(user)
    session.commit()
    assert user.id is not None


def test_read_user(session):
    user = User(name="Francisco", email="test@test.com")
    session.add(user)
    session.commit()

    result = session.get(User, user.id)

    assert result is not None
    assert result.name == "Francisco"


def test_update_user(session):

    user = User(name="Francisco", email="test@test.com")

    session.add(user)
    session.commit()

    user.name = "Javier"
    session.commit()

    updated = session.get(User, user.id)

    assert updated.name == "Javier"


def test_delete_user(session):

    user = User(name="Francisco", email="test@test.com")

    session.add(user)
    session.commit()

    user_id = user.id

    session.delete(user)
    session.commit()

    deleted = session.get(User, user_id)

    assert deleted is None
