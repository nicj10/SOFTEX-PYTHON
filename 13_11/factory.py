from abc import ABC, abstractmethod

class Midia(ABC):
    @abstractmethod
    def ler_midia(self):
        pass


class Ebook(Midia):
    def __init__(self, tipo: str, nome: str):
        self.tipo = tipo
        self.nome = nome

    def ler_midia(self) -> None:
        print(f"Lendo o livro: {self.nome}")


class Audio(Midia):
    def __init__(self, tipo: str, nome: str):
        self.tipo = tipo
        self.nome = nome

    def ler_midia(self) -> None:
        print(f"Ouvindo a música: {self.nome}")



musica01 = Audio("MP3", "Beyond the Sea")
musica01.ler_midia()

class fabric_midia(ABC):

    @abstractmethod
    def fabric_method(self, midia:midia):
        midia.ler_midia()

class fabric_ebook(fabric_midia):
    def fabric_method(self, ebook):
        return ebook("mp4", "florentina")

fabric_ebook()