class Pessoa:
    def __init__(self,nome, ano_nasc):
        self.nome = nome
        self.idade = 2024 - ano_nasc

    def mostrarIdade(self):
        return print(self.idade)
    
    def mostrarQualidade(self,quali):
        return print(f"{self.nome} é muito {quali}")
    




