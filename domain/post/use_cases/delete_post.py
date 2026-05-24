import logging

from domain.post.exceptions import (PostDeleteForbiddenException,
                                    PostNotFoundByIdException)
from sqlite.database import database
from sqlite.repos.posts import PostRepository

logger = logging.getLogger(__name__)


class DeletePostUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, post_id, user):
        with self._database.session() as session:
            post = self._repo.get_by_id(session, post_id)
            if post is None:
                logger.error(f'Поста с id {post_id} не существует!')
                raise PostNotFoundByIdException(post_id)
            if post.author_id != user.id and not user.is_admin:
                raise PostDeleteForbiddenException(post_id)
            self._repo.delete(session, post)
            logger.info(f'Пост с id {post.id} успешно удалён.')
