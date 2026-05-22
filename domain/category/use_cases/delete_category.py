import logging

from domain.category.exceptions import CategoryNotFoundByTitleException
from sqlite.database import database
from sqlite.repos.categories import CategoryRepository

logger = logging.getLogger(__name__)


class DeleteCategoryUseCase:
    def __init__(self):
        self._database = database
        self._repo = CategoryRepository()

    async def execute(self, title):
        with self._database.session() as session:
            category = self._repo.get_by_title(session, title)
            if category is None:
                logger.error(f'Категории {title} не существует!')
                raise CategoryNotFoundByTitleException(title)
            self._repo.delete(session, category)
            logger.info(f'Категория {title} с id {category.id} успешно удалена.')
