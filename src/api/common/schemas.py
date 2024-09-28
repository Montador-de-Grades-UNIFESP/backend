from pydantic import BaseModel, Field
from typing import List, Set
from enum import Enum


class DIA(str, Enum):
    SEG = "Segunda"
    TER = "Terça"
    QUA = "Quarta"
    QUI = "Quinta"
    SEX = "Sexta"
    SAB = "Sábado"
    DOM = "Domingo"


class HORARIO(str, Enum):
    M1 = "08h00-10h00"
    M2 = "10h00-12h00"
    T1 = "13h30-15h30"
    T2 = "15h30-17h30"
    N1 = "19h00-21h00"
    N2 = "21h00-23h00"


class CURSO(str, Enum):
    BCT_I = "BCT_I"
    BCT_N = "BCT_N"
    CCOMP_I = "CCOMP_I"
    CCOMP_N = "CCOMP_N"


class DisciplinaGet(BaseModel):
    curso: CURSO
    dia: Set[DIA]
    horario: HORARIO
    id: int
    nome: str
    professores: str
    turma: str = Field(max_length=1)


class RankingPost(BaseModel):
    cr: float
    creditos: int
    curso: CURSO
    grade: List[DisciplinaGet]


class RankingGet(BaseModel):
    cr: float
    creditos: int
    curso: CURSO
    grade: List[DisciplinaGet]

