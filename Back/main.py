from fastapi import FastAPI
from controller.routes import usuario_router, projeto_router

app = FastAPI()

@app.get("/")
def home():
    return "Salve"

app.include_router(router=usuario_router)
app.include_router(router=projeto_router) 
