class Cachorro:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def falas(self):
        print(f"{self.nome} disse: To com fome porra")

dog1 = Cachorro("Tufão","Preto","Biggas")
dog2 = Cachorro("Bob","Branco e marrom","Minor")


dog1.falas() 