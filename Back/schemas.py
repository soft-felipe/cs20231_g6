from pydantic import BaseModel, validator, EmailStr
import datetime
import re

class Usuario(BaseModel):
    data_nascimento: datetime.date
    nome_completo: str
    avatar: str
    
class UsuarioLogin(BaseModel):
    username: str
    email: EmailStr
    senha: str
    
    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value