# Documentação

## FastAPI:

https://realpython.com/fastapi-python-web-apis/

### Estrutura dos Projetos

```bash
projects = [
    {'name': 'Project 1', 'creator': {'User':{'name':'John', 'nickname':'Jo'}},'step':'1', 'tasks':[1,2,3,4,5], 'team':[{'User':{'name':'Doe', 'nickname':'Do'}},{'User':{'name':'John', 'nickname':'Jo'}}]},
    {'name': 'Project 1', 'creator': {'User':{'name':'Doe', 'nickname':'Do'}},'step':'1', 'tasks':[6,7], 'team': [{'User':{'name':'John', 'nickname':'Jo'}},{'User':{'name':'Doe', 'nickname':'Do'}}]}
]

```
### Rodando local
- Para rodar a API local será necessário o Python na versão >= 3.10.x
- Com o Python instalado, devemos instalar também o PIP para instalação de dependências do Python.
- Com ambos instalados, iremos instalar o Poetry: ```pip install poetry```
- Criar novo ambiente virtual: ```poetry env use python```
- Entrar no ambiente virtual: ```poetry shell```
- Instalar todas as dependências necessárias para o projeto: ```poetry install```
- Rodar a API localmente: ```uvicorn main:app --reload```
