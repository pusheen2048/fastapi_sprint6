from domain.category.exceptions import CategoryNotFoundByTitleException
from infrastructure.database import database
from infrastructure.repos.categories import CategoryRepository
from schemas.categories import CategoryResponse


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
