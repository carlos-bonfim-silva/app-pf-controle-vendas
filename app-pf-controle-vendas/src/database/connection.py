import pymongo

url_database = "mongodb+srv://carlosbonfim:xaY26bTNUk1HddGf@devops.vcnyn.mongodb.net/"
banco = pymongo.MongoClient(url_database)
db = banco['Grupo_4']

Estoque = db.Estoque
