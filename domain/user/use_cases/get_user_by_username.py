from domain.user.exceptions import UserNotFoundByUsernameException
from infrastructure.database import database
from infrastructure.repos.users import UserRepository
from schemas.users import UserResponse


class GetUserByUsernameUseCase:
    def __init__(self):
        self._database = database
        self._repo = UserRepository()

    async def execute(self, username):
        with self._database.session() as session:
            user = self._repo.get_by_username(session=session,
                                              username=username)
            if user is None:
                raise UserNotFoundByUsernameException(username)

        return UserResponse.model_validate(obj=user)
