from fastapi import FastAPI, APIRouter  # Importa FastAPI para criar a aplicação e APIRouter para definir rotas
from src.controller.estoqueController import app_router  # Importa o router do estoque, que contém as rotas relacionadas ao estoque

app = FastAPI()  # Cria uma instância da aplicação FastAPI

# Incluindo o router do estoque na aplicação, permitindo que as rotas do estoque sejam acessíveis
app.include_router(app_router)
