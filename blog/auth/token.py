from datetime import datetime, timedelta

import jwt

from core import settings

payload = {
    'iss': 'backend-api',
    'exp': datetime.utcnow() + timedelta(minutes=15),
    'type': 'access'
}


def create_access_token(*, data: dict):
    payload.update({'sub': data['username']})

    encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return encoded_jwt
