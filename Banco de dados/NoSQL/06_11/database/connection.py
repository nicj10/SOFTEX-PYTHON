from pymongo import MongoClient

def get_database():
    # Conexão local (padrão)
    client = MongoClient("mongodb://localhost:27017/")

    # Cria (ou conecta-se) ao banco de dados
    db = client["meu_banco"]

    return db
