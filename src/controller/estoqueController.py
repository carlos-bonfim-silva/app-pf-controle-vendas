# src/controller/estoqueController.py
from fastapi import APIRouter, HTTPException
from src.models.estoqueModel import EstoqueModel
from src.services.estoqueService import EstoqueService
from src.models.respostasModel import Resposta

app_router = APIRouter(prefix="/estoque")

@app_router.get("/listar", status_code=200)
async def ListarEstoque():
    resposta = await EstoqueService.ListarTodos()
    return Resposta(resposta)

@app_router.post("/adicionar", status_code=201)
async def AdicionarEstoque(estoqueModel: EstoqueModel):
    resposta = await EstoqueService.AdicionarEstoque(estoqueModel)
    return Resposta(resposta)

# Alterei esta rota para aceitar um ID e chamei o método correto no serviço
@app_router.get("/id/{id}", status_code=200)
async def ListarEstoquePorId(id: str):
    resposta = await EstoqueService.ListarPorId(id)
    return Resposta(resposta)
