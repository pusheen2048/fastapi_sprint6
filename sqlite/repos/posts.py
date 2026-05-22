from sqlite.models.posts import Post


class PostRepository:
    def __init__(self):
        self._model = Post

    def get_by_title(self, session, title):
        query = (session.query(self._model)
                 .where(self._model.title == title))
        return query.scalar()

    def create(self, session, post):
        session.add(post)
        session.flush()
        return post

    def delete(self, session, post):
        session.delete(post)
        session.commit()
        session.flush()
