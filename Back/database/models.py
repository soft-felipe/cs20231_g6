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


class ProjetoModel(Base, SerializerMixin):
    __tablename__ = 'projeto'

    id_projeto = Column('id_projeto', Integer, primary_key=True, autoincrement=True)
    id_criador = Column('id_criador', Integer, ForeignKey('usuario.id_usuario'))
    nome = Column('nome', String(100))
    descricao = Column('descricao', String(200))


class EtapaModel(Base, SerializerMixin):
    __tablename__ = 'etapa'

    id_etapa = Column('id_etapa', Integer, primary_key=True, autoincrement=True)
    id_projeto = Column('id_projeto', Integer, ForeignKey('projeto.id_projeto'))
    nome = Column('nome', String(30))
    # cor -> não precisamos disso por enquanto


class TarefaModel(Base, SerializerMixin):
    __tablename__ = 'tarefa'

    id_tarefa = Column('id_tarefa', Integer, primary_key=True, autoincrement=True)
    id_criador = Column('id_criador', Integer, ForeignKey('usuario.id_usuario'))
    id_etapa = Column('id_etapa', Integer, ForeignKey('etapa.id_etapa'))
    descricao = Column('descricao', String(200))


class ComentarioModel(Base, SerializerMixin):
    __tablename__ = 'comentario'

    id_comentario = Column('id_comentario', Integer, primary_key=True, autoincrement=True)
    id_criador = Column('id_criador', Integer, ForeignKey('usuario.id_usuario'))
    id_tarefa = Column('id_tarefa', Integer, ForeignKey('tarefa.id_tarefa'))
    descricao = Column('descricao', String(200))


class ProjetoParticipanteModel(Base, SerializerMixin):
    __tablename__ = 'projeto_participante'

    id_projeto_participante = Column('id_projeto_participante', Integer, primary_key=True, autoincrement=True)
    id_projeto = Column('id_projeto', Integer)
    id_participante = Column('id_participante', Integer)


# MODELS DAS VIEWS (SELECTS COM JOINS)

class ViewInfosParticipantesProjetoModel(Base, SerializerMixin):
    __tablename__ = 'infos_participantes_projetos'

    id_projeto = Column('id_projeto', Integer, primary_key=True)
    id_participante = Column('id_participante', Integer)
    nome_projeto = Column('nome_projeto', String(100))
    apelido_participante = Column('apelido_participante', String(30))
    nome_completo_participante = Column('nome_completo_participante', String(255))
    data_nasc = Column('data_nasc', Date)
    email = Column('email', String)
