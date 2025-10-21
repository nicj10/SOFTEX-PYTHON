class Mamifero:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico de mamífero"

class Cachorro(Mamifero):
    def emitir_som(self):
        return "Latido"