from datetime import datetime, timedelta, timezone

from jose import jwt

from api.depends import user_repo
from core.auth import verify_password
from core.settings import settings
from domain.user.exceptions import UserNotFoundByUsernameException
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.auth import Token
from sqlite.database import database

auth_router = APIRouter()


@auth_router.post("/token")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    try:
        with database.session() as session:
            user = user_repo.get_by_username(session=session,
                                             username=data.username)
            if user is None:
                raise UserNotFoundByUsernameException(data.username)
        if not verify_password(plain_password=data.password,
                               hashed_password=user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный пароль",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except UserNotFoundByUsernameException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail,
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token_data = {"sub": user.username}

    to_encode = token_data.copy()
    if access_token_expires:
        expire = datetime.now(timezone.utc) + access_token_expires
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    access_token = jwt.encode(
        claims=to_encode,
        key=settings.SECRET_AUTH_KEY.get_secret_value(),
        algorithm=settings.AUTH_ALGORITHM,
    )
    return Token(access_token=access_token, token_type="bearer")
