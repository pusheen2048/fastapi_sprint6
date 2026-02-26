from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserBase(BaseModel):
    first_name: str = Field(max_length=256)
    last_name: str = Field(max_length=256)
    username: str = Field(max_length=256)
    email: EmailStr


class UserCreate(UserBase):
    password: SecretStr = Field(min_length=8, max_length=256)


class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(default=None, max_length=256)
    last_name: Optional[str] = Field(default=None, max_length=256)
    username: Optional[str] = Field(default=None, max_length=256)
    email: Optional[EmailStr] = None


class UserUpdatePassword(BaseModel):
    current_password: SecretStr = Field(min_length=8, max_length=256)
    new_password: SecretStr = Field(min_length=8, max_length=256)


class User(UserBase):
    id: UUID
    is_active: bool = True
    is_superuser: bool = False
    created_at: Optional[datetime] = None
