# src/models/estoqueModel.py
from pydantic import BaseModel, Field
from datetime import datetime

class EstoqueModel(BaseModel):
    produto_id: str = Field(..., description="ID do produto")
    nome_produto: str = Field(..., description="Nome do produto")
    quantidade: int = Field(..., gt=0, description="Quantidade disponível")
    preco_unitario: float = Field(..., gt=0, description="Preço unitário do produto")
    data_criacao: datetime = Field(default_factory=datetime.now)

    class Config:
        schema_extra = {
            "example": {
                "produto_id": "produto123",
                "nome_produto": "Notebook",
                "quantidade": 10,
                "preco_unitario": 2500.0
            }
        }
