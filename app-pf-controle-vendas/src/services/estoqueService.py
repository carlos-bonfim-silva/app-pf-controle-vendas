from src.database.connection import Estoque
from src.models.estoqueModel import EstoqueModel
from fastapi import HTTPException

class EstoqueService:
    async def ListarTodos():
        try:
            return list(Estoque.find())
        except Exception as error:
            raise HTTPException(400, detail=str(error))

    async def AdicionarEstoque(estoqueModel: EstoqueModel):
        try:
            produto_existente = Estoque.find_one({"produto_id": estoqueModel.produto_id})

            if produto_existente:
                raise HTTPException(status_code=400, detail="Produto já cadastrado no estoque.")

            novo_produto = {
                "produto_id": estoqueModel.produto_id,
                "nome_produto": estoqueModel.nome_produto,
                "quantidade": estoqueModel.quantidade,
                "preco_unitario": estoqueModel.preco_unitario,
                "data_criacao": estoqueModel.data_criacao
            }
            Estoque.insert_one(novo_produto)
            return {"message": "Produto adicionado com sucesso."}

        except Exception as error:
            raise HTTPException(400, detail=str(error))

    async def BuscarEstoque(produto_id: str, quantidade: int):
        try:
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                raise HTTPException(status_code=404, detail="Produto não encontrado.")

            if int(produto['quantidade']) < quantidade:
                raise HTTPException(status_code=400, detail="Estoque insuficiente.")

            return produto
        except Exception as error:
            raise HTTPException(400, detail=str(error))
    
    async def Vendas (produto_id: str, quantidade: int):
        try:
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                raise HTTPException(status_code=404, detail="Produto não encontrado.")
            if produto['quantidade'] < quantidade:
                raise HTTPException(status_code=400, detail="Estoque insuficiente.")
            Estoque.update_one(
                {"produto_id": produto_id},
                {"$inc": {"quantidade": -quantidade}}
                )
            return {"message": "Venda realizada com sucesso."}
        except Exception as error:
            raise HTTPException(400, detail=str(error))
       