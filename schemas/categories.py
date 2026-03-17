from pydantic import BaseModel, Field
from datetime import datetime


class CategoryBase(BaseModel):
    title: str = Field(max_length=256, description='Заголовок')
    description: str = Field(description='Описание')
    slug: str = Field(max_length=64, description='Идентификатор страницы для URL')
    is_published: bool = Field(default=True, description='Опубликовано')


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
