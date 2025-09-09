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