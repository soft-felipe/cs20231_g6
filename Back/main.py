from fastapi import FastAPI
from controller.routes import usuario_router, projeto_router, tarefas_router, comentario_router, etapa_router

app = FastAPI()

@app.get("/")
def home():
    return "Salve"

app.include_router(router=usuario_router)
app.include_router(router=projeto_router) 
app.include_router(router=etapa_router)
app.include_router(router=tarefas_router)
app.include_router(router=comentario_router)