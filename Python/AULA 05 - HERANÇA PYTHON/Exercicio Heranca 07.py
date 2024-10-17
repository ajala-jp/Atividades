class Brinquedos:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.prco = preco

    def brincar(self):
        print(f"Estou brincando com o {self.nome}")

    
class Pou(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, fome = False, sujo = False):
        super().__init__(nome, cor, tamanho, preco)
        self.fome = fome
        self.sujo = sujo

    def banho(self):
        if self.sujo == True:
            print(f"O Pou {self.nome} está sujo, deve tomar um banho de água benta!")
        
        else:
            print("O Pou está limpo!")

    def comer(self):
        if self.fome == True:
            print("O Pou está com fome! Dê a ele algo para comer")

        else:
            print("Ja comeu!")

class Maxsteel(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, modo_turbo = bool):
        super().__init__(nome, cor, tamanho, preco)
        self.turbo = modo_turbo

    def ativar(self):
        if self.turbo == True:
            print("MODO TURBO ATIVADO!")

        else:
            print("MAXSTEEL ESTÁ BROXADO!!!")

        

class Miranha(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, teia = bool, sensor = bool):
        super().__init__(nome, cor, tamanho, preco)
        self.teia = teia
        self.sensor= sensor

    def atirar(self):
        if self.teia == True:
            print("Teia disparada!")
        else:
            print("Teia falhou!")

    def sentidoaranha(self):
        if self.sensor == True:
            print("DESVIOU DO ATAQUE!!!!")

        else:
            print("HOMEM ARANHA FOI ATINGIDO POR UMA BALA!!!!!!!!!!")
    
class KungFuPanda(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, pastel = bool):
        super().__init__(nome, cor, tamanho, preco)
        self.pastel = pastel

    def comendo(self):
        if self.pastel == True:
            print("O Poo parou para comer no meio da batalha!!")
        
        else:
            print("Ele está faminto, e perdeu suas forças!")


class MCGolfinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, cantar):
        super().__init__(nome, cor, tamanho, preco)
        self.cantar = cantar
    
    def cantando(self):
        print(f"Aqui vai uma letra da música que andei compondo...")
        print({self.cantar})


