num_avaliacoes = int(input("Digite o número de avaliações: "))
soma = 0
i = 0

while   i < num_avaliacoes:
    soma += float(input("Informe sua nota: "))
    i += 1
media = soma / num_avaliacoes
print(media)