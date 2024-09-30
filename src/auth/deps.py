from firebase_admin import auth
from fastapi import Cookie, HTTPException
from . import services


async def get_user(session_token: str = Cookie(None)):
    """Dependência(fastapi) que retorna o usuário autenticado."""
    session = await services.get_session(session_token)
    if session is None:
        raise HTTPException(status_code=403, detail="Acesso negado")
    user = auth.get_user(session['user_id'])
    if user is None:
        raise HTTPException(status_code=403, detail="Acesso negado")
    return user
