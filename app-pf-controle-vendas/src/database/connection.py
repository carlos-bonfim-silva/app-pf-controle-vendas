import pymongo  # Importa a biblioteca pymongo, que é usada para interagir com o banco de dados MongoDB.

# Define a URL de conexão com o banco de dados MongoDB. No caso, está usando o formato MongoDB Atlas (nuvem).
url_database = "mongodb+srv://carlosbonfim:xaY26bTNUk1HddGf@devops.vcnyn.mongodb.net/"

# Cria uma instância do MongoClient utilizando a URL fornecida. Isso estabelece a conexão com o MongoDB.
banco = pymongo.MongoClient(url_database)

# Acessa o banco de dados chamado 'Grupo_4'. Se o banco não existir, ele será criado quando os dados forem inseridos.
db = banco['Grupo_4']

# Acessa ou cria a coleção 'Estoque' dentro do banco de dados 'Grupo_4'. As coleções no MongoDB são como tabelas em bancos de dados relacionais.
Estoque = db.Estoque
