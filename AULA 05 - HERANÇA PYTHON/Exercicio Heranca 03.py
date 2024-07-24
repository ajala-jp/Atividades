class Ingresso():
    def __init__(self, preco, setor):
        self.__preco = preco 
        self.setor = setor

    def alterar_preco(self):
        novopreco = float(input("Informe um novo preço: "))
        self.__preco = novopreco
        print("Preço alterado")
    
    def mostrar_preco(self):
        print(self.__preco)
    
class IngressoVIP(Ingresso):
    def __init__(self, preco, setor, camarote = True, open_bar = False, open_food = False, estacionamento = True):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.openbar = open_bar
        self.openfood = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.openbar == True:
            print("Bebida servida, boa festa!")
        else:
            print("Infelizmente o seu VIP não contém open bar.")
    def acessar_camarote(self):
        if self.camarote == True:
            print("Acesso ao camarote permitida, por favor suba as escadas!")
        
        else:
            print("Infelizmente seu Ingresso VIP não contém camarote!")

pessoa1 = IngressoVIP(120,2,False,False,True,False)

pessoa1.pegar_bebida()
pessoa1.acessar_camarote()