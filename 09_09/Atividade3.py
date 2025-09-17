class Cachorro:
    especie = "Canis familiaris"

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


dog1 = Cachorro("Rex", 5)
dog2 = Cachorro("Luna", 3)

print(f"{dog1.nome} tem {dog1.idade} anos")
print(f"{dog2.nome} tem {dog2.idade} anos")

print("Espécie (pela classe):", Cachorro.especie)
print("Espécie (pelo objeto dog1):", dog1.especie)
print("Espécie (pelo objeto dog2):", dog2.especie)
