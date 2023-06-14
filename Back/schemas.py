from pydantic import BaseModel, validator, EmailStr, Field
import datetime
import re

class Usuario(BaseModel):
    email: EmailStr
    data_nascimento: datetime.date
    nome_completo: str
    avatar: str
    
class UsuarioLogin(BaseModel):
    username: str = Field(None)
    senha: str = Field(None)
    
    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value