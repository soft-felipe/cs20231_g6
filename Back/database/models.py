from sqlalchemy import Column, String, Integer, JSON
from database.base import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(128))
    board_data = Column(JSON, default='{"tasks": {}, "columns": {}, "columnOrder": []}')
