from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from .users import User


class LocationBase(BaseModel):
    title: str = Field(max_length=256, description='Заголовок')
    description: str = Field(description='Описание')
    is_published: bool = Field(default=True, description='Опубликовано')


class LocationCreate(LocationBase):
    author_id: int


class LocationResponse(LocationBase):
    id: int
    author: User
    created_at: datetime
