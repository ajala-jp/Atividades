class Pessoa():
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargahoraria = carga_horaria
        self.__salario = salario

    def getsalario(self):
        print(f"O salario do professor {self.nome} é {self.__salario}")
    
    def getdisciplina(self):
        print(f"O Professor {self.nome} da aula de {self.disciplina}")

    def getcarga(self):
        print(f"A carga horária do professor {self.nome} é de {self.cargahoraria} horas por dia")
    
    def getformacao(self):
        print(f"O Professor {self.nome} é formado em {self.formacao}")

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, *notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas

    def calcularmedia(self):
        media = sum(self.notas)/ len(self.notas)
        print(media)
    
    def estudar(self):
        print(f"{self.nome} você está atrasado na matéria, é melhor começar a estudar!")

    

aluno1 = Aluno(1524262,"João,", 19, 5,5,4,9)
aluno1.estudar()

professor1 = Professor(15215, "Zoio de zoio", 85, "Garçom","Educação Física", 6, 1000)
professor1.getsalario()
professor1.getdisciplina()
professor1.getcarga()
professor1.getformacao()