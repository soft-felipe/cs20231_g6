from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from sqlalchemy_serializer import SerializerMixin

class UsuarioModel(Base, SerializerMixin):
    __tablename__ = 'usuario'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    data_nascimento = Column('data_nascimento', Date, nullable=False)
    nome_completo = Column('nome_completo', String, nullable=False)
    avatar = Column('avatar', String, nullable=True)
    email = Column('email', String, nullable=False)
    usuario_login_id = Column('usuario_login_id', Integer, ForeignKey('usuario_login.id'), unique=True)
    login = relationship("UsuarioLoginModel", back_populates="usuario")
    

class UsuarioLoginModel(Base, SerializerMixin):
    __tablename__ = 'usuario_login'
    
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False)
    senha = Column('senha', String, nullable=False)
    usuario = relationship("UsuarioModel", uselist=False, back_populates="login")

