from typing import Type, Optional
from sqlalchemy.orm import Session

from sqlite.models.users import Category


class CategoryRepository:
    def __init__(self):
        self._model = Category

    def get_by_title(self, session, title):
        query = (session.query(self._model)
                 .where(self._model.title == title))
        return query.scalar()

    def get_by_id(self, session, category_id):
        return (session.query(self._model)
                .where(self._model.id == category_id)).scalar()

    def create(self, session, category):
        session.add(category)
        session.flush()
        return category
