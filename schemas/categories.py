import uuid
from datetime import datetime
from pydantic import BaseModel, Field


class Category(BaseModel):
    title: str = Field(max_length=256, description='Заголовок')
    description: str = Field(description='Описание')
    slug: str = Field(description='Идентификатор страницы для URL')
    is_published: bool = Field(True, description='Опубликовано')
    created_at: datetime = Field(description='Добавлено')


class CategoryCreate(Category):
    author_id: int 


class CategoryUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=256)
    description: Optional[str]
    slug: Optional[str]
    is_published: Optional[bool]


class CategoryResponse(Category):
    id: uuid.UUID
    created_at: datetime
