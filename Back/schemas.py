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
    etapas: List[Etapa]

class Comentario(BaseModel):
    id: int
    descricao: str

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    pontuacao: int
    prioridade: int
    comentarios: List[Comentario]
   
class Etapa(BaseModel):
    id: int
    titulo: str
    tarefas: List[Tarefa]

class Projeto(BaseModel):
    id: int
    nome: str
    etapas: List[Etapa]