from domain.post.exceptions import PostNotFoundByIdException
from schemas.posts import PostResponse
from sqlite.database import database
from sqlite.repos.posts import PostRepository


class GetPostByIdUseCase:
    def __init__(self):
        self._database = database
        self._repo = PostRepository()

    async def execute(self, post_id):
        with self._database.session() as session:
            post = self._repo.get_by_id(session=session, id=post_id)
            if post is None:
                raise PostNotFoundByIdException(post_id)
        return PostResponse.model_validate(obj=post)
