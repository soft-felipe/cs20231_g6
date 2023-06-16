import bcrypt
from jwt import PyJWTError
from jose import jwt

from sqlalchemy.orm import Session

from schemas import Board, User, UserIn_Pydantic, User_Pydantic
from database.models import UserModel


class UsuarioLoginService:
    def __init__(self, db_session: Session = None):
        self.db_session = db_session

    def save_board(self, board: Board, user: User_Pydantic):
        user_db = self.db_session.query(UserModel).filter_by(id=user.id).first()
        user_db.board_data = board.json()
        self.db_session.commit()

    def create_user(self, user: UserIn_Pydantic):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user_data = user.dict()
        user_data['password_hash'] = hashed_password.decode('utf-8')
        user_db = UserModel(**user_data)
        self.db_session.add(user_db)
        self.db_session.commit()

        token = jwt.encode({"id": user_db.id}, "myjwtsecret")
        return {'access_token': token, 'token_type': 'bearer'}

    def generate_token(self, form_data):
        username = form_data.username
        password = form_data.password

        user_db = self.db_session.query(UserModel).filter_by(username=username).first()
        if not user_db or not bcrypt.checkpw(password.encode('utf-8'), user_db.password_hash.encode('utf-8')):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid username or password'
            )

        token = jwt.encode({"id": user_db.id}, "myjwtsecret")
        return {'access_token': token, 'token_type': 'bearer'}

    def verify_token(self, access_token):
        try:
            payload = jwt.decode(access_token, "myjwtsecret")
            user = self.db_session.query(UserModel).filter_by(id=payload.get('id')).first()
            return User_Pydantic.from_orm(user)
        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Invalid token'
            )
