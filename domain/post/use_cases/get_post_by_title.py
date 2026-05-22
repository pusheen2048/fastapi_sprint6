from sqlite.database import database
from sqlite.repos.posts import PostRepository
from schemas.posts import PostResponse
from domain.post.exceptions import PostNotFoundByTitleException


class GetPostByTitleUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, title):
        with self._database.session() as session:
            post = self._repo.get_by_title(session=session, title=title)
            if post is None:
                raise PostNotFoundByTitleException(title)
        return PostResponse.model_validate(obj=post)
