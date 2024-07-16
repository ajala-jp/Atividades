tupla = (3,12,2,9,1,7,5)
cont = -1
cont1 = 0
maior = 0

for i in range(len(tupla)):
    if tupla[cont] > tupla[cont1]:
        maior = tupla[cont]
        cont1 +=1
    elif tupla[cont1] > tupla[cont]:
        maior = tupla[cont1]
        cont -= 1

print(maior)

        
    