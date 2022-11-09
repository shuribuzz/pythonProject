import uuid

from ninja import Router

from blog.auth.token import create_access_token
from blog.schemas.requests import LoginRequest
from blog.schemas.responses import AuthTokenResponse

auth_router = Router()


@auth_router.post('/token/')
def create_token(request, body: LoginRequest):
    access_token = create_access_token(data=body.dict())
    refresh_token = uuid.uuid4()

    return AuthTokenResponse(
        access_token=access_token,
        refresh_token=str(refresh_token)
    )
