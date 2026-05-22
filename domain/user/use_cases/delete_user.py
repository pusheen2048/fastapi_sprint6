import logging

from domain.user.exceptions import UserNotFoundByUsernameException
from sqlite.database import database
from sqlite.repos.users import UserRepository

logger = logging.getLogger(__name__)


class DeleteUserUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, username):
        with self._database.session() as session:
            user = self._repo.get_by_username(session=session,
                                              username=username)
            if user is None:
                logger.error(f'Пользователя {username} не существует!')
                raise UserNotFoundByUsernameException(username)
        self._repo.delete(session, user)
        logger.info(f'Пользователь {username} с id {user.id} успешно удалён.')
