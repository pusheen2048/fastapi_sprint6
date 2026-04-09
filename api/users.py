from fastapi import APIRouter, status, Depends, HTTPException
from schemas.users import UserResponse, UserCreate
from domain.user.use_cases.get_user_by_username import GetUserByUsernameUseCase
from domain.user.use_cases.create_user import CreateUserUseCase
from domain.user.use_cases.delete_user import DeleteUserUseCase
from api.depends import (
        get_user_by_username_use_case,
        create_user_use_case,
        delete_user_use_case
)
from domain.user.exceptions import (
        UserNotFoundByUsernameException,
        UserExistsException
)

user_router = APIRouter()


@user_router.get("/user/{username}",
                 status_code=status.HTTP_200_OK,
                 response_model=UserResponse)
async def get_user_by_username(username: str,
                               use_case: GetUserByUsernameUseCase
                               = Depends(get_user_by_username_use_case)):
    try:
        return await use_case.execute(username=username)
    except UserNotFoundByUsernameException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.get_detail())


@user_router.post("/user",
                  status_code=status.HTTP_201_CREATED,
                  response_model=UserResponse)
async def create_user(data: UserCreate,
                      use_case: CreateUserUseCase
                      = Depends(create_user_use_case)):
    try:
        return await use_case.execute(data)
    except UserExistsException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.get_detail())


@user_router.delete("/user/{username}",
                    status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(username: str,
                      use_case: DeleteUserUseCase
                      = Depends(delete_user_use_case)):
    try:
        return await use_case.execute(username=username)
    except UserNotFoundByUsernameException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.get_detail())
