from pydantic import BaseModel, Field, field_validator
from email_validator import validate_email, EmailNotValidError
  
class EstoqueModel(BaseModel):
    nome: str = Field(..., description="nome não pode ser nulo")
    sobrenome: str = Field(..., description="")
    email: str = Field(..., description="")
    telefone: str = Field(..., description="")
    preco: float = Field(..., description="")

    @field_validator('preco')
    def preco_nao_ser_null(cls, value):
        if value <= 0:
            raise ValueError('preço tem, que ser positivo.')
        return value
    
    @field_validator('nome', 'sobrenome', 'email', 'telefone')
    def must_not_be_empty(cls, value):
        if not value or value.strip() == "":
            raise ValueError('campo não pode ser nulo')
        return value
    
    @field_validator('email')
    def validar_email(cls, value):
        try:
            validate_email(value)
        except EmailNotValidError as error:
            raise EmailNotValidError(error)