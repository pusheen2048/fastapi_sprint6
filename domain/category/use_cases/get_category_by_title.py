from fastapi import HTTPException, status

from sqlite.database import database
from sqlite.repos.categories import CategoryRepository
from schemas.categories import CategoryResponse


class GetCategoryByTitleUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, title):
        with self._database.session() as session:
            category = self._repo.get_by_title(session=session, title=title)
        if category is None:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Category with title '{title}' not found"
                )
        return CategoryResponse.model_validate(obj=category)
