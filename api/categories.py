from fastapi import APIRouter, status, HTTPException
from datetime import datetime

from schemas.categories import Category

categories_router = APIRouter()
categories = list()


@categories_router.get("/", status_code=status.HTTP_200_OK, response_model=list[Category])
async def get_categories():
    return categories


@categories_router.get("/{category_id}", status_code=status.HTTP_200_OK, response_model=Category)
async def get_category(category_id):   
    for category in categories:
        if category.id == category_id:
            return category
    raise HTTPException(detail="Категория не найдена",
                        status_code=status.HTTP_404_NOT_FOUND)


@categories_router.post("/add", status_code=status.HTTP_201_CREATED, response_model=Category)
async def create_category(title, description, slug, is_published):
    new_category = Category(
        id=len(categories) + 1,
        title=title,
        description=description,
        slug=slug,
        is_published=is_published,
        created_at=datetime.now()
    )
    categories.append(new_category)
    return new_category


@categories_router.delete("/{category_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(category_id:int):
    for idx, category in enumerate(categories, 1):
        if category.id == category_id:
            categories.pop(idx)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Категория не найдена")
