import traceback

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database.depends import get_db_session, token_verifier

from services.projeto_service import ProjetoService
from services.usuario_service import UsuarioLoginService
from model.schemas import Usuario, UsuarioLogin, Projeto, Etapa, Tarefa, Comentario, UsuarioAlterarSenha
from database.models import UsuarioModel, ProjetoModel, ViewInfosParticipantesProjetoModel

db_session: Session = Depends(get_db_session)

usuario_router = APIRouter(prefix='/usuario')
test_router = APIRouter(prefix='/teste', dependencies=[Depends(token_verifier)])
projeto_router = APIRouter(prefix='/projeto')


# -------- ROTAS PARA USUÁRIO -------- #

@usuario_router.post('/cadastrar-login', summary="Cadastro de credenciais: login, senha, email")
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


@usuario_router.post('/{id_login}/cadastrar-usuario', summary="Cadastro de informaçoes do usuario: nome, apelido, data nascimento")
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


@usuario_router.get('/listar', summary="Listar todos os usuários cadastrados no banco")
def listar_usuarios(db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    user_dict = uc.listar_usuarios_login()

    return JSONResponse(
        content=user_dict,
        status_code=status.HTTP_200_OK
    )


@usuario_router.post('/login')
def login_usuario(request_form_usuario: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_session)):
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


