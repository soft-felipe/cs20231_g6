from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import PyJWTError
from sqlalchemy.orm import Session
from jose import jwt

from depends import get_db_session, token_verifier
from schemas import Board, UserIn_Pydantic, User_Pydantic
from services.usuario_service import UsuarioLoginService

usuario_router = APIRouter(prefix='/usuario')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@usuario_router.get("/board")
def get_board(user: User_Pydantic = Depends(token_verifier)):
    return {'board': user.board_data}


@usuario_router.post("/board")
def save_board(board: Board, user: User_Pydantic = Depends(token_verifier)):
    uc = UsuarioLoginService(db_session=user.db_session)
    uc.save_board(board=board, user=user)
    return {"status": "success"}


@usuario_router.post('/users')
def create_user(user: UserIn_Pydantic):
    uc = UsuarioLoginService()
    return uc.create_user(user=user)


@usuario_router.post('/token')
def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    uc = UsuarioLoginService()
    return uc.generate_token(form_data=form_data)
