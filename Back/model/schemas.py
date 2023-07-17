from pydantic import BaseModel, validator, EmailStr, Field
import datetime
import re
from typing import List


class Usuario(BaseModel):
    apelido: str
    nome_completo: str
    data_nasc: datetime.date
    avatar: str

class UsuarioLogin(BaseModel):
    username: str
    senha: str
    email: EmailStr = Field(None)

    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@|_|-)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value

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