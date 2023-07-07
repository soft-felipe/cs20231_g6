from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from sqlalchemy_serializer import SerializerMixin


class UsuarioLoginModel(Base, SerializerMixin):
    __tablename__ = 'login'

    id_login = Column('id_login', Integer, primary_key=True, autoincrement=True)
    username = Column('login', String, nullable=False)
    senha = Column('senha', String, nullable=False)
    email = Column('email', String, nullable=False)
    credencial_login = relationship('UsuarioModel', backref="login")


class UsuarioModel(Base, SerializerMixin):
    __tablename__ = 'usuario'

    id_usuario = Column('id_usuario', Integer, primary_key=True, autoincrement=True)
    id_credencial = Column('id_credencial', Integer, ForeignKey('login.id_login'))
    apelido = Column('apelido', String(30))
    nome_completo = Column('nome_completo', String(255))
    data_nasc = Column('data_nasc', Date)
    avatar = Column('avatar', String(255))
