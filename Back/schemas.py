from pydantic import BaseModel, EmailStr
import datetime

class Usuario(BaseModel):
    apelido: str
    nome_completo: str
    data_nasc: datetime.date
    avatar: str
    data_criacao: datetime.date
    
class UsuarioLogin(BaseModel):
    username: str
    senha: str
    email: EmailStr
    