from fastapi import FastAPI
from routes import usuario_router, test_router

app = FastAPI()

@app.get("/")
def home():
    return "Salve"

app.include_router(router=usuario_router)
app.include_router(router=test_router)
    
