# 1 e 2
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos")

nicholas = Pessoa("Nicholas", 19)
heloisa = Pessoa("Heloisa", 22)

nicholas.apresentar()


