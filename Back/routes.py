from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from depends import get_db_session
from auth_user import UsuarioUseCase
from schemas import Usuario
import json

db_session: Session = Depends(get_db_session)

router = APIRouter(prefix='/usuario')

@router.post('/registrar')
def registrar_usuario(usuario: Usuario, db_session: Session = Depends(get_db_session)):
    uc = UsuarioUseCase(db_session=db_session)
    uc.registrar_usuario(usuario=usuario)
    return JSONResponse(
        content={'msg':"Success"},
        status_code=status.HTTP_201_CREATED
    )
    
@router.get('/get')
def listar_usuarios(db_session: Session = Depends(get_db_session)):
    uc = UsuarioUseCase(db_session=db_session)
    usuarios = uc.listar_usuarios()
    user_dict = []
    for u in usuarios:
        user_dict.append(u.to_dict())
    return JSONResponse(
        content=user_dict,
        status_code=status.HTTP_200_OK
    )
