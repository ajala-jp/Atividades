class Pessoa:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} do endereço {self.endereco}, tem negócios a tratar com você hoje!")

    
class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco,cpf, idade):
        super().__init__(nome, telefone, email, endereco)
        self.__cpf = cpf
        self.idade = idade

    def getidade(self):
        print(f"{self.nome} tem atualmente {self.idade} anos")

    def getcpf(self):
        print(self.__cpf)

    

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj, criacao):
        super().__init__(nome, telefone, email, endereco)
        self.__cnpj = cnpj
        self.criado = criacao
    
    def getcnpj(self):
        print(self.__cnpj)

    def getanos(self):
        print(f"A empresa {self.nome} foi criada em {self.criado}")


pessoafisica = PessoaFisica("Joao", 190, "asdasd@gmail.com", "Rua 9 de juhlo 226", 1951616, 19)

pessoafisica.getidade()
pessoafisica.getcpf()

empresa = PessoaJuridica("AAAAAAAA",1920, "adasdas@gmail.com", "Rua 9 de julho 221",5616516, 1915)
empresa.getanos()
empresa.getcnpj()

empresa.negociar()