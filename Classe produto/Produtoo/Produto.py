class Produto:
    def __init__(self, nome, desc, preco, estoque):
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.estoque = estoque
    
    def getNome(self):
        print(self.nome)

    def getPreco(self):
        print(self.preco)