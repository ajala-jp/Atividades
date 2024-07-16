a = [[1,13,3],[4,45,67],[7,80,9]]

b = [[100,8,7],[6,5,4],[3,25,10]]

c = [[0,0,0],[0,0,0],[0,0,0]]

cont = 0

soma = 0
for linha in range(len(a)):
    soma = 0
    for coluna in range(len(a)):
        c[linha][coluna] += a[linha][coluna] + b[linha][coluna]
         

for i in range(len(c)):
    print(c[i]) 

