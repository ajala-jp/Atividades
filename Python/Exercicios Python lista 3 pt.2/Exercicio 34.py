lista_total = []
lista_par = []
lista_impar = []
cont = 0

for i in range(20):
    num = int(input("Informe um número: "))
    lista_total.append(num)
    if num % 2 == 1:
        lista_impar.append(num)
    elif num % 2 == 0:
        lista_par.append(num)

import time
time.sleep(0.6)
print("Os números digitados foram:")

for i in range(len(lista_total)):
    print(lista_total[0+cont])
    cont += 1
cont = 0
print("\n")

time.sleep(0.6)
print("Os números ímpares digitados foram:")
for i in range(len(lista_impar)):
    print(lista_impar[0+cont])
    cont += 1
cont = 0
print("\n")
time.sleep(0.6)
print("Os números pares digitados foram:")
for i in range(len(lista_par)):
    print(lista_par[0+cont])
    cont += 1
cont = 0

