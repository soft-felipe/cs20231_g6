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


class UsuarioAlterarSenha(BaseModel):
    username: str
    senha_atual: str
    nova_senha: str
    email: EmailStr = Field(None)


class Projeto(BaseModel):
    nome: str
    descricao: str


class AlterarInfoProjeto(BaseModel):
    nova_info: str


class ProjetoParticipantes(BaseModel):
    id_projeto: int
    id_participante: int


class Comentario(BaseModel):
    id_criador: int
    descricao: str


class Tarefa(BaseModel):
    id_criador: int
    id_responsavel: int
    descricao: str


class Etapa(BaseModel):
    titulo: str
    tarefas: List[Tarefa]