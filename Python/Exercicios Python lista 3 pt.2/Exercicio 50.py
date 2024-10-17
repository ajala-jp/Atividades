n = 6
i = 2
j = 3
cont = 0
listasnumeros = []

while len(listasnumeros) < n:
    if cont % i == 0 or cont % j == 0:
        listasnumeros.append(cont)
    cont +=1

print(listasnumeros)