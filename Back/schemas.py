from pydantic import BaseModel, validator, EmailStr
import datetime
import re
from typing import Optional

class Usuario(BaseModel):
    username: str
    senha: str
    email: Optional[EmailStr]
    data_nascimento: Optional[datetime.date]
    nome_completo: Optional[str]

    @validator('username')
    def validar_username(cls, value):
        if not re.match('^([a-z]|[0-9]|@)+$', value):
            raise ValueError('Formato invalido de nome de usuario')
        return value