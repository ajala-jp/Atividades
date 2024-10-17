class MeuCachorro:
    def __init__(self, nome, cor, ano_adocao, raça, qualidade, tamanho):
        self.nome = nome
        self.cor = cor
        self.idade = ano_adocao
        self.raca = raça
        self.quali = qualidade
        self.tamanho = tamanho

    def dormindo(self):
        print(f"{self.nome} está dormindo agora.")
    
    def banho(self):
        print(f"{self.nome} ainda não tomou banho!")

    def passaro(self):
        print(f"{self.nome} MATOU UM PASSÁRINHO!!!!!!")

    def comida(self):
        print(f"{self.nome} quer comer de novo")

    def tempo(self,ano_atual,ano_nascimento):
        tempoidade = (ano_atual - ano_nascimento)-(ano_atual - self.idade)
        passado = ano_atual - self.idade
        print(f"Você tinha {tempoidade} anos quando adotou o {self.nome}, isso ja faz {passado} anos")


dog1 = MeuCachorro("Tufão","Preto",2018,"vira-lata","esfomeado","grande")
dog2 = MeuCachorro("Pretinha","Preto",2017,"vira-lata","medrosa","pequena")
dog3 = MeuCachorro("Belinha","Branco",2017,"alguma raça de burgues","Doida","medio")

dog1.tempo(2024,2005)
dog2.tempo(2024,2005)
dog3.passaro()