class Aluno_academia:
    def __init__(self, nome, idade, peso, altura, mensalidade = 120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def Obter_mensalidade(self):
        if self.idade >= 18:
            print(self.mensalidade)
        
        elif self.idade < 18:
            self.mensalidade = self.mensalidade - (self.mensalidade*0.20) 
            print(self.mensalidade)

        
    def Calcular_IMC(self):
        res = self.peso / self.altura**2
        print(f"IMC = {res}")


p1 = Aluno_academia("Andreia", 18, 80,1.70)

p1.Obter_mensalidade()