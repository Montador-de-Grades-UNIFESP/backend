from typing import List
from fastapi import APIRouter, HTTPException, Depends
from . import schemas
from auth.deps import get_user
from data import db

router = APIRouter()


@router.post("/ranking/{user_id}")
async def cadastrar_ranking(user_id: str, ranking: schemas.RankingPost, user = Depends(get_user)):
    if user_id != user.uid:
        raise HTTPException(status_code=403, detail="Acesso negado")
    await db.collection('ranking').document(user_id).set(ranking.model_dump())
    return ranking.model_dump()


@router.get("/ranking", response_model=List[schemas.RankingGet])
async def consultar_ranking(user = Depends(get_user)):
    if user is None:
        raise HTTPException(status_code=403, detail="Acesso negado")
    ranking_stream = db.collection('ranking').stream()
    ranking = []
    async for doc in ranking_stream:
        ranking.append(schemas.DisciplinaGet.model_validate(doc.to_dict()))
    if ranking:
        return ranking
    raise HTTPException(status_code=404, detail="Ranking não encontrado")
