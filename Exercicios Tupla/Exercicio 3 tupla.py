tupla = (0,4,5,6,2,1,4,7,8,5,9,6,3,2,1,12,16,14,81,52,41,12)
cont = 0
print("Os números pares na tupla são: ")
for i in tupla:
    if tupla[cont] % 2 == 0:
        print(tupla[cont])
        cont += 1
    else:
        cont += 1