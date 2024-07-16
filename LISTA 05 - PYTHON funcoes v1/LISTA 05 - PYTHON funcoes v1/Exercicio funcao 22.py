def criaMatrizUser(linhaa):
    matrix = []

    for i in range(4):
        linha = []
        for j in range(4):
            numero = int(input("Informe um número: "))
            linha.append(numero)
        
        matrix.append(linha)
    
    soma = sum(matrix[linhaa])
    return soma

x = criaMatrizUser(2)
print(x)

