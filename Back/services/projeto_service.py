from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from model.schemas import Projeto
from database.models import ProjetoModel, ProjetoParticipanteModel
from fastapi import status
from fastapi.exceptions import HTTPException

class ProjetoService:
    def __init__(self, db_session:Session):
        self.db_session = db_session

    def criar_projeto(self, projeto: Projeto, id_usario: int):
        projeto_model = ProjetoModel(
            id_criador = id_usario,
            nome = projeto.nome,
            descricao = projeto.descricao
        )

        try:
            self.db_session.add(projeto_model)
            self.db_session.flush()
            infos_projeto = {
                "nome": projeto_model.nome,
                "id_projeto": projeto_model.id_projeto
            }
            return infos_projeto
        except Exception:
            raise HTTPException(
                detail="Erro ao criar um novo projeto",
                status_code=status.HTTP_400_BAD_REQUEST
            )
        
    def relacionar_projeto_participante(self, id_projeto: int, id_participante: int):
        projeto_participante_model = ProjetoParticipanteModel(
            id_projeto=id_projeto,
            id_participante=id_participante
        )

        try:
            self.db_session.add(projeto_participante_model)
            self.db_session.flush()
        except Exception:
            raise HTTPException(
                detail="Erro ao relacionar projeto-participante",
                status_code=status.HTTP_400_BAD_REQUEST
            )

