from sqlite.models.users import User


class UserRepository:
    def __init__(self):
        self._model = User

    def get_by_username(self, session, username):
        user = (session.query(self._model)
                .where(self._model.username == username))
        return user.scalar()

    def get_by_id(self, session, user_id):
        user = (session.query(self._model)
                .where(self._model.id == user_id))
        return user.scalar()

    def create(self, session, user):
        session.add(user)
        session.flush()
        return user

    def delete(self, session, user):
        session.delete(user)
        session.commit()
        session.flush()
