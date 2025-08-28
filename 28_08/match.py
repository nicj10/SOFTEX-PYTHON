'''
nome = input("Digite seu nome: ")
num = input("Digite um número de 1 a 5: ")

match num:
    case "1":
        print(nome, "vai estudar Python")
    case "2":
        print(nome, "vai estudar JavaScript")
    case "3":
        print(nome, "vai estudar Java")
    case "4":
        print(nome, "vai estudar C#")
    case "5":
        print(nome, "vai estudar Assembly")
    case _:
        print("Número invalido")
'''

def adiciona_livro():
    global casa
    casa = 3
    print("Livro adicionado")

while True:
    opcao = (input(
        "Escolha uma opção:\n"
        " 1 - Adicionar um livro\n"
        " 2 - Editar a informação de um livro cadastrado\n"
        " 3 - Pesquisar por um livro\n"
        " 4 - Deletar um livro\n"
        " 5 - Abrir um livro\n"
        " 0 - Sair\n"
    ))

    match opcao:
        case "1":
            adiciona_livro()
        case "2":
            print("Livro editado")
        case "3":
            print("Acahdo o livro")
        case "4":
            print("Livro deletado")
        case "5":
            print("Livro abrido")
        case "0":
            break
        case _:
            print("Número inválido")