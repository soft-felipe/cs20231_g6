from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database.depends import get_db_session, token_verifier

from services.projeto_service import ProjetoService
from services.usuario_service import UsuarioLoginService
from model.schemas import Usuario, UsuarioLogin, Projeto, Etapa, Tarefa, Comentario
from database.models import UsuarioModel

db_session: Session = Depends(get_db_session)

usuario_router = APIRouter(prefix='/usuario')
test_router = APIRouter(prefix='/teste', dependencies=[Depends(token_verifier)])
projeto_router = APIRouter(prefix='/projeto')

#USUÁRIO

@usuario_router.post('/registrar-login')
def registrar_login(usuario_login: UsuarioLogin, db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    id_usuario_login = uc.registrar_usuario_login(usuario=usuario_login)
    return JSONResponse(
        content={
            'msg': "Usuario registrado com sucesso.",
            'id_login': id_usuario_login
        },
        status_code=status.HTTP_201_CREATED
    )

@usuario_router.post('/{id_login}/registrar-usuario')
def registrar_usuario(id_login: int, usuario: Usuario, db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    id_usuario = uc.registrar_usuario(usuario=usuario, id_credencial=id_login)
    return JSONResponse(
        content={
            'msg': "Informacoes do usuario registrado com sucesso.",
            'id_usuario': id_usuario
        },
        status_code=status.HTTP_200_OK
    )

@usuario_router.get('/listar')
def listar_usuarios(db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    usuarios = uc.listar_usuarios_login()
    user_dict = []
    for u in usuarios:
        infos_json = {
            'id_login': u.id_login,
            'email': u.email
        }
        user_dict.append(infos_json)
    return JSONResponse(
        content=user_dict,
        status_code=status.HTTP_200_OK
    )


@usuario_router.post('/login')
def login_usuario(request_form_usuario: OAuth2PasswordRequestForm = Depends(),
                  db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    usuario = UsuarioLogin(
        username=request_form_usuario.username,
        senha=request_form_usuario.password
    )
    auth_data = uc.login_usuario(usuario=usuario)
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )


@test_router.get('/check')
def teste_login():
    return "Logado"

#PROJETO

# Pra listarmos os projetos, precisamos de um usuário logado
@projeto_router.get('/listar')
def listar_projetos(db_session: Session = Depends(get_db_session), usuario: Usuario = Depends(get_db_session)):
    # Buscar os projetos do usuário no banco de dados
    projetos = db_session.query(Projeto).filter(Projeto.usuario_id == usuario.id).all()

    projetos_dict = []
    for projeto in projetos:
        projeto_dict = {
            "id": projeto.id,
            "nome": projeto.nome,
            "etapas": []
        }

        # Buscar as etapas do projeto
        etapas = db_session.query(Etapa).filter(Etapa.projeto_id == projeto.id).all()

        for etapa in etapas:
            etapa_dict = {
                "id": etapa.id,
                "titulo": etapa.titulo,
                "tarefas": []
            }

            # Buscar as tarefas da etapa
            tarefas = db_session.query(Tarefa).filter(Tarefa.etapa_id == etapa.id).all()

            for tarefa in tarefas:
                tarefa_dict = {
                    "id": tarefa.id,
                    "titulo": tarefa.titulo,
                    "descricao": tarefa.descricao,
                    "pontuacao": tarefa.pontuacao,
                    "prioridade": tarefa.prioridade,
                    "comentarios": []
                }

                # Buscar os comentários da tarefa
                comentarios = db_session.query(Comentario).filter(Comentario.tarefa_id == tarefa.id).all()

                for comentario in comentarios:
                    comentario_dict = {
                        "id": comentario.id,
                        "descricao": comentario.descricao
                    }
                    tarefa_dict["comentarios"].append(comentario_dict)

                etapa_dict["tarefas"].append(tarefa_dict)

            projeto_dict["etapas"].append(etapa_dict)

        projetos_dict.append(projeto_dict)

    return JSONResponse(
        content=projetos_dict,
        status_code=status.HTTP_200_OK
    )


# Criar um projeto específico pra um usuário logado
@projeto_router.post('/{usuario_id}/criar-projeto')
def criar_projeto(usuario_id: int, projeto: Projeto, db_session: Session = Depends(get_db_session)):
    # Lógica para criar um novo projeto para o usuário específico
    usuario = db_session.query(UsuarioModel).filter_by(id_usuario=usuario_id).first()

    if not usuario:
        return JSONResponse(
            content={'error': 'Usuário não encontrado'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    ps = ProjetoService(db_session=db_session)
    projeto_criado = ps.criar_projeto(projeto=projeto, id_usario=usuario_id)

    return JSONResponse(
        content={
            'msg': f"Projeto '{projeto_criado['nome']}' criado com sucesso para o usuário {usuario_id}",
            'id_projeto': projeto_criado['id_projeto']
        },
        status_code=status.HTTP_201_CREATED
    )


#ETAPAS

# Endpoint para pegar no front-end os dados das etapas de um projeto específico para fornecer aos cards de projetos na página inicial
@projeto_router.get('/{projeto_id}/etapas')
def listar_etapas(projeto_id: int, db_session: Session = Depends(get_db_session),
                  usuario: Usuario = Depends(get_db_session)):
    # Lógica para listar as etapas de um projeto específico
    projeto = db_session.query(Projeto).filter(Projeto.id == projeto_id, Projeto.usuario_id == usuario.id).first()

    if not projeto:
        return JSONResponse(
            content={'error': 'Projeto não encontrado ou não pertence ao usuário'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    etapas = db_session.query(Etapa).filter(Etapa.projeto_id == projeto.id).all()

    etapas_dict = []
    for etapa in etapas:
        etapa_dict = {
            'id': etapa.id,
            'titulo': etapa.titulo,
            'index': etapa.index
        }
        etapas_dict.append(etapa_dict)

    return JSONResponse(
        content=etapas_dict,
        status_code=status.HTTP_200_OK
    )


#TAREFAS

# Endpoint para pegar no front-end os dados das tarefas de um projeto específico para fornecer aos cards de projetos na página inicial
@projeto_router.get('/{projeto_id}/etapas/{etapa_id}/tarefas')
def listar_tarefas(projeto_id: int, etapa_id: int, db_session: Session = Depends(get_db_session)):
    # Lógica para listar as tarefas de uma etapa específica de um projeto
    projeto = db_session.query(Projeto).filter(Projeto.id == projeto_id).first()

    if not projeto:
        return JSONResponse(
            content={'error': 'Projeto não encontrado'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    etapa = db_session.query(Etapa).filter(Etapa.id == etapa_id, Etapa.projeto_id == projeto_id).first()

    if not etapa:
        return JSONResponse(
            content={'error': 'Etapa não encontrada'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    tarefas = db_session.query(Tarefa).filter(Tarefa.etapa_id == etapa_id).all()

    tarefas_dict = []
    for tarefa in tarefas:
        tarefa_dict = {
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'criacao': tarefa.criacao.isoformat(),
            'limite': tarefa.limite.isoformat(),
            'pontuacao': tarefa.pontuacao,
            'prioridade': tarefa.prioridade
        }
        tarefas_dict.append(tarefa_dict)

    return JSONResponse(
        content=tarefas_dict,
        status_code=status.HTTP_200_OK
    )


#COMENTÁRIOS

# Endpoint para pegar no front-end os dados dos comentários de um projeto específico para fornecer aos cards de projetos na página inicial
@projeto_router.get('/{projeto_id}/etapas/{etapa_id}/tarefas/{tarefa_id}/comentarios')
def listar_comentarios(projeto_id: int, etapa_id: int, tarefa_id: int, db_session: Session = Depends(get_db_session)):
    # Lógica para listar os comentários de uma tarefa específica
    projeto = db_session.query(Projeto).filter(Projeto.id == projeto_id).first()

    if not projeto:
        return JSONResponse(
            content={'error': 'Projeto não encontrado'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    etapa = db_session.query(Etapa).filter(Etapa.id == etapa_id, Etapa.projeto_id == projeto_id).first()

    if not etapa:
        return JSONResponse(
            content={'error': 'Etapa não encontrada'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    tarefa = db_session.query(Tarefa).filter(Tarefa.id == tarefa_id, Tarefa.etapa_id == etapa_id).first()

    if not tarefa:
        return JSONResponse(
            content={'error': 'Tarefa não encontrada'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    comentarios = db_session.query(Comentario).filter(Comentario.tarefa_id == tarefa_id).all()

    comentarios_dict = []
    for comentario in comentarios:
        comentario_dict = {
            'id': comentario.id,
            'descricao': comentario.descricao
        }
        comentarios_dict.append(comentario_dict)

    return JSONResponse(
        content=comentarios_dict,
        status_code=status.HTTP_200_OK
    )


# Endpoint para postar um comentário em uma tarefa específica
@projeto_router.post('/{tarefa_id}/comentar')
def adicionar_comentario(tarefa_id: int, comentario: Comentario, db_session: Session = Depends(get_db_session)):
    # Lógica para adicionar um comentário a uma tarefa específica
    tarefa = db_session.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    if not tarefa:
        return JSONResponse(
            content={'error': 'Tarefa não encontrada'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    novo_comentario = Comentario(
        descricao=comentario.descricao,
        tarefa_id=tarefa_id
    )

    db_session.add(novo_comentario)
    db_session.commit()

    return JSONResponse(
        content={'msg': f"Comentário adicionado à tarefa {tarefa_id}"},
        status_code=status.HTTP_201_CREATED
    )


# Endpoint para editar um comentário em uma tarefa específica
@projeto_router.put('/{tarefa_id}/comentarios/{comentario_id}')
def modificar_comentario(tarefa_id: int, comentario_id: int, comentario: Comentario,
                         db_session: Session = Depends(get_db_session)):
    # Lógica para modificar um comentário em uma tarefa específica
    tarefa = db_session.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    if not tarefa:
        return JSONResponse(
            content={'error': 'Tarefa não encontrada'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    comentario_modificado = db_session.query(Comentario).filter(Comentario.id == comentario_id,
                                                                Comentario.tarefa_id == tarefa_id).first()

    if not comentario_modificado:
        return JSONResponse(
            content={'error': 'Comentário não encontrado'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    comentario_modificado.descricao = comentario.descricao
    db_session.commit()

    return JSONResponse(
        content={'msg': f"Comentário {comentario_id} modificado na tarefa {tarefa_id}"},
        status_code=status.HTTP_200_OK
    )


# Endpoint para excluir um comentário em uma tarefa específica
@projeto_router.delete('/{tarefa_id}/comentarios/{comentario_id}')
def remover_comentario(tarefa_id: int, comentario_id: int, db_session: Session = Depends(get_db_session)):
    # Lógica para remover um comentário de uma tarefa específica
    tarefa = db_session.query(Tarefa).filter(Tarefa.id == tarefa_id).first()

    if not tarefa:
        return JSONResponse(
            content={'error': 'Tarefa não encontrada'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    comentario_removido = db_session.query(Comentario).filter(Comentario.id == comentario_id,
                                                              Comentario.tarefa_id == tarefa_id).first()

    if not comentario_removido:
        return JSONResponse(
            content={'error': 'Comentário não encontrado'},
            status_code=status.HTTP_404_NOT_FOUND
        )

    db_session.delete(comentario_removido)
    db_session.commit()

    return JSONResponse(
        content={'msg': f"Comentário {comentario_id} removido da tarefa {tarefa_id}"},
        status_code=status.HTTP_200_OK
    )
