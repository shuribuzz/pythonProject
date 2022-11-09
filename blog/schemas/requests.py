from typing import Optional

from ninja import Schema
from pydantic import Field


class ArticleRequest(Schema):
    title: str
    content: str


class CommentRequest(Schema):
    text_field: str = Field(alias='textField')


class LoginRequest(Schema):
    username: str
    password: str
