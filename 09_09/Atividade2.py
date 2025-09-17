# 5
'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        if(valor <= self.saldo):
            self.saldo -= valor
            return self.saldo
        else:
            return f"Não foi possível realizar o saque"
        
conta = ContaBancaria("Nicholas", 500)
conta.sacar(5500)
'''
# 6
'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False


# Testando
conta = ContaBancaria("Nicholas", 500)

if conta.sacar(200):
    print("Saque realizado com sucesso!")
    print(f"Saldo atual: R${conta.saldo}")
else:
    print("Não foi possível realizar o saque. Saldo insuficiente.")

if conta.sacar(5500):
    print("Saque realizado com sucesso!")
    print(f"Saldo atual: R${conta.saldo}")
else:
    print("Não foi possível realizar o saque. Saldo insuficiente.")
'''

# 7 e 8
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"


# Testando os objetos
aluno1 = Aluno("Nicholas", 9.5)
aluno2 = Aluno("João", 8.0)
aluno3 = Aluno("Ana", 7.2)

print(aluno1)
print(aluno2)
print(aluno3)
