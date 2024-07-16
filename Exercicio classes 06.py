class Agenda:
    def __init__(self, dia, mes, ano, *anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        if self.dia > 31 or self.dia < 1:
            print(f"O dia {self.dia} é inválido")
        
        elif self.mes > 12 or self.mes < 1:
            print(f"O mes {self.mes} é inválido")

        else:
            print(f"{self.dia}/{self.mes}/{self.ano}")

    def anotar_tarefa(self,outraanotacao):
        lista = []
        lista.append(self.anotacao)
        lista.append(outraanotacao)
        self.anotacao = lista
        

    def Mostrar_anotacao(self):
        print(self.anotacao)
        

p1 = Agenda(7,6,2005,"Hoje é o meu aniversário")



p1.anotar_tarefa("Hoje vou viajar")
p1.anotar_tarefa("Viajei")

p1.Mostrar_anotacao()