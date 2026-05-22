from domain.category.exceptions import CategoryNotFoundByTitleException
from schemas.categories import CategoryResponse
from sqlite.database import database
from sqlite.repos.categories import CategoryRepository


class GetCategoryByTitleUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, title):
        with self._database.session() as session:
            category = self._repo.get_by_title(session=session, title=title)
            if category is None:
                raise CategoryNotFoundByTitleException(title)
        return CategoryResponse.model_validate(obj=category)
