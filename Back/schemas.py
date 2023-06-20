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
    