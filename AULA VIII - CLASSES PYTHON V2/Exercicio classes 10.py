class NF():
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produto, icms, frete, ipi, valor_total = 0):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razaosocial = razao_social
        self.data = data
        self.valorproduto = valor_produto
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valortotal = valor_total

    def obter_numero(self):
        print(self.numero)

    def obter_dataEmissao(self):
        print(self.data)

    def alterarRazaoSocial(self):
        self.razao = input("Informe a razão social")

    def calcularValorTotal(self):
        imposto = ((self.valorproduto * 7) / 100) + ((self.valorproduto * 12)/100)
        self.valortotal = self.valorproduto + imposto + self.frete
        print(self.valortotal)