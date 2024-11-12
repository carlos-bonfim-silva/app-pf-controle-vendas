from src.database.connection import Estoque  # Importa o modelo de conexão com a base de dados (Estoque)
from src.models.estoqueModel import EstoqueModel  # Importa o modelo EstoqueModel para validação dos dados
from fastapi import HTTPException  # Importa HTTPException do FastAPI para gerar exceções personalizadas

# Classe que gerencia os serviços relacionados ao estoque
class EstoqueService:

    # Método estático para listar todos os produtos no estoque
    @staticmethod
    async def listar_todos():
        try:
            # Busca todos os itens no estoque e retorna como uma lista
            return list(Estoque.find())
        except Exception as error:
            # Em caso de erro, gera uma exceção HTTP com status 400 e mensagem do erro
            raise HTTPException(status_code=400, detail=str(error))

    # Método estático para adicionar um novo produto ao estoque
    @staticmethod
    async def adicionar_estoque(estoqueModel: EstoqueModel):
        try:
            # Verifica se o produto já existe no estoque com base no produto_id
            produto_existente = Estoque.find_one({"produto_id": estoqueModel.produto_id})
            if produto_existente:
                # Se o produto já existir, lança uma exceção de conflito (status 400)
                raise HTTPException(status_code=400, detail="Produto já cadastrado no estoque.")

            # Converte o modelo EstoqueModel para dicionário e insere no banco de dados
            novo_produto = estoqueModel.dict()
            Estoque.insert_one(novo_produto)
            return {"message": "Produto adicionado com sucesso."}
        except Exception as error:
            # Em caso de erro, gera uma exceção HTTP com status 400 e mensagem do erro
            raise HTTPException(status_code=400, detail=str(error))

    # Método estático para buscar um produto específico no estoque pelo produto_id
    @staticmethod
    async def buscar_estoque(produto_id: str):
        try:
            # Busca o produto no banco de dados com base no produto_id
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                # Se o produto não for encontrado, lança uma exceção de não encontrado (status 404)
                raise HTTPException(status_code=404, detail="Produto não encontrado.")
            return produto
        except Exception as error:
            # Em caso de erro, gera uma exceção HTTP com status 400 e mensagem do erro
            raise HTTPException(status_code=400, detail=str(error))

    # Método estático para atualizar a quantidade de um produto no estoque
    @staticmethod
    async def atualizar_estoque(produto_id: str, quantidade: int):
        try:
            # Busca o produto no banco de dados com base no produto_id
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                # Se o produto não for encontrado, lança uma exceção de não encontrado (status 404)
                raise HTTPException(status_code=404, detail="Produto não encontrado.")
            # Atualiza a quantidade do produto no banco de dados
            Estoque.update_one({"produto_id": produto_id}, {"$set": {"quantidade": quantidade}})
            return {"message": "Estoque atualizado com sucesso."}
        except Exception as error:
            # Em caso de erro, gera uma exceção HTTP com status 400 e mensagem do erro
            raise HTTPException(status_code=400, detail=str(error))

    # Método estático para realizar a venda de um produto e atualizar o estoque
    @staticmethod
    async def realizar_venda(produto_id: str, quantidade: int):
        try:
            # Busca o produto no banco de dados com base no produto_id
            produto = Estoque.find_one({"produto_id": produto_id})
            if not produto:
                # Se o produto não for encontrado, lança uma exceção de não encontrado (status 404)
                raise HTTPException(status_code=404, detail="Produto não encontrado.")
            # Verifica se há quantidade suficiente no estoque
            if produto['quantidade'] < quantidade:
                # Se o estoque for insuficiente, lança uma exceção de erro (status 400)
                raise HTTPException(status_code=400, detail="Estoque insuficiente.")
            # Atualiza a quantidade no estoque, diminuindo a quantidade vendida
            Estoque.update_one(
                {"produto_id": produto_id},
                {"$inc": {"quantidade": -quantidade}}  # Decrementa a quantidade
            )
            return {"message": "Venda realizada com sucesso."}
        except Exception as error:
            # Em caso de erro, gera uma exceção HTTP com status 400 e mensagem do erro
            raise HTTPException(status_code=400, detail=str(error))
