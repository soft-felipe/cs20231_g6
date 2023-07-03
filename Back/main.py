from fastapi import FastAPI
from routes import usuario_router, projeto_router, etapa_router, tarefa_router, comentario_router

def include_router(app):
	app.include_router(general_pages_router)

@app.get("/")
def home():
    return "Salve"

app.include_router(router=usuario_router)
app.include_router(router=projeto_router)
app.include_router(router=etapa_router)
app.include_router(router=tarefa_router)
app.include_router(router=comentario_router)    
