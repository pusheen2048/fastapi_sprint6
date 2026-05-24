from domain.category.exceptions import CategoryNotFoundByIdException
from schemas.categories import CategoryResponse
from sqlite.database import database
from sqlite.repos.categories import CategoryRepository


class GetCategoryByIdUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, category_id):
        with self._database.session() as session:
            category = self._repo.get_by_id(session=session, id=category_id)
            if category is None:
                raise CategoryNotFoundByIdException(category_id)
        return CategoryResponse.model_validate(obj=category)
