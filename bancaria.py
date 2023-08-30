class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'seu saldo: {self.saldo}')
    def depositar(self, dinheiro):
        self.saldo += dinheiro

    def sacar_dinheiro(self, valor):
        if valor > self.saldo:
            print('voce nao pode sacar =)')
        else:
            self.saldo -= valor

    
guilherme = ContaBancaria('guilherme', 0)
guilherme.depositar(50)
guilherme.mostrar_saldo()

guilherme.sacar_dinheiro(200)
guilherme.mostrar_saldo()