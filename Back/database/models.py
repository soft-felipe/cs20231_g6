from sqlalchemy import Column, String, Integer, Date
from database.base import Base
from sqlalchemy_serializer import SerializerMixin

class UsuarioModel(Base, SerializerMixin):
    __tablename__ = 'usuario'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    data_nascimento = Column('data_nascimento', Date, nullable=False)
    nome_completo = Column('nome_completo', String, nullable=False)
    avatar = Column('avatar', String, nullable=True)

class UsuarioLoginModel(Base, SerializerMixin):
    __tablename__ = 'usuario_login'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String, nullable=False)

