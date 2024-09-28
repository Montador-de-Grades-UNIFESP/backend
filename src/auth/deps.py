from firebase_admin import auth
from fastapi import Cookie
from . import services


async def get_user(auth_token: str = Cookie(None)):
    """Dependência(fastapi) que retorna o usuário autenticado."""
    user_id = services.get_session(auth_token)
    user = auth.get_user(user_id)
    return user.email
