import logging
from datetime import datetime

from domain.category.exceptions import CategoryNotFoundByIdException
from schemas.posts import PostCreate, PostResponse
from sqlite.database import database
from sqlite.models.posts import Post
from sqlite.repos.categories import CategoryRepository
from sqlite.repos.posts import PostRepository

logger = logging.getLogger(__name__)


class CreatePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()
        self._category_repo = CategoryRepository()

    async def execute(self, data: PostCreate, user_id):
        with self._database.session() as session:
            category = self._category_repo.get_by_id(session, data.category_id)
            if category is None:
                raise CategoryNotFoundByIdException(data.category_id)
            post = Post(title=data.title,
                        text=data.text,
                        is_published=data.is_published,
                        pub_date=data.pub_date,
                        category_id=data.category_id,
                        author_id=user_id,
                        created_at=datetime.now())
            created = self._repo.create(session, post)
            logger.info(f'Пост {created.title} успешно создан, ему присвоен id {created.id}.')
            return PostResponse.model_validate(created,
                                               from_attributes=True)
