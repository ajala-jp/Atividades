class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self):
        novopreco = float(input("Informe um  novo preço: "))
        self.preco = novopreco
        
    def escolher_assento(self):
        novoassento = int(input("Informe qual assento gostaria de estar: "))
        self.assento = novoassento

    
class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaoembarque, checkin):
        super().__init__(preco, assento)
        self.portaoembarque = portaoembarque
        self.checkin = checkin
    
    def decolar(self):
        print(f"O vôo do portão {self.portaoembarque} está para decolar!")

    def vip(self):
        if self.preco >= 1200:
            print("Você está em um assento Vip!")
        else:
            print("Você está em um assento de pobre :(")


class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def viajar(self):
        print(f"O ônibus com a placa {self.placa} está para começar a viagem!")

    def abastecer(self):
        print("Estaremos dando uma pausa de 30 minutos no próximo posto para abastecer e descansar da viagem!")


pessoa1 = PassagemAviao(1200,50,20,"Permitido")
pessoa1.vip()
pessoa1.decolar()


pessoa2 = PassagemBus(350,10,152452,"seila")
pessoa2.viajar()
pessoa2.abastecer()