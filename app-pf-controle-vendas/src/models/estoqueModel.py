from pydantic import BaseModel, Field  # Importa as classes BaseModel e Field do Pydantic para definir e validar os dados
from datetime import datetime  # Importa a classe datetime para manipular e formatar datas e horas

# Definindo o modelo de dados do estoque
class EstoqueModel(BaseModel):
    # Campo para o ID do produto, obrigatório e com uma descrição
    produto_id: str = Field(..., description="ID do produto")
    
    # Campo para o nome do produto, obrigatório e com uma descrição
    nome_produto: str = Field(..., description="Nome do produto")
    
    # Campo para a quantidade de itens em estoque, obrigatório, deve ser maior que 0 e com uma descrição
    quantidade: int = Field(..., gt=0, description="Quantidade disponível")
    
    # Campo para o preço unitário do produto, obrigatório, deve ser maior que 0 e com uma descrição
    preco_unitario: float = Field(..., gt=0, description="Preço unitário do produto")
    
    # Campo para a data de criação do estoque, utiliza o valor atual por padrão
    data_criacao: datetime = Field(default_factory=datetime.now)

    # Configuração extra para o modelo, adicionando um exemplo para o esquema de dados
    class Config:
        schema_extra = {
            "example": {
                "produto_id": "produto123",  # Exemplo de ID de produto
                "nome_produto": "Notebook",  # Exemplo de nome de produto
                "quantidade": 10,  # Exemplo de quantidade de produtos no estoque
                "preco_unitario": 2500.0  # Exemplo de preço unitário do produto
            }
        }
