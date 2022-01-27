class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(selfself, valor):
        self.saldo -= valor

        #Testando

conta1 = Conta('Geek', 150.00, 1500)

print(f'O titular da conta é: {conta1.titular}')
print(f'{conta1.titular}, O seu Saldo é de: {conta1.saldo}')
print(f'{conta1.titular}, O seu Limite é de: {conta1.limite}')


