from pydantic import BaseModel, validator, EmailStr
import datetime
import re


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