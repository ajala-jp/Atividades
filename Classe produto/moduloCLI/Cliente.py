class Cliente:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome

    def getNomecli(self):
        print(f"CLIENTE {self.nome}")

    def getIdade(self):
        print(f"IDADE CLIENTE: {self.idade}")