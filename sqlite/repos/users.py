from typing import Type, Optional
from sqlalchemy.orm import Session
from sqlite.models.users import User


class UserRepository:
    def __init__(self):
        self._model: Type[UserModel] = User

    def get_by_username(self, session: Session, username: str):
        query = (
            session.query(self._model)
            .where(self._model.username == username)
        )
        return query.scalar()

    def get_by_id(self, session: Session, user_id: int):
        return session.query(self._model).where(self._model.id == user_id).scalar()

    def create(self, session: Session, user: User):
        session.add(user)
        session.flush()
        return user
