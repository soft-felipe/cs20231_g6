from sqlalchemy import Column, String, Integer, Date, ForeignKey
from database.base import Base
from sqlalchemy_serializer import SerializerMixin

class UsuarioModel(Base, SerializerMixin):
    __tablename__ = 'usuario'
    
    id_usuario = Column('id_usuario', Integer, primary_key=True, autoincrement=True)
    id_credencial = Column('id_credencial', Integer, ForeignKey('login.id_login'), nullable=True)
    apelido = Column('apelido', String(30), nullable=True)
    nome_completo = Column('nome_completo', String(255), nullable=True)
    data_nasc = Column('data_nasc', Date, nullable=True)
    avatar = Column('avatar', String(255), nullable=True)
    data_criacao = Column('data_criacao', Date, nullable=True)

class UsuarioLoginModel(Base, SerializerMixin):
    __tablename__ = 'login'
    
    id_login = Column('id_login', Integer, primary_key=True, autoincrement=True)
    username = Column('login', String, nullable=False)
    senha = Column('senha', String, nullable=False)
    email = Column('email', String, nullable=True)
