class Pessoa:
    def __init__(self,nome, ano_nasc,):
        self.nome = nome
        self.idade = 2024 - ano_nasc

    def mostrarIdade(self):
        return self.idade
    
    def mostrarQualidade(self,quali):
        return f"{self.nome} é muito {quali}"
    


p1 = Pessoa("João",2005)

print(p1.mostrarQualidade("Legal"))