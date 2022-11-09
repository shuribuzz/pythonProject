from django.urls import path

from blog import routers

urlpatterns = [
    path('articles/create/', routers.blogs.create_article),
    path('articles/<str:article_id>/', routers.blogs.get_article),
    path('articles/', routers.blogs.get_all_articles),
    path('comments/create/', routers.comments.create_comment),
    path('token/', routers.auth.create_access_token),

]
