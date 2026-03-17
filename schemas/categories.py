from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class CategoryBase(BaseModel):
    title: str = Field(max_length=256, description='Заголовок')
    description: str = Field(description='Описание')
    slug: str = Field(max_length=64, description='Идентификатор страницы для URL')
    is_published: bool = Field(default=True, description='Опубликовано')


class CategoryCreate(CategoryBase):
    model_config = ConfigDict(from_attributes=True)


class CategoryResponse(CategoryBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
