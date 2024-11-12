from fastapi import FastAPI, APIRouter
from src.controller.estoqueController import app_router

app = FastAPI()

# Incluindo o router do estoque
app.include_router(app_router)