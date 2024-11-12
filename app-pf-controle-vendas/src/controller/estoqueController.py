from fastapi import APIRouter, HTTPException
from src.models.estoqueModel import EstoqueModel
from src.services.estoqueService import EstoqueService
from src.models.respostasModel import Resposta

app_router = APIRouter(prefix="/estoque")

# Listar todo o estoque
@app_router.get("/listar", status_code=200)
async def listar_estoque():
    resposta = await EstoqueService.listar_todos()
    return Resposta(resposta)

# Adicionar produto ao estoque
@app_router.post("/adicionar", status_code=201)
async def adicionar_estoque(estoqueModel: EstoqueModel):
    resposta = await EstoqueService.adicionar_estoque(estoqueModel)
    return Resposta(resposta)

# Buscar produto por ID
@app_router.get("/{id}", status_code=200)
async def buscar_estoque(id: str):
    resposta = await EstoqueService.buscar_estoque(id)
    return Resposta(resposta)

# Atualizar a quantidade de um produto no estoque
@app_router.put("/atualizar", status_code=200)
async def atualizar_estoque(produto_id: str, quantidade: int):
    resposta = await EstoqueService.atualizar_estoque(produto_id, quantidade)
    return Resposta(resposta)

# Vender um produto
@app_router.post("/vender", status_code=200)
async def vender_produto(produto_id: str, quantidade: int):
    resposta = await EstoqueService.realizar_venda(produto_id, quantidade)
    return Resposta(resposta)
