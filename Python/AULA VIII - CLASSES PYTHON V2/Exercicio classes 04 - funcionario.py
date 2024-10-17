class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horastrabalhadas = horas_trabalhadas
        self.valorhora = valor_hora

    
    def nomeCompleto(self):
        print(f"{self.nome} {self.sobrenome}")

    def calcularSalario(self):
        total = self.horastrabalhadas * self.valorhora
        print(f"O salário será: {total}")

    def incrementarHoras(self,hora):
        self.horastrabalhadas += hora


p1 = Funcionario("João Pedro","Gonçalves Ajala", 170, 20)

p1.nomeCompleto()
p1.incrementarHoras(10)
p1.calcularSalario()