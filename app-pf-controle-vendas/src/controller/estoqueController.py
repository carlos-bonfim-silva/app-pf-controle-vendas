from fastapi import APIRouter
from src.models.estoqueModel import EstoqueModel 
from src.services.estoqueService import EstoqueService
from src.models.respostasModel import Resposta

app_router = APIRouter(prefix="/estoque")

@app_router.get("/list", status_code=200)
async def ListarTodos():
    resposta = await EstoqueService.ListarTodos()
    return Resposta(resposta)

@app_router.post('/criar', status_code=200)   
async def CriarDados(estoqueModel: EstoqueModel):
    await EstoqueService.CriarDados(estoqueModel)