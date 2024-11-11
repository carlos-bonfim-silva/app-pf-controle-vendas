from fastapi import APIRouter, HTTPException
from src.models.estoqueModel import EstoqueModel
from src.services.estoqueService import EstoqueService
from src.models.respostasModel import Resposta

app_router = APIRouter(prefix="/estoque")

@app_router.get("/listar", status_code=200)
async def ListarEstoque():
    resposta = await EstoqueService.ListarTodos()
    return Resposta(resposta)

@app_router.post("/adicionar", status_code=200)
async def AdicionarEstoque(estoqueModel: EstoqueModel):
    resposta = await EstoqueService.AdicionarEstoque(estoqueModel)
    return Resposta(resposta)

@app_router.get("/{id}", status_code=200)
async def Estoque(id):
    resposta = await EstoqueService.BuscarEstoque(id, 0)
    return Resposta(resposta)

@app_router.post("/Atualizar", status_code=200)
async def AtualizarEstoque(produto_id: str, quantidade: int):
    resposta = await EstoqueService.Vendas(produto_id, quantidade)
    return Resposta(resposta)

@app_router.post("/vender", status_code=200)
async def Vendas (produto_id: str, quantidade: int):
    resposta = await EstoqueService.Vendas(produto_id, quantidade)
    return Resposta(resposta)
