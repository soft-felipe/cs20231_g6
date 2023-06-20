from pydantic import BaseModel, validator, EmailStr
import datetime
import re

class Usuario(BaseModel):
    id_usuario: int
    id_credencial: int
    apelido: str
    nome_completo: str
    data_nascimento: datetime.date
    avatar: str
    data_criacao: datetime.date
    
class UsuarioLogin(BaseModel):
    id_login: int
    login: str
    senha: str
    email: EmailStr
    
    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value