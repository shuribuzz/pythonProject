from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from blog.routers.auth import auth_router
from blog.routers.blogs import blog_router

api = NinjaAPI()

api.add_router('/blog/', blog_router)
api.add_router(('/auth/'), auth_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
