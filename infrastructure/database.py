from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import settings


class Database:
    def __init__(self):
        self._db_url = settings.DATABASE_URL
        self._engine = create_engine(self._db_url, pool_pre_ping=True)
        self._session_factory = sessionmaker(bind=self._engine,
                                             expire_on_commit=False)
    @contextmanager
    def session(self):
        session = self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


database = Database()
Base = declarative_base()
