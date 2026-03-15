from fastapi import APIRouter, status, Depends
from schemas.users import UserResponse, UserCreate, UserBase
from domain.user.use_cases.get_user_by_username import GetUserByUsernameUseCase
from domain.user.use_cases.create_user import CreateUserUseCase
from api.depends import get_user_by_username_use_case, create_user_use_case

user_router = APIRouter()


@user_router.get("/user/{username}", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user_by_username(
    username: str,
    use_case: GetUserByUsernameUseCase = Depends(
        get_user_by_username_use_case)
):
    user = await use_case.execute(username=username)
    return user


@user_router.post("/user", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def create_user(
    data: UserCreate,
    use_case: CreateUserUseCase = Depends(create_user_use_case)
) -> UserBase:
    return await use_case.execute(data)