@usuario_router.post('/{id_usuario}/alterar-senha', summary="Alterar senha validando: senha atual, username e login")
def alterar_senha_usuario(id_usuario: int, usuario_alterar_senha: UsuarioAlterarSenha, db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    usuario_atualizado = uc.valida_senha_email(id_usuario=id_usuario, usuario_alterar_senha=usuario_alterar_senha)

    return JSONResponse(
        content=f'Senha do usuario {usuario_atualizado.username} foi atualizada!',
        status_code=status.HTTP_200_OK
    )


@test_router.get('/check')
def teste_login():
    return "Logado"


# -------- ROTAS PARA PROJETO -------- #

# Pra listarmos os projetos, precisamos de um usuário logado
@projeto_router.get('/desenvolver')
def listar_projetos(db_session: Session = Depends(get_db_session), usuario: Usuario = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    projetos_dict = ps.listar_projetos(usuario=usuario)

    return JSONResponse(
        content=projetos_dict,
        status_code=status.HTTP_200_OK
    )

@projeto_router.get('/{id_usuario}/listar', summary="Listar projetos que o usuário participa")
def listar_projetos(id_usuario: int, db_session: Session = Depends(get_db_session)):
    us = UsuarioLoginService(db_session=db_session)
    usuario_existe, resposta = us.verifica_existencia_usuario(id_usuario=id_usuario)
    if not usuario_existe:
        return resposta

    ps=ProjetoService(db_session=db_session)
    infos_projetos = ps.listar_projetos_usuario(id_usuario=id_usuario)

    return JSONResponse(
        content=infos_projetos,
        status_code=status.HTTP_200_OK
    )


@projeto_router.get('/{id_usuario}/listar-criados', summary="Listar os projetos que o usuário criou")
def listar_projetos_criados(id_usuario: int, db_session: Session = Depends(get_db_session)):
    us = UsuarioLoginService(db_session=db_session)
    usuario_existe, resposta = us.verifica_existencia_usuario(id_usuario=id_usuario)
    if not usuario_existe:
        return resposta

    ps = ProjetoService(db_session=db_session)
    infos_projetos = ps.listar_projetos_criados_usuario(id_usuario=id_usuario)

    return JSONResponse(
        content=infos_projetos,
        status_code=status.HTTP_200_OK
    )

@projeto_router.post('/{id_usuario}/criar', summary="Criar um projeto para um usuário passando seu ID")
def criar_projeto(id_usuario: int, projeto: Projeto, db_session: Session = Depends(get_db_session)):
    us = UsuarioLoginService(db_session=db_session)
    usuario_existe, resposta = us.verifica_existencia_usuario(id_usuario=id_usuario)
    
    if not usuario_existe:
        return resposta

    ps = ProjetoService(db_session=db_session)
    sucesso, falha = ps.criar_relacionar_novo_projeto(id_usuario=id_usuario, projeto=projeto)

    if sucesso is None:
        return falha
    
    else:
        return sucesso
    
@projeto_router.put('/{projeto_id}', summary="(IMPLEMENTAR) EDITAR PROJETO")
def editar_projeto(projeto_id: int, db_session: Session = Depends(get_db_session), usuario: Usuario = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)

@projeto_router.delete('/{projeto_id}', summary="(IMPLEMENTAR) EXCLUIR PROJETO")
def excluir_projeto(projeto_id: int, db_session: Session = Depends(get_db_session), usuario: Usuario = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)



# ETAPAS

# Endpoint para pegar no front-end os dados das etapas de um projeto específico para fornecer aos cards de projetos na página inicial
@projeto_router.get('/{projeto_id}/etapas')
def listar_etapas(projeto_id: int, db_session: Session = Depends(get_db_session), usuario: Usuario = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    etapas_dict, repostaJSON = ps.listar_etapas(projeto_id=projeto_id, usuario=usuario)

    if etapas_dict is None:
        return repostaJSON

    else: 
        return JSONResponse(
            content=etapas_dict,
            status_code=status.HTTP_200_OK
        )
    
@projeto_router.post('/{projeto_id}/etapas', summary="(IMPLEMENTAR) ADICIONAR NOVA ETAPA")
def adicionar_etapas(projeto_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)

@projeto_router.put('/{projeto_id}/etapas/{etapa_id}', summary="(IMPLEMENTAR) EDITAR ETAPA EXISTENTE")
def editar_etapa(projeto_id: int, etapa_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)

@projeto_router.delete('/{projeto_id}/etapas/{etapa_id}', summary="(IMPLEMENTAR) EXCLUIR ETAPA EXISTENTE")
def excluir_etapa(projeto_id: int, etapa_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)


# TAREFAS

# Endpoint para pegar no front-end os dados das tarefas de um projeto específico para fornecer aos cards de projetos na página inicial
@projeto_router.get('/{projeto_id}/etapas/{etapa_id}/tarefas')
def listar_tarefas(projeto_id: int, etapa_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    tarefas_dict, respostaJSON = ps.listar_tarefas(projeto_id=projeto_id, etapa_id=etapa_id)

    if tarefas_dict is None:
        return respostaJSON

    else:
        return JSONResponse(
            content=tarefas_dict,
            status_code=status.HTTP_200_OK
        )

@projeto_router.post('/{projeto_id}/etapas/{etapa_id}/tarefas', summary="(IMPLEMENTAR) ADICIONAR NOVA TAREFA")
def adicinar_tarefa(projeto_id: int, etapa_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)

@projeto_router.put('/{projeto_id}/etapas/{etapa_id}/tarefas/{tarefa_id}', summary="(IMPLEMENTAR) EDITAR TAREFA EXISTENTE")
def editar_etapa(projeto_id: int, etapa_id: int, tarefa_id:int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)

@projeto_router.delete('/{projeto_id}/etapas/{id_etapa}', summary="(IMPLEMENTAR) EXCLUIR TAREFA EXISTENTE")
def excluir_etapa(projeto_id: int, etapa_id: int, tarefa_id:int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)

# COMENTÁRIOS

# Endpoint para pegar no front-end os dados dos comentários de um projeto específico para fornecer aos cards de projetos na página inicial
@projeto_router.get('/{projeto_id}/etapas/{etapa_id}/tarefas/{tarefa_id}/comentarios')
def listar_comentarios(projeto_id: int, etapa_id: int, tarefa_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    comentarios_dict, respostaJSON = ps.listar_comentarios(projeto_id=projeto_id, etapa_id=etapa_id, tarefa_id=tarefa_id)

    if comentarios_dict is None:
        return respostaJSON

    else:
        return JSONResponse(
            content=comentarios_dict,
            status_code=status.HTTP_200_OK
        )


# Endpoint para postar um comentário em uma tarefa específica
@projeto_router.post('/{tarefa_id}/comentar')
def adicionar_comentario(tarefa_id: int, comentario: Comentario, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    sucesso, falha = ps.adicionar_comentario
    
    if sucesso is None:
        return falha
    
    else:
        return sucesso


# Endpoint para editar um comentário em uma tarefa específica
@projeto_router.put('/{tarefa_id}/comentarios/{comentario_id}')
def modificar_comentario(tarefa_id: int, comentario_id: int, comentario: Comentario, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    sucesso, falha = ps.editar_comentario(tarefa_id=tarefa_id, comentario_id=comentario_id, comentario=comentario)

    if sucesso is None:
        return falha
    
    else:
        return sucesso


# Endpoint para excluir um comentário em uma tarefa específica
@projeto_router.delete('/{tarefa_id}/comentarios/{comentario_id}')
def remover_comentario(tarefa_id: int, comentario_id: int, db_session: Session = Depends(get_db_session)):
    ps = ProjetoService(db_session=db_session)
    sucesso, falha = ps.excluir_comentario(tarefa_id=tarefa_id, comentario_id=comentario_id)

    if sucesso is None:
        return falha
    
    else:
        return sucesso
