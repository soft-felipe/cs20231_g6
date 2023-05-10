from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import UsuarioModel
from schemas import Usuario
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status

crypt_context = CryptContext(schemes=['sha256_crypt'])

class UsuarioUseCase:
    def __init__(self, db_session:Session):
        self.db_session = db_session

    def registrar_usuario(self, usuario:Usuario):
        usuario_model = UsuarioModel(
            username = usuario.username,
            senha = crypt_context.hash(usuario.senha),
            email = usuario.email,
            data_nascimento = usuario.data_nascimento,
            nome_completo = usuario.nome_completo
        )
        try:
            self.db_session.add(usuario_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                detail="Erro ao inserir usuario",
                status_code=status.HTTP_400_BAD_REQUEST
            )

            

    

