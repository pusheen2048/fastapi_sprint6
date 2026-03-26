from fastapi import HTTPException, status

from sqlite.database import database
from sqlite.repos.users import UserRepository


class DeleteUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, username):
        with self._database.session() as session:
            user = self._repo.get_by_username(
                session=session, username=username)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with username '{username}' not found"
            )
        self._repo.delete(session, user)
