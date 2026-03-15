import uuid
from datetime import datetime
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import mapped_column
from core.db import Base


class Category(Base):
    __tablename__ = "categories"
    id = mapped_column(primary_key=True, default=uuid.uuid4)
    author_id = mapped_column(ForeignKey("users.id"))
    title = mapped_column(nullable=False)
    description = mapped_column(nullable=False)
    is_published = mapped_column(nullable=False)
    created_at = mapped_column(server_default=func.now())
