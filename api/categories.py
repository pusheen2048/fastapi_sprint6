from fastapi import APIRouter, status, Depends
from schemas.categories import CategoryResponse, CategoryCreate
from domain.category.use_cases.create_category import CreateCategoryUseCase
from domain.category.use_cases.get_category_by_title import GetCategoryByTitleUseCase
from domain.category.use_cases.delete_category import DeleteCategoryUseCase
from api.depends import create_category_use_case, get_category_by_title_use_case, delete_category_use_case

category_router = APIRouter()


@category_router.get("/category/{title}", status_code=status.HTTP_200_OK,
                     response_model=CategoryResponse)
async def get_category_by_title(title: str,
                                use_case: GetCategoryByTitleUseCase
                                = Depends(get_category_by_title_use_case)):
    return await use_case.execute(title=title)


@category_router.post("/category", status_code=status.HTTP_200_OK,
                      response_model=CategoryResponse)
async def create_category(data: CategoryCreate,
                          use_case: CreateCategoryUseCase
                          = Depends(create_category_use_case)):
    return await use_case.execute(data)


@category_router.delete("/category/{title}",
                  status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(title: str,
                          use_case: DeleteCategoryUseCase
                          = Depends(delete_category_use_case)):
    return await use_case.execute(title=title)

