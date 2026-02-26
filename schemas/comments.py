from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from .posts import Post
from .users import User


class CommentBase(BaseModel):
    text: str


class CommentCreate(CommentBase):
    author_id: int
    post_id: int


class CommentUpdate(BaseModel):
    text: Optional[str]


class Comment(CommentBase):
    author: User
    post: Post
    created_at: datetime
