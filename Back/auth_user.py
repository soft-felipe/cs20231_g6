from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database.models import UsuarioModel
from schemas import Usuario
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.ext.declarative import DeclarativeMeta
import json
from jose import jwt, JWTError
from datetime import datetime, timedelta
from decouple import config


SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

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
            
    def listar_usuarios(self):
        try:
            usuario_lista = self.db_session.query(UsuarioModel).all()
            return usuario_lista
        except:
            raise HTTPException(
                detail="Erro ao buscar usuarios",
                status_code=status.HTTP_400_BAD_REQUEST
            )
            
            
    def login_usuario(self, usuario:Usuario, expires_in: int = 60):
        usuario_back = self.db_session.query(UsuarioModel).filter_by(username=usuario.username).first()
        
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
            'sub' : usuario.username,
            'exp' : exp
        }
        
        access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        
        return {
            'access_token' : access_token,
            'exp' : exp.isoformat()
        }
    
    def verify_token(self, access_token):
        try:
            data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token de acesso invalido.'
            )
        
        
        usuario_back = self.db_session.query(UsuarioModel).filter_by(username=data['sub']).first()
        
        if usuario_back is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token de acesso invalido.'
            )
        
            
        
        

            

    

