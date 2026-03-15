import uuid
from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlite.database import Base


class Post(Base):
    __tablename__ = "posts"
    id = mapped_column(primary_key=True, default=uuid.uuid4)
    author_id = mapped_column(ForeignKey("users.id"))
    datetime_to_publish = mapped_column()
