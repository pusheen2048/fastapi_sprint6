from fastapi import HTTPException, status
from datetime import datetime

from sqlite.repos.users import UserRepository
from sqlite.models.users import User
from sqlite.database import database
from schemas.users import UserCreate, UserResponse
from domain.user.exceptions import UserExistsException


class CreateUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, data: UserCreate):
        with self._database.session() as session:
            exists = self._repo.get_by_username(session=session,
                                                username=data.username)
            if exists:
                raise UserExistsException(data.username)
            user = User(first_name=data.first_name,
                        last_name=data.last_name,
                        username=data.username,
                        password=data.password,
                        email=data.email,
                        created_at=datetime.now())
            created = self._repo.create(session, user)
            return UserResponse.model_validate(created, from_attributes=True)
