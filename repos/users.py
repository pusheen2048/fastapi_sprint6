from sqlalchemy import select
from models.users import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, session):
        super().__init__(User, session)

    async def get_by_email(self, email: str):
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_username(self, username: str):
        query = select(User).where(User.username == username)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def user_exists(self, login: str):
        query = select(User).where(User.login == login)
        result = await self.session.execute(query)
        return (result.scalar_one_or_none() is not None)
