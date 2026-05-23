import os
import shutil
from uuid import uuid4

from api.auth import get_current_user
from api.depends import (create_post_use_case, delete_post_use_case,
                         get_post_by_id_use_case, upload_image_use_case)
from domain.post.exceptions import (PostDeleteForbiddenException,
                                    PostNotFoundByIdException)
from domain.post.use_cases.create_post import CreatePostUseCase
from domain.post.use_cases.delete_post import DeletePostUseCase
from domain.post.use_cases.get_post_by_id import GetPostByIdUseCase
from domain.post.use_cases.upload_image import UploadImageUseCase
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer
from schemas.posts import PostCreate, PostResponse

posts_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
UPLOAD_DIR = os.path.join('uploads', 'posts')


@posts_router.get("/post/{post_id}",
                  status_code=status.HTTP_200_OK,
                  response_model=PostResponse)
async def get_post_by_id(post_id: int,
                         use_case: GetPostByIdUseCase
                         = Depends(get_post_by_id_use_case),
                         token: str = Depends(oauth2_scheme)):
    try:
        return await use_case.execute(post_id=post_id)
    except PostNotFoundByIdException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.get_detail())


@posts_router.post("/post",
                   status_code=status.HTTP_201_CREATED,
                   response_model=PostResponse)
async def create_post(data: PostCreate,
                      use_case: CreatePostUseCase
                      = Depends(create_post_use_case),
                      current_user = Depends(get_current_user)):
    try:
        return await use_case.execute(data, user_id=current_user.id)
    except CategoryNotFoundByIdException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.get_detail())


@posts_router.post("/post/{post_id}/image",
                   status_code=status.HTTP_200_OK,
                   response_model=PostResponse)
async def upload_post_image(post_id: int,
                            file: UploadFile = File(...),
                            use_case: UploadImageUseCase = Depends(upload_image_use_case),
                            token: str = Depends(oauth2_scheme)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Файл не является изображением.")

    extension = os.path.splitext(file.filename)[1]
    filename = f"{post_id}_{uuid4()}{extension}"
    path = os.path.join(UPLOAD_DIR, filename)
    try:
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            return await use_case.execute(post_id=post_id, image_path=path)

    except PostNotFoundByIdException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.get_detail())


@posts_router.get("/post/image/{post_id}", status_code=status.HTTP_200_OK)
async def get_post_image(post_id: int,
                         use_case: GetPostByIdUseCase = Depends(get_post_by_id_use_case),
                         token: str = Depends(oauth2_scheme)):
    try:
        post = await use_case.execute(post_id=post_id)
        if not post.image_path:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="У этого поста нет изображения.")
        if not os.path.exists(post.image_path):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Файл изображения не найден на сервере.")
        return FileResponse(post.image_path)

    except PostNotFoundByIdException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.get_detail())


@posts_router.delete("/posts/{post_id}",
                     status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int,
                      use_case: DeletePostUseCase
                      = Depends(delete_post_use_case),
                      current_user = Depends(get_current_user)):
    try:
        return await use_case.execute(post_id=post_id, user_id=current_user.id)

    except PostNotFoundByIdException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.get_detail())
    except PostDeleteForbiddenException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=e.get_detail())
