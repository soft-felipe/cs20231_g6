from sqlalchemy import Column, String, Integer, Date
from database.base import Base
from sqlalchemy_serializer import SerializerMixin

class UsuarioModel(Base, SerializerMixin):
    __tablename__ = 'usuario'
    
    id_usuario = Column('id_usuario', Integer, primary_key=True, autoincrement=True)
    id_credencial = Column('id_credencial', Integer, foreign_key=True)
    apelido = Column('apelido', String, nullable=True)
    nome_completo = Column('nome_completo', String, nullable=True)
    data_nasc = Column('data_nasc', Date, nullable=True)
    avatar = Column('avatar', String, nullable=True)
    data_criacao = Column('data_criacao', Date, nullable=True)

class UsuarioLoginModel(Base, SerializerMixin):
    __tablename__ = 'usuario_login'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String, nullable=False)

