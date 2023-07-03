from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from depends import get_db_session, token_verifier
from services.usuario_service import UsuarioLoginService
from schemas import Usuario, UsuarioLogin, Projeto, Etapa, Tarefa, Comentario


db_session: Session = Depends(get_db_session)

usuario_router = APIRouter(prefix='/usuario')
test_router = APIRouter(prefix='/teste', dependencies=[Depends(token_verifier)])

@usuario_router.post('/registrar')
def registrar_usuario(usuario: UsuarioLogin, db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    uc.registrar_usuario_login(usuario=usuario)
    return JSONResponse(
        content={'msg':"Usuario registrado com sucesso."},
        status_code=status.HTTP_201_CREATED
    )
    
@usuario_router.get('/listar')
def listar_usuarios(db_session: Session = Depends(get_db_session)):
    uc = UsuarioLoginService(db_session=db_session)
    usuarios = uc.listar_usuarios_login()
    user_dict = []
    for u in usuarios:
        user_dict.append(u.to_dict())
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
    
@test_router.get('/check')
def teste_login():
    return "Logado"


@projeto_router.get('/listar')
def listar_projetos(db_session: Session = Depends(get_db_session)):
    # Lógica para listar os projetos
    return JSONResponse(
        content={'msg': "Lista de projetos"},
        status_code=status.HTTP_200_OK
    )

@projeto_router.get('/{projeto_id}/etapas')
def listar_etapas(projeto_id: int, db_session: Session = Depends(get_db_session)):
    # Lógica para listar as etapas de um projeto específico
    return JSONResponse(
        content={'msg': f"Etapas do projeto {projeto_id}"},
        status_code=status.HTTP_200_OK
    )

@etapa_router.get('/{etapa_id}/tarefas')
def listar_tarefas(etapa_id: int, db_session: Session = Depends(get_db_session)):
    # Lógica para listar as tarefas de uma etapa específica
    return JSONResponse(
        content={'msg': f"Tarefas da etapa {etapa_id}"},
        status_code=status.HTTP_200_OK
    )

@tarefa_router.get('/{tarefa_id}/comentarios')
def listar_comentarios(tarefa_id: int, db_session: Session = Depends(get_db_session)):
    # Lógica para listar os comentários de uma tarefa específica
    return JSONResponse(
        content={'msg': f"Comentários da tarefa {tarefa_id}"},
        status_code=status.HTTP_200_OK
    )

@comentario_router.post('/{tarefa_id}/comentar')
def adicionar_comentario(tarefa_id: int, comentario: Comentario, db_session: Session = Depends(get_db_session)):
    # Lógica para adicionar um comentário a uma tarefa específica
    return JSONResponse(
        content={'msg': f"Comentário adicionado à tarefa {tarefa_id}"},
        status_code=status.HTTP_201_CREATED
    )