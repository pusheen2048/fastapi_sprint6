from domain.user.use_cases.get_user_by_username import GetUserByUsernameUseCase
from domain.user.use_cases.create_user import CreateUserUseCase
from domain.category.use_cases.get_category_by_title import GetCategoryByTitleUseCase
from domain.category.use_cases.create_category import CreateCategoryUseCase


def get_user_by_username_use_case() -> GetUserByUsernameUseCase:
    return GetUserByUsernameUseCase()


def create_user_use_case() -> CreateUserUseCase:
    return CreateUserUseCase()


def get_category_by_title_use_case() -> GetCategoryByTitleUseCase:
    return GetCategoryByTitleUseCase()


def create_category_use_case() -> CreateCategoryUseCase:
    return CreateCategoryUseCase()
