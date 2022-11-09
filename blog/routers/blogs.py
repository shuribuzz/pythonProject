from typing import List

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.pagination import paginate, LimitOffsetPagination

from blog.auth.validate_token import AuthBearer
from blog.models import Article, Comment
from blog.repository import get_all_articles, get_all_comments
from blog.schemas.requests import ArticleRequest, CommentRequest
from blog.schemas.responses import ArticleResponse, CommentResponse

blog_router = Router()


@blog_router.post('/articles/create/', auth=AuthBearer(), tags=['article'])
def create_article(request, body: ArticleRequest):
    data = body.dict()
    try:
        author = User.objects.get(username=request.auth)
        article = Article.objects.create(author=author, **data)
        return {
            'detail': 'Article has been successfully created.',
            'id': article.id,
        }
    except User.DoesNotExist:
        return {'detail': 'The specific user cannot be found.'}


@blog_router.get('/articles/{article_id}/', response=ArticleResponse)
def get_article(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    return article


@blog_router.get('/articles/', auth=AuthBearer(), response=List[ArticleResponse])
@paginate(LimitOffsetPagination)
def get_articles(request):
    try:
        user = User.objects.get(username=request.auth)
        articles = get_all_articles()
        return articles
    except User.DoesNotExist:
        return {'detail': 'The specific user cannot be found.'}


@blog_router.post('/comments/create/')
def create_comment(request, body: CommentRequest):
    data = body.dict()

    comment = Comment.objects.create(**data)

    return {
        'detail': 'Comment has been successfully created.',
        'id': comment.id,
    }


@blog_router.get('/comments/', response=List[CommentResponse], by_alias=True)
def get_articles(request):
    comments = get_all_comments()
    return comments


@blog_router.get("/blog/{post_id}")
async def search(request, post_id: int):
    blog = await Comment.objects.aget(pk=post_id)
