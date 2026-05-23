from jose import JWTError, jwt

from core.exceptions import CredentialsException
from core.settings import settings
from domain.category.use_cases.create_category import CreateCategoryUseCase
from domain.category.use_cases.delete_category import DeleteCategoryUseCase
from domain.category.use_cases.get_category_by_title import \
    GetCategoryByTitleUseCase
from domain.post.use_cases.create_post import CreatePostUseCase
from domain.post.use_cases.delete_post import DeletePostUseCase
from domain.post.use_cases.get_post_by_id import GetPostByIdUseCase
from domain.post.use_cases.upload_image import UploadImageUseCase
from domain.user.use_cases.create_user import CreateUserUseCase
from domain.user.use_cases.delete_user import DeleteUserUseCase
from domain.user.use_cases.get_user_by_username import GetUserByUsernameUseCase
from fastapi import HTTPException, status
from schemas.auth import TokenData
from sqlite.database import Database
from sqlite.repos.users import UserRepository


def get_user_by_username_use_case() -> GetUserByUsernameUseCase:
    return GetUserByUsernameUseCase()


def create_user_use_case() -> CreateUserUseCase:
    return CreateUserUseCase()


def delete_user_use_case() -> DeleteUserUseCase:
    return DeleteUserUseCase()


def get_category_by_title_use_case() -> GetCategoryByTitleUseCase:
    return GetCategoryByTitleUseCase()


def create_category_use_case() -> CreateCategoryUseCase:
    return CreateCategoryUseCase()


def delete_category_use_case() -> DeleteCategoryUseCase:
    return DeleteCategoryUseCase()


def get_post_by_id_use_case() -> GetPostByIdUseCase:
    return GetPostByIdUseCase()


def create_post_use_case() -> CreatePostUseCase:
    return CreatePostUseCase()


def delete_post_use_case() -> DeletePostUseCase:
    return DeletePostUseCase()


def upload_image_use_case() -> UploadImageUseCase:
    return UploadImageUseCase()


user_repo = UserRepository()
database = Database()
