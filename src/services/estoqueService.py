from src.database.connection import Estoque
from src.models.estoqueModel import EstoqueModel
from fastapi import HTTPException
from datetime import datetime
from src.models.respostasModel import Resposta

class EstoqueService:
    async def ListarTodos() -> list:
        try:
            return list(Estoque.find())
        except Exception as error:
            raise HTTPException(400, detail=error)
    
    async def CriarDados(estoqueModel: EstoqueModel):
        try:
            estoque = Estoque.count_documents()
            id = 0
            if estoque > 1: 
                id = estoque + 1

            novo = {
                "id": id,
                "nome": estoqueModel.nome,
                "sobrenome": estoqueModel.sobrenome,
                "email": estoqueModel.email,
                "telefone": estoqueModel.telefone,
                "datacricao": datetime.now()
            }
            Estoque.insert_one(novo)
        except Exception as error:
            raise HTTPException(400, detail=error)
            
    async def BuscarEstoqueId(id):
        try:
            resultado = Estoque.find_one({"id": id}) 
            resposta = Resposta(resultado)

            if resposta == None:
                erro = {
                "code": "404",
                "description" : "Não Encontrado!", 
                "parameter_name": f'{id}'
                }
                return  erro
            
            return resposta
        except Exception as error:
            raise HTTPException(400, detail=error)
        




# nome = "Carlos"
# idade = "29"
# email = "carlos@gmail.com"
# telefone = "999999999"