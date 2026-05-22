import logging
from sqlite.database import database
from sqlite.repos.posts import PostRepository
from domain.post.exceptions import PostNotFoundByTitleException

logger = logging.getLogger(__name__)


class DeletePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, title):
        with self._database.session() as session:
            post = self._repo.get_by_title(session, title)
            if post is None:
                logger.error(f'Поста {title} не существует!')
                raise PostNotFoundByTitleException(title)
            self._repo.delete(session, post)
            logger.info(f'Пост {title} с id {post.id} успешно удалён.')
