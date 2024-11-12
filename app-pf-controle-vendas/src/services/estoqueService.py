from src.database.connection import Estoque
from src.models.estoqueModel import EstoqueModel
from fastapi import HTTPException

class EstoqueService:

    @staticmethod
    async def listar_todos():
        try:
            return list(Estoque.find())
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    @staticmethod
    async def adicionar_estoque(estoqueModel: EstoqueModel):
        try:
            produto_existente = Estoque.find_one({"produto_id": estoqueModel.produto_id})
            if produto_existente:
                raise HTTPException(status_code=400, detail="Produto já cadastrado no estoque.")

            novo_produto = estoqueModel.dict()
            Estoque.insert_one(novo_produto)
            return {"message": "Produto adicionado com sucesso."}
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    @staticmethod
    async def buscar_estoque(produto_id: str):
        try:
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                raise HTTPException(status_code=404, detail="Produto não encontrado.")
            return produto
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    @staticmethod
    async def atualizar_estoque(produto_id: str, quantidade: int):
        try:
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                raise HTTPException(status_code=404, detail="Produto não encontrado.")
            Estoque.update_one({"produto_id": produto_id}, {"$set": {"quantidade": quantidade}})
            return {"message": "Estoque atualizado com sucesso."}
        except Exception as error:
            raise HTTPException(status_code=400, detail=str(error))

    @staticmethod
    async def realizar_venda(produto_id: str, quantidade: int):
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
            raise HTTPException(status_code=400, detail=str(error))
