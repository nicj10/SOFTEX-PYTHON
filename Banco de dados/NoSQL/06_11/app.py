from database.connection import get_database

db = get_database()

# Criar ou acessar coleções
usuarios = db["usuarios"]
produtos = db["produtos"]

# Inserir documento (exemplo)
usuario = {
    "nome": "Maria",
    "email": "maria@example.com",
    "idade": 25
}
usuarios.insert_one(usuario)

# Buscar dados
for user in usuarios.find():
    print(user)

print("Conexão e inserção realizadas com sucesso!")
