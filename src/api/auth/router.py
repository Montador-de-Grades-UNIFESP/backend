from fastapi import APIRouter, Response, status
from auth import services as auth_services
from . import schemas


router = APIRouter()


@router.post("/sessao", status_code=status.HTTP_201_CREATED)
async def criar_sessao(credenciais: schemas.SessaoPost):
    user_id = await auth_services.authenticate_token_id(credenciais.id_token)
    if not user_id:
        return Response(status_code=401)
    session_token = await auth_services.new_session(user_id)
    response = Response()
    response.set_cookie(key="session_token",
                        value=session_token,
                        httponly=True,
                        secure=True,
                        samesite="strict")
    return response



