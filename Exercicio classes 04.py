class Conta:
    def __init__(self, Nome, CPF, numero, Saldo):
        self.nome = Nome
        self.cpf = CPF
        self.numero = numero
        self.saldo = Saldo

    
    def Depositar(self, quantidade):
        self.saldo += quantidade

    def Sacar(self, dinheiro):
        if dinheiro <= self.saldo:
            self.saldo -= dinheiro
        
        else:
            print("Saldo insuficiente")

    
    def Imprimir_saldo(self):
        print(f"Saldo atual: {self.saldo}")


pessoa1 = Conta("Joao", 123, 190, 5000)

pessoa1.Depositar(1000)

pessoa1.Imprimir_saldo()

pessoa1.Sacar(6000)

pessoa1.Imprimir_saldo()
        
