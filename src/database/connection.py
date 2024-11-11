# src/database/connection.py
from pymongo import MongoClient

url_database = "mongodb+srv://carlosbonfim:xaY26bTNUk1HddGf@devops.vcnyn.mongodb.net/"
banco = MongoClient(url_database)
db = banco['Grupo_4']
Estoque = db.Estoque
