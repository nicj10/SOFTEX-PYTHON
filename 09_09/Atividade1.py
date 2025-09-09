# 3 e 4
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def __str__(self):
        return f"CARRO: {self.modelo}\nMARCA: {self.marca}\nANO: {self.ano}\n================="


hb20 = Carro("Hyundai", "HB20", 2025)
siena = Carro("Fiat", "Siena", 2008)
jeep = Carro("Jeep", "Renegade", 2020)

print(hb20)
hb20.ano = 2015
print(hb20)

print(siena)
print(jeep)