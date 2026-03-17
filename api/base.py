from fastapi import APIRouter, status, Depends
from schemas.users import CategoryResponse, CategoryCreate, CategoryBase
from domain.user.use_cases.create_category import CreateCategoryUseCase
from api.depends import create_category_use_case

category_router = APIRouter()


@router.post("/category", status_code=status.HTTP_200_OK, response_model=CategoryResponse)
async def create_category(
    data: CategoryCreate,
    use_case: CreateCategoryUseCase = Depends(create_category_use_case)
) -> CategoryBase:
    return await use_case.execute(data)
