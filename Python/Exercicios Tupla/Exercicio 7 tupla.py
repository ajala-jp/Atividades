matrix = [[1,2,3],[4,5,6],[7,8,9]]
soma = 0


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        
        soma += matrix[i][j]

print('Resultado =',soma)
    
    