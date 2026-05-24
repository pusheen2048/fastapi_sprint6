from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostBase(BaseModel):
    title: str = Field(max_length=256, description="Заголовок")
    text: str = Field(description='Текст поста')
    category_id: Optional[int] = None
    pub_date: datetime
    is_published: bool = Field(default=True)
    image_path: Optional[str] = None


class PostCreate(PostBase):
    model_config = ConfigDict(from_attributes=True)


class PostResponse(PostBase):
    id: int
    author_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
