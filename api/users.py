from fastapi import APIRouter, status, HTTPException

from schemas.users import User

users_router = APIRouter()
users = list()


@users_router.get("/", status_code=status.HTTP_200_OK,
                  response_model=list[User])
async def get_users():
    return users


@users_router.get("/{user_id}", status_code=status.HTTP_200_OK,
                  response_model=User)
async def get_user(user_id):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(detail="Пользователь не найден",
                        status_code=status.HTTP_404_NOT_FOUND)


@users_router.post("/add", status_code=status.HTTP_201_CREATED,
                   response_model=User)
async def create_user(login, email, password,
                      first_name=None, second_name=None):
    new_user = User(id=len(users) + 1,
                    login=login,
                    email=email,
                    password=password,
                    first_name=first_name,
                    second_name=second_name)
    users.append(new_user)
    return new_user
