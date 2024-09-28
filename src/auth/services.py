from . import utils
from data import db
from firebase_admin import auth


async def new_session(user_id: str):
    """Cria uma nova sessão para o usuário e retorna o token da sessão."""
    token = utils.generate_session_token()
    await db.collection("sessions").document(token).set({"user_id": user_id})
    return token


async def get_session(token: str):
    """Retorna a sessão correspondente ao token passado."""
    session = await db.collection("sessions").document(token).get()
    return session.to_dict()


async def authenticate_token_id(id_token) -> str | None:
    """Verifica se o token de autenticação é válido e retorna o ID do usuário."""
    decoded_token = auth.verify_id_token(id_token)
    user_id = decoded_token.get('uid')
    if user_id:
        return user_id
    return None
