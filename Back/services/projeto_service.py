import traceback
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from model.schemas import Comentario, Projeto, Tarefa, Usuario,  Etapa
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
    
    def listar_tarefas(self, projeto_id: int, etapa_id: int):
        # Lógica para listar as tarefas de uma etapa específica de um projeto
        projeto = self.db_session.query(ProjetoModel).filter_by(id_projeto=projeto_id).first()

        if not projeto:
            return None, JSONResponse(
                content={'error': 'Projeto não encontrado'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        etapa = self.db_session.query(EtapaModel).filter_by(id_etapa = etapa_id).first()

        if not etapa:
            return None, JSONResponse(
                content={'error': 'Etapa não encontrada'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        tarefas = self.db_session.query(TarefaModel).filter_by(id_etapa = etapa_id).all()

        tarefas_dict = []
        for tarefa in tarefas:
            tarefa_dict = {
                'id': tarefa.id_tarefa,
                'descricao': tarefa.descricao,
            }
            tarefas_dict.append(tarefa_dict)
        
        return tarefas_dict, None
    
    def listar_comentarios(self, projeto_id: int, etapa_id: int, tarefa_id: int):
        # Lógica para listar os comentários de uma tarefa específica
        projeto = self.db_session.query(ProjetoModel).filter_by(id_projeto = projeto_id).first()

        if not projeto:
            return None, JSONResponse(
                content={'error': 'Projeto não encontrado'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        etapa = self.db_session.query(EtapaModel).filter_by(id_etapa = etapa_id).first()

        if not etapa:
            return None, JSONResponse(
                content={'error': 'Etapa não encontrada'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        tarefa = self.db_session.query(TarefaModel).filter_by(id_tarefa = tarefa_id).first()

        if not tarefa:
            return None, JSONResponse(
                content={'error': 'Tarefa não encontrada'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        comentarios = self.db_session.query(ComentarioModel).filter_by(id_tarefa = tarefa_id).all()

        comentarios_dict = []
        for comentario in comentarios:
            comentario_dict = {
                'id': comentario.id_comentario,
                'descricao': comentario.descricao
            }
            comentarios_dict.append(comentario_dict)
        
        return comentarios_dict, None
    
    def adicionar_comentario(self, tarefa_id: int, comentario: Comentario):
        # Lógica para adicionar um comentário a uma tarefa específica
        tarefa = self.db_session.query(TarefaModel).filter_by(id_tarefa=tarefa_id).first()

        if not tarefa:
            return None, JSONResponse(
                content={'error': 'Tarefa não encontrada'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        novo_comentario = ComentarioModel(
            id_criador = comentario.id_criador,
            id_tarefa = tarefa_id,
            descricao = comentario.descricao
        )

        self.db_session.add(novo_comentario)
        self.db_session.commit()

        return JSONResponse(
            content={'msg': f"Comentário adicionado à tarefa {tarefa_id}"},
            status_code=status.HTTP_201_CREATED
        ), None
    
    def editar_comentario(self, tarefa_id: int, comentario_id: int, comentario: str):
        # Lógica para modificar um comentário em uma tarefa específica
        tarefa = self.db_session.query(TarefaModel).filter_by(id_tarefa=tarefa_id).first()

        if not tarefa:
            return None, JSONResponse(
                content={'error': 'Tarefa não encontrada'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        comentario_modificado = self.db_session.query(ComentarioModel).filter_by(id_comentario=comentario_id).first()

        if not comentario_modificado:
            return None, JSONResponse(
                content={'error': 'Comentário não encontrado'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        comentario_modificado.descricao = comentario
        self.db_session.commit()

        return JSONResponse(
            content={'msg': f"Comentário {comentario_id} modificado na tarefa {tarefa_id}"},
            status_code=status.HTTP_200_OK
        ), None
    
    def excluir_comentario(self, tarefa_id: int, comentario_id: int):
        # Lógica para remover um comentário de uma tarefa específica
        tarefa = self.db_session.query(TarefaModel).filter_by(id_tarefa=tarefa_id).first()

        if not tarefa:
            return None, JSONResponse(
                content={'error': 'Tarefa não encontrada'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        comentario_removido = self.db_session.query(ComentarioModel).filter_by(id_comentario = comentario_id).first()

        if not comentario_removido:
            return None, JSONResponse(
                content={'error': 'Comentário não encontrado'},
                status_code=status.HTTP_404_NOT_FOUND
            )

        self.db_session.delete(comentario_removido)
        self.db_session.commit()

        return JSONResponse(
            content={'msg': f"Comentário {comentario_id} removido da tarefa {tarefa_id}"},
            status_code=status.HTTP_200_OK
        ), None
    
    
