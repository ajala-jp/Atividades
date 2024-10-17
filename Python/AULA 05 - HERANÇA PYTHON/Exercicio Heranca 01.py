class Filme:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def play(self):
        print(f"O filme {self.nome} começou! E ele tem {self.duracao} de duração!")

    

class Acao(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def sobreacao(self):
        print(f"O filme {self.nome} é da categoria de ação, onde pode ocorrer várias explosões e efeitos sonoros altos!")


class Comedia(Filme):
    def __init__(self, nome, duracao):
        super().__init__(nome, duracao)

    def sobrecomedia(self):
        print(f"O filme {self.nome} é sobre comédia, onde há várias partes engraçadas para curtir com amigos ou familia. Cuidado para não mijar na poltrona do cinema!")


filme1 = Acao("Vingadores","1:30")
filme1.play()
filme1.sobreacao()

