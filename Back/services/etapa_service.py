from sqlalchemy.orm import Session
from fastapi import status
from fastapi.responses import JSONResponse
from Back.database.models import ProjetoModel, EtapaModel

class EtapaService:
    def __init__(self, db_session:Session):
        self.db_session = db_session
    
    def listar_etapas(self, projeto_id:int):
        # Lógica para listar as etapas de um projeto específico
        projeto = self.db_session.query(ProjetoModel).filter_by(id_projeto = projeto_id).first()

        if not projeto:
            return None, JSONResponse(
                content={'error': 'Projeto não encontrado'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        etapas = self.db_session.query(EtapaModel).filter_by(id_projeto = projeto_id).all()

        etapas_dict = []
        for etapa in etapas:
            etapa_dict = {
                'id_etapa': etapa.id_etapa,
                'nome': etapa.nome
            }
            etapas_dict.append(etapa_dict)
        
        return etapas_dict