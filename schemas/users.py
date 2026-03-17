from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=256, description='Пароль')
    model_config = ConfigDict(from_attributes=True)


class UserResponse(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
