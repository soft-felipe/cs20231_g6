from pydantic import BaseModel, validator, EmailStr
import datetime
import re

class Usuario(BaseModel):
    username: str
    senha: str
    email: EmailStr
    data_nascimento: datetime.date
    nome_completo: str

    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value