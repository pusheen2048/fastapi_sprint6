from fastapi import APIRouter, status, Depends
from schemas.categories import CategoryResponse, CategoryCreate
from domain.category.use_cases.create_category import CreateCategoryUseCase
from domain.category.use_cases.get_category_by_title import GetCategoryByTitleUseCase
from api.depends import create_category_use_case, get_category_by_title_use_case

category_router = APIRouter()


@category_router.get("/", status_code=status.HTTP_200_OK,
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
