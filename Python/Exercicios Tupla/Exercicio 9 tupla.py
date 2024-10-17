matriz = [[1,2,11,13],[4,15,16,60],[7,8,19,200],[20,100,5,3]]
soma = 0

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > 10:
            soma +=1
        
print(soma)

