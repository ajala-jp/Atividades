class Compra():
    def __init__(self, numero, produto, valor, valor_total = 0):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valortotal = valor_total

    def calcular_valor_total(self,icms =17,frete = 5):
        self.valortotal = (self.valor + (self.valor * icms) / 100) + ((self.valor*frete) / 100)
        print(self.valortotal)
        valortotal = self.valortotal

class Avista(Compra):
    def __init__(self, numero, produto, valor,desconto, valor_total=0 ):
        super().__init__(numero, produto, valor, valor_total)
        
        self.desconto = desconto

    def valoravista(self):
        self.valortotal = self.valortotal - (self.valor * self.desconto)/ 100
        

    def getvalor(self):
        print(f"O valor a vista com um desconto de {self.desconto}% ficou: {self.valortotal}")

class Parcelado(Compra):
    def __init__(self, numero, produto, valor, numero_parcelas, valor_total=0):
        super().__init__(numero, produto, valor, valor_total)
        self.parcelas = numero_parcelas

    def valorparcelas(self):
        self.valortotal = self.valortotal / self.parcelas

    def getparcelas(self):
        print(f"O valor das parcelas ficou {self.valortotal} de {self.parcelas}")

compra1 = Avista(141,"seila", 1200, 6)
compra1.calcular_valor_total()
compra1.valoravista()
compra1.getvalor()


compra2 = Parcelado(141,"seila", 1200, 6)
compra2.calcular_valor_total()
compra2.valorparcelas()
compra2.getparcelas()