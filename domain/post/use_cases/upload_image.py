import logging

from sqlite.repos.posts import PostRepository
from sqlite.database import database
from schemas.posts import PostResponse
from domain.post.exceptions import PostNotFoundByTitleException 

logger = logging.getLogger(__name__)


class UploadImageUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, title: str, image_path: str):
        with self._database.session() as session:
            post = self._repo.get_by_title(session=session, title=title)
            if not post:
                logger.error(f'Пост {title} не найден!')
                raise PostNotFoundByTitleException(title)
            
            post.image_path = image_path
            session.commit()
            session.refresh(post)
            logger.info(f'Картинка для поста {title} успешно обновлена.')
            return PostResponse.model_validate(post, from_attributes=True)
