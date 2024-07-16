matriz = [[1,120,-3],[4,5,250],[7,0,9]]
linha = 0
coluna = 0

linha1 = 0
coluna1 = 0

maior = matriz[0][0]
menor = matriz[0][0]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j

for o in range(len(matriz)):
    for p in range(len(matriz)):
        if matriz[o][p] < menor:
            menor = matriz[o][p]
            linha1 = o
            coluna1 = p        
print(f"O maior número da matriz é: {maior} e se encontra na linha {linha} e na coluna {coluna}")

print(f'Ja o menor número é {menor} e se encontra na linha {linha1} e na coluna {coluna1}')