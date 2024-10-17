tupla = (0,2,4,6,8,10,12,11,13,15,14,16,17,18,19,20)
cont = 0
soma = 0
for i in tupla:
    if tupla[cont] % 2 == 0:
        soma += tupla[cont]
        cont += 1
    else:
        cont += 1
    
print(soma)
