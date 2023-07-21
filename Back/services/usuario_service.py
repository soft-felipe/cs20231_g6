from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import UsuarioModel, UsuarioLoginModel
from model.schemas import Usuario, UsuarioLogin
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
import json
from jose import jwt, JWTError
from datetime import datetime, timedelta
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

crypt_context = CryptContext(schemes=['sha256_crypt'])


class UsuarioLoginService:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def registrar_usuario_login(self, usuario: UsuarioLogin):
        usuario_login_model = UsuarioLoginModel(
            username=usuario.username,
            senha=crypt_context.hash(usuario.senha),
            email=usuario.email
        )
        try:
            self.db_session.add(usuario_login_model)
            self.db_session.commit()
            return usuario_login_model.id_login
        except IntegrityError:
            raise HTTPException(
                detail="Erro ao inserir login do usuario",
                status_code=status.HTTP_400_BAD_REQUEST
            )

    def registrar_usuario(self, usuario: Usuario, id_credencial: int):
        usuario_model = UsuarioModel(
            id_credencial=id_credencial,
            apelido=usuario.apelido,
            nome_completo=usuario.nome_completo,
            data_nasc=usuario.data_nasc,
            avatar=usuario.avatar,
        )

        try:
            self.db_session.add(usuario_model)
            self.db_session.commit()
            return usuario_model.id_usuario
        except IntegrityError:
            raise HTTPException(
                detail="Erro ao inserir dados do usuario",
                status_code=status.HTTP_400_BAD_REQUEST
            )

    # todo
    def listar_usuarios_login(self):
        try:
            usuario_lista = self.db_session.query(UsuarioLoginModel).all()
            return usuario_lista
        except:
            raise HTTPException(
                detail="Erro ao buscar usuarios",
                status_code=status.HTTP_400_BAD_REQUEST
            )

    def login_usuario(self, usuario: UsuarioLogin, expires_in: int = 60):
        usuario_back = self.db_session.query(UsuarioLoginModel).filter_by(username=usuario.username).first()

        if usuario_back is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Username ou senha incorretos.'
            )

        if not crypt_context.verify(usuario.senha, usuario_back.senha):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Username ou senha incorretos.'
            )

        exp = datetime.utcnow() + timedelta(minutes=expires_in)

        payload = {
            'sub': usuario.username,
            'exp': exp,
        }

        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        return {
            'access_token': access_token,
            'exp': exp.isoformat(),
            'id_login': usuario_back.id_login
        }

    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token de acesso invalido.'
            )

        usuario_back = self.db_session.query(UsuarioLoginModel).filter_by(username=data['sub']).first()

        if usuario_back is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token de acesso invalido.'
            )

    def verifica_existencia_usuario(self, id_usuario: int):
        usuario = self.db_session.query(UsuarioModel).filter_by(id_usuario=id_usuario).first()
        if not usuario:
            return False, JSONResponse(
                content={'error': 'Usuário não encontrado'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        return True, None
