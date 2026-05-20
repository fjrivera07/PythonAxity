from sqlalchemy import select
from sqlalchemy.orm import Session

from laboratorio8_2.db.models.user import User
from laboratorio8_2.db.session import engine


def create_user():
    with Session(engine) as session:
        user = User(name="Francisco", email="francisco@test.com")
        session.add(user)
        session.commit()


def read_users():
    with Session(engine) as session:
        users = session.scalars(select(User)).all()

        for user in users:
            print(user.id, user.name, user.email)


def update_user():
    with Session(engine) as session:
        user = session.get(User, 1)

        if user:
            user.name = "Javier"
            session.commit()


def delete_user():
    with Session(engine) as session:
        user = session.get(User, 1)

        if user:
            session.delete(user)
            session.commit()


if __name__ == "__main__":
    # delete_user()
    # create_user()
    update_user()
    read_users()
