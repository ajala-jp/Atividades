class Funcionario():
    def __init__(self,nome, matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def bater_ponto(self):
        pontos = []
        ponto = int(input("Você bateu o ponto hoje?: "))
        if ponto != 0 or ponto != 1:
            print("Valor inserido inválido")
        else:
            pontos.append(ponto)


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao, meta_vendas):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
        self.metavendas = meta_vendas
    
    def getinfo(self):
        print(f"Você está atualmente ganhando {self.salario} com {self.comissao}% de comissao por venda!")

    def meta(self):
        print(f"Você deve vender por dia {self.metavendas} produtos!")

    def vendas(self,valor):
        if valor >= 50:
            print("Você bateu a meta diária!")
        
        else:
            print(f"Você ainda precisa vender {self.metavendas - valor} produtos para conseguir bater a meta diária!")


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha, metadiaria):
        super().__init__(nome, matricula, salario)
        self.__senha = senha
        self.metadiaria = metadiaria

    def getsenha(self):
        print(f'ATEÇÃO!!! CUIDADO COM OS DADOS PEDIDOS!')
        print(self.__senha)

    def vendadiaria(self, vendas):
        if vendas == self.metadiaria or vendas > self.metadiaria:
            print("Meta diária batida!!")
        else:
            print(f"Você ainda precisa vender {self.metadiaria - vendas} em produtos para bater a meta diária da loja!")


vendedor = Vendedor("João", 1524, 1200, 5, 50)
vendedor.getinfo()
vendedor.meta()
vendedor.vendas(42)

gerente = Gerente("Joao", 1222, 5000,1521,1000)
gerente.getsenha()
gerente.vendadiaria(580)