from bson import json_util  # Importa o módulo json_util do BSON para manipulação de objetos BSON em JSON
import json  # Importa o módulo json para manipulação de dados em formato JSON

# Função que converte um objeto BSON em um dicionário JSON
def Resposta(item) -> dict:
    # Converte o item BSON para JSON utilizando json_util.dumps
    doc = json_util.dumps(item)
    
    # Converte o JSON gerado para um dicionário e retorna
    return json.loads(doc)
