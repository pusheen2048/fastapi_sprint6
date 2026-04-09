from datetime import datetime

from sqlite.repos.categories import CategoryRepository
from sqlite.models.categories import Category
from sqlite.database import database
from schemas.categories import CategoryCreate, CategoryResponse
from domain.category.exceptions import CategoryExistsException


class CreateCategoryUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, data: CategoryCreate):
        with self._database.session() as session:
            exists = self._repo.get_by_title(session=session,
                                             title=data.title)
            if exists:
                raise CategoryExistsException(data.title)
            category = Category(title=data.title,
                                description=data.description,
                                is_published=data.is_published,
                                slug=data.slug,
                                created_at=datetime.now())
            created = self._repo.create(session, category)
            return CategoryResponse.model_validate(created,
                                                   from_attributes=True)
