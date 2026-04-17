from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

from core.settings import settings
from domain.user.exceptions import UserNotFoundByUsernameException
from schemas.auth import Token, AuthCredential
from sqlite.database import database
from core.auth import verify_password
from .depends import user_repo


auth_router = APIRouter()


@auth_router.post("/token")
async def login(data: OAuth2PasswordRequestForm = Depends()):
    try:
        with database.session() as session:
            user = user_repo.get_by_username(session=session,
                                             username=data.username)
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
            detail=e.message,
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
