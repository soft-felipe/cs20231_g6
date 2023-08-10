import traceback
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from model.schemas import  Projeto
from database.models import ComentarioModel, EtapaModel, ProjetoModel, ProjetoParticipanteModel, TarefaModel, ViewInfosParticipantesProjetoModel
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
        
    def criar_relacionar_novo_projeto(self, id_usuario: int, projeto: Projeto):
        try:
            projeto_criado = self.criar_projeto(projeto=projeto, id_usario=id_usuario)
            self.relacionar_projeto_participante(id_projeto=projeto_criado['id_projeto'], id_participante=id_usuario)
            self.db_session.commit()

            return JSONResponse(
                content={
                    'msg': f"Projeto '{projeto_criado['nome']}' criado com sucesso para o usuário {id_usuario}",
                    'id_projeto': projeto_criado['id_projeto']
                },
                status_code=status.HTTP_201_CREATED
            ), None
        
        except Exception as e:
            traceback.print_exc()
            self.db_session.rollback()
            return None,JSONResponse(
                content={
                    'msg': 'Erro ao criar projeto e relacionar projeto-participante'
                },
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def listar_projetos(self):
        # Buscar os projetos do usuário no banco de dados
        projetos = self.db_session.query(ProjetoModel).all()

        projetos_dict = []
        for projeto in projetos:
            projeto_dict = {
                "id": projeto.id_projeto,
                "nome": projeto.nome,
                "descricao": projeto.descricao,
                "etapas": []
            }

            # Buscar as etapas do projeto
            etapas = self.db_session.query(EtapaModel).filter_by(id_projeto = projeto.id_projeto).all()

            for etapa in etapas:
                etapa_dict = {
                    "id": etapa.id_etapa,
                    "titulo": etapa.nome,
                    "tarefas": []
                }

                # Buscar as tarefas da etapa
                tarefas = self.db_session.query(TarefaModel).filter_by(id_etapa = etapa.id_etapa).all()

                for tarefa in tarefas:
                    tarefa_dict = {
                        "id": tarefa.id_tarefa,
                        "descricao": tarefa.descricao,
                        "comentarios": []
                    }

                    # Buscar os comentários da tarefa
                    comentarios = self.db_session.query(ComentarioModel).filter_by(id_tarefa=tarefa.id_tarefa).all()

                    for comentario in comentarios:
                        comentario_dict = {
                            "id": comentario.id_comentario,
                            "descricao": comentario.descricao
                        }
                        tarefa_dict["comentarios"].append(comentario_dict)

                    etapa_dict["tarefas"].append(tarefa_dict)

                projeto_dict["etapas"].append(etapa_dict)

            projetos_dict.append(projeto_dict)
            
        return projetos_dict
    
    def listar_projetos_usuario(self, id_usuario:int):
        infos_projetos = []
        projetos_participantes = self.db_session.query(ViewInfosParticipantesProjetoModel).filter_by(id_participante=id_usuario).all()
        
        for projeto_criado in projetos_participantes:
            info = {
                'id_projeto': projeto_criado.id_projeto,
                'nome_projeto': projeto_criado.nome_projeto,
                'email': projeto_criado.email
            }
            infos_projetos.append(info)

        return infos_projetos
    
    def listar_projetos_criados_usuario(self, id_usuario:int):
        infos_projetos = []
        projetos_criados = self.db_session.query(ProjetoModel).filter_by(id_criador=id_usuario).all()
        
        for projeto_criado in projetos_criados:
            info = {
                'id_projeto': projeto_criado.id_projeto,
                'nome': projeto_criado.nome,
                'descricao': projeto_criado.descricao
            }
            infos_projetos.append(info)

        return infos_projetos

    def editar_nome(self, id_projeto, novoValorCampo):
        projeto = self.db_session.query(ProjetoModel).filter_by(id_projeto=id_projeto).first()
        projeto.nome = novoValorCampo
        self.db_session.commit()
        self.db_session.refresh(projeto)

    def editar_descricao(self, id_projeto, novoValorCampo):
        projeto = self.db_session.query(ProjetoModel).filter_by(id_projeto=id_projeto).first()
        projeto.descricao = novoValorCampo
        self.db_session.commit()
        self.db_session.refresh(projeto)

    def deletar_projeto(self, id_projeto):
        projeto = self.db_session.query(ProjetoModel).filter_by(id_projeto=id_projeto).first()
        # todo: precisa antes deletar os participantes da tabela projeto_participantes
        self.db_session.delete(projeto)
        self.db_session.commit()


