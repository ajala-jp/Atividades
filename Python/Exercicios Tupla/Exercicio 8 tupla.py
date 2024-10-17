M = [[1,2,3],[4,5,6],[7,8,9]]
N =[[0,0,0],[0,0,0],[0,0,0]]
cont = 0

for linha in range(len(M)):
    for coluna in range(len(M)):
        N[linha][coluna] = M[coluna][linha]



print(N)