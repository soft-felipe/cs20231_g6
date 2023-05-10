
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

projects = [
    {'name': 'Project 1', 'creator': {'User':{'name':'John', 'nickname':'Jo'}},'step':'1', 'tasks':[1,2,3,4,5], 'team':[{'User':{'name':'Doe', 'nickname':'Do'}},{'User':{'name':'John', 'nickname':'Jo'}}]},
    {'name': 'Project 1', 'creator': {'User':{'name':'Doe', 'nickname':'Do'}},'step':'1', 'tasks':[6,7], 'team': [{'User':{'name':'John', 'nickname':'Jo'}},{'User':{'name':'Doe', 'nickname':'Do'}}]}
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/projects/")
async def create_project():
    return {'projects':projects}

