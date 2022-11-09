from ninja.security import HttpBearer
import jwt
from core import settings


class AuthBearer(HttpBearer):

    def authenticate(self, request, token):
        try:
            SECRET_KEY = getattr(settings, 'SECRET_KEY', None)
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            username: str = payload.get('sub')
            if username is None:
                return None
        except jwt.PyJWTError as e:
            return None

        return username
