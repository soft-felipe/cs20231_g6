from pydantic import BaseModel
from typing import Dict, List


class Task(BaseModel):
    id: str
    content: str


class Tasks(BaseModel):
    __root__: Dict[str, Task]


class Column(BaseModel):
    id: str
    title: str
    taskIds: List[str]


class Columns(BaseModel):
    __root__: Dict[str, Column]


class Board(BaseModel):
    tasks: Tasks
    columns: Columns
    columnOrder: List[str]


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
