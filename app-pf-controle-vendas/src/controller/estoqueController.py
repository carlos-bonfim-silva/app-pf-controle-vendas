# Importações necessárias para as rotas da API
from fastapi import APIRouter, HTTPException  # APIRouter é utilizado para criar rotas dentro de um módulo de API. HTTPException lida com erros HTTP.
from src.models.estoqueModel import EstoqueModel  # Importa o modelo de dados EstoqueModel, que define a estrutura de um produto no estoque.
from src.services.estoqueService import EstoqueService  # Importa o serviço EstoqueService, que contém a lógica de manipulação do estoque.
from src.models.respostasModel import Resposta  # Importa o modelo de resposta, provavelmente usado para padronizar as respostas da API.

# Cria um roteador de API com o prefixo "/estoque", que será adicionado a todas as rotas definidas aqui.
app_router = APIRouter(prefix="/estoque")

# Rota para listar todo o estoque
@app_router.get("/listar", status_code=200)
async def listar_estoque():
    # Chama o serviço que lista todos os produtos do estoque e retorna uma resposta padronizada
    resposta = await EstoqueService.listar_todos()
    return Resposta(resposta)

# Rota para adicionar um novo produto ao estoque
@app_router.post("/adicionar", status_code=201)
async def adicionar_estoque(estoqueModel: EstoqueModel):
    # Recebe um EstoqueModel como corpo da requisição e o passa ao serviço para adicionar ao estoque
    resposta = await EstoqueService.adicionar_estoque(estoqueModel)
    return Resposta(resposta)

# Rota para buscar um produto por ID
@app_router.get("/{id}", status_code=200)
async def buscar_estoque(id: str):
    # Busca um produto no estoque pelo seu ID, utilizando o serviço correspondente
    resposta = await EstoqueService.buscar_estoque(id)
    return Resposta(resposta)

# Rota para atualizar a quantidade de um produto no estoque
@app_router.put("/atualizar", status_code=200)
async def atualizar_estoque(produto_id: str, quantidade: int):
    # Recebe o ID do produto e a nova quantidade, e chama o serviço para atualizar essa informação
    resposta = await EstoqueService.atualizar_estoque(produto_id, quantidade)
    return Resposta(resposta)

# Rota para realizar a venda de um produto, subtraindo a quantidade do estoque
@app_router.post("/vender", status_code=200)
async def vender_produto(produto_id: str, quantidade: int):
    # Chama o serviço que realiza a venda, subtraindo a quantidade especificada do produto no estoque
    resposta = await EstoqueService.realizar_venda(produto_id, quantidade)
    return Resposta(resposta)
