import logging

from domain.post.exceptions import (PostEditForbiddenException,
                                    PostNotFoundByIdException)
from schemas.posts import PostResponse
from sqlite.database import database
from sqlite.repos.posts import PostRepository

logger = logging.getLogger(__name__)


class UploadImageUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, post_id, user, image_path):
        with self._database.session() as session:
            post = self._repo.get_by_id(session=session, id=post_id)
            if not post:
                logger.error(f'Пост с id {post_id} не найден!')
                raise PostNotFoundByIdException(post_id)
            if post.author_id != user.id and not user.is_admin:
                raise PostEditForbiddenException(post_id)
            post.image_path = image_path
            session.commit()
            session.refresh(post)
            logger.info(f'Картинка для поста с id {post_id} успешно обновлена.')
            return PostResponse.model_validate(post, from_attributes=True)
