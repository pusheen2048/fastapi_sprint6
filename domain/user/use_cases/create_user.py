import logging
from datetime import datetime

from domain.user.exceptions import UserExistsException
from schemas.users import UserCreate, UserResponse
from sqlite.database import database
from sqlite.models.users import User
from sqlite.repos.users import UserRepository

logger = logging.getLogger(__name__)


class CreateUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, data: UserCreate):
        with self._database.session() as session:
            exists = self._repo.get_by_username(session=session,
                                                username=data.username)
            if exists:
                logger.error(f'Пользователь {data.username} уже существует!')
                raise UserExistsException(data.username)
            user = User(first_name=data.first_name,
                        last_name=data.last_name,
                        username=data.username,
                        password=data.password,
                        email=data.email,
                        created_at=datetime.now())
            created = self._repo.create(session, user)
            logger.info(f'Пользователь {created.username} успешно зарегистрирован, ему присвоен id {created.id}.')
            return UserResponse.model_validate(created, from_attributes=True)
