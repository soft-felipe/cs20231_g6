from fastapi import FastAPI
from routes import router

app = FastAPI()

@app.get("/")
def home():
    return "Salve"

app.include_router(router=router)
    
