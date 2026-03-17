from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str = Field(max_length=255)
    text: str = Field(description='Текст поста')
    pub_date: datetime
    is_published: bool = Field(default=True)


class PostCreate(PostBase):
    author_id: int
    category_id: Optional[int] = None
    location_id: Optional[int] = None


class PostResponse(PostBase):
    id: int
    author_id: int
    created_at: datetime
