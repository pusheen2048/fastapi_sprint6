import logging
from datetime import datetime

from sqlite.repos.posts import PostRepository
from sqlite.models.posts import Post
from sqlite.database import database
from schemas.posts import PostCreate, PostResponse
from domain.post.exceptions import PostExistsException

logger = logging.getLogger(__name__)


class CreatePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, data: PostCreate):
        with self._database.session() as session:
            exists = self._repo.get_by_title(session=session,
                                             title=data.title)
            if exists:
                logger.error(f'Пост {data.title} уже существует!')
                raise PostExistsException(data.title)
            post = Post(title=data.title,
                        text=data.text,
                        is_published=data.is_published,
                        pub_date=data.pub_date,
                        category_id=data.category_id,
                        author_id=data.author_id,
                        created_at=datetime.now())
            created = self._repo.create(session, post)
            logger.info(f'Пост {created.title} успешно создан, ему присвоен id {created.id}.')
            return PostResponse.model_validate(created,
                                               from_attributes=True)
