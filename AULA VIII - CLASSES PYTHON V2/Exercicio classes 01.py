class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    
    def getNome(self):
        print(f"Nome: {self.nome}")

    def setIdade(self, novaidade):
        self.idade = novaidade
        print(self.idade)
        return self.idade
    
    def getEndereco(self):
        print(f"Endereço: {self.endereco}")


p1 = Pessoa("Joao", 19, "Rua 9 de julho 226")

p1.getNome()
p1.setIdade(25)
p1.getEndereco()