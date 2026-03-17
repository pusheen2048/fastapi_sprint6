from sqlite.models.users import User


class UserRepository:
    def __init__(self):
        self._model = User

    def get_by_username(self, session, username):
        query = (session.query(self._model)
                 .where(self._model.username == username))
        return query.scalar()

    def get_by_id(self, session, user_id):
        return (session.query(self._model)
                .where(self._model.id == user_id)).scalar()

    def create(self, session, user):
        session.add(user)
        session.flush()
        return user
