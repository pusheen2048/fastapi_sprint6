from fastapi import HTTPException, status

from sqlite.database import database
from sqlite.repos.categories import CategoryRepository
from domain.category.exceptions import CategoryNotFoundByTitleException


class DeleteCategoryUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, title):
        with self._database.session() as session:
            category = self._repo.get_by_title(session, title)
            if category is None:
                raise CategoryNotFoundByTitleException(title)
            self._repo.delete(session, category)
