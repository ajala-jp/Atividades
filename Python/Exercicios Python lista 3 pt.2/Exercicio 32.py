lista_num = []
cont = 0

for i in range(5):
    num = int(input("Informe um número: "))
    lista_num.append(num)
print(f"A soma dos números digitados foi: {sum(lista_num)}")

import time
time.sleep(1)

print("Os números digitados foram:")
while cont < len(lista_num):
    time.sleep(0.8)
    print(lista_num[0+cont])
    cont += 1
    if cont == len(lista_num):
        break
