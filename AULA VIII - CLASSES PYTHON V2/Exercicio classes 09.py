class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo, nivel = 5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel
        self.car = False
        self.distancia = 0

    
    def ligar(self):
        self.car= True
        print("VRUMMMMM")

    def abastecer(self, quantidade):
        self.nivel += quantidade
        print(f"Combustivel colocado: {quantidade}, valor total {self.nivel}")

    def andar(self,distancia=0):
        if  self.car == True:
            print(f"Km andados: {distancia}")
            self.distancia = distancia
        
        elif self.car == False:
            print(f"Carro desligado")

    def verificar_nivel(self):
        consumoKM = self.distancia / self.consumo
        print(f"Consumo por km: {consumoKM}")
    
    def calcular_imposto(self):
        valorIPVA = (self.valor * 2.5) / 100
        print(f"Valor do IPVA: {valorIPVA}")


carro1 = Carro("Volkswaven","Gol","Preto",2014,90000,12,100)
carro1.ligar()
carro1.abastecer(40)
carro1.andar(10)
carro1.verificar_nivel()
carro1.calcular_imposto()


