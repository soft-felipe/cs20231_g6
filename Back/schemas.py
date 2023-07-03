from pydantic import BaseModel, validator, EmailStr
import datetime
import re
from typing import List


class Usuario(BaseModel):
    data_nasc: datetime.date
    nome_completo: str
    apelido: str
    avatar: str
    data_criacao = datetime.date


class UsuarioLogin(BaseModel):
    username: str
    senha: str
    email: EmailStr

    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value

class Projeto(BaseModel):
    nome: str
    # não tenho certeza se é assim que se faz '-'
    etapas: List[Etapa] = []

class Etapa(BaseModel):
    titulo: str
    index: int


class Tarefa(BaseModel):
    titulo: str
    descricao: str
    criacao: datetime.date
    limite: datetime.date
    pontuacao: int
    prioridade: int


class Comentario(BaseModel):
    descricao: str