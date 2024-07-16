num_avaliacoes = int(input("Digite o número de avaliações: "))
soma = 0

for i in range(num_avaliacoes):
    nota = float(input("Informe a nota:"))
    soma += nota
    
media = soma/num_avaliacoes
print(media)

