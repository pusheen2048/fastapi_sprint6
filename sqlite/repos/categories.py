from sqlite.models.categories import Category


class CategoryRepository:
    def __init__(self):
        self._model = Category

    def get_by_title(self, session, title):
        query = (session.query(self._model)
                 .where(self._model.title == title))
        return query.scalar()

    def create(self, session, category):
        session.add(category)
        session.flush()
        return category
