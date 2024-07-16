class Aluno:
    def __init__(self, nome, RA, *notas):
        self.nome = nome
        self.ra = RA
        self.notas = notas
    
    def Mostrar_situacao(self):
        total = sum(self.notas)/len(self.notas)
        if total >= 5 and total <= 6.9:
            print("Exame")
        
        elif total < 5:
            print("Reprovado")
        
        else:
            print("Aprovado")


aluno1 = Aluno("Joao", 226455878, 0,5,10,4)

aluno1.Mostrar_situacao()