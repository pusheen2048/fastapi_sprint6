import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, status, Depends, HTTPException, File, UploadFile
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import FileResponse

from schemas.posts import PostResponse, PostCreate
from domain.post.use_cases.create_post import CreatePostUseCase
from domain.post.use_cases.get_post_by_title import GetPostByTitleUseCase
from domain.post.use_cases.delete_post import DeletePostUseCase
from domain.post.use_cases.upload_image import UploadImageUseCase
from api.depends import (
        create_post_use_case,
        get_post_by_title_use_case,
        delete_post_use_case,
        upload_image_use_case
)
from domain.post.exceptions import (
        PostNotFoundByTitleException,
        PostExistsException
)

posts_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
UPLOAD_DIR = "uploads/posts"


@posts_router.get("/post/{title}",
                     status_code=status.HTTP_200_OK,
                     response_model=PostResponse)
async def get_post_by_title(title: str,
                            use_case: GetPostByTitleUseCase
                            = Depends(get_post_by_title_use_case),
                            token: str = Depends(oauth2_scheme)):
    try:
        return await use_case.execute(title=title)
    except PostNotFoundByTitleException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.get_detail())


@posts_router.post("/post",
                      status_code=status.HTTP_201_CREATED,
                      response_model=PostResponse)
async def create_post(data: PostCreate,
                      use_case: CreatePostUseCase
                      = Depends(create_post_use_case),
                      token: str = Depends(oauth2_scheme)):
    try:
        return await use_case.execute(data)
    except PostExistsException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=e.get_detail())


@posts_router.post("/post/{title}/image",
                   status_code=status.HTTP_200_OK,
                   response_model=PostResponse)
async def upload_post_image(title: str,
                            file: UploadFile = File(...),
                            use_case: UploadImageUseCase = Depends(upload_image_use_case),
                            token: str = Depends(oauth2_scheme)):
    
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Файл не является изображением.")
    
    extension = os.path.splitext(file.filename)[1]
    filename = f"{uuid4()}{extension}"
    path = os.path.join(UPLOAD_DIR, filename)
    try:
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            return await use_case.execute(title=title, image_path=path)        
    except PostNotFoundByTitleException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.get_detail())
 

@posts_router.get("/post/image/{title}", status_code=status.HTTP_200_OK)
async def get_post_image(title: str,
                         use_case: GetPostByTitleUseCase = Depends(get_post_by_title_use_case),
                         token: str = Depends(oauth2_scheme)):
    try:
        post = await use_case.execute(title=title)
        
        if not post.image_path:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="У этого поста нет изображения.")
                                
        if not os.path.exists(post.image_path):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Файл изображения не найден на сервере.")
        return FileResponse(post.image_path)
        
    except PostNotFoundByTitleException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.get_detail())


@posts_router.delete("/posts/{title}",
                        status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(title: str,
                      use_case: DeletePostUseCase
                      = Depends(delete_post_use_case),
                      token: str = Depends(oauth2_scheme)):
    try:
        return await use_case.execute(title=title)
    except PostNotFoundByTitleException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=e.get_detail())
