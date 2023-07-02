from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from depends import get_db_session, token_verifier
from services.usuario_service import UsuarioLoginService
from schemas import Usuario, UsuarioLogin

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