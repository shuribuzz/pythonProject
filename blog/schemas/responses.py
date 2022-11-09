from datetime import datetime
from typing import Optional

from ninja import Schema
from pydantic import Field

from blog.schemas.common import UserSchema


class ArticleResponse(Schema):
    id: int
    author: Optional[UserSchema]
    created: datetime
    title: str
    content: str


class CommentResponse(Schema):
    id: int
    text_field: str = Field(alias='textField')

    class Config(Schema.Config):
        allow_population_by_field_name = True


class AuthTokenResponse(Schema):
    access_token: str
    refresh_token: str
