numerospares = []
listas = []
cont = 0
soma = 0
contadorpares = 0
while True:
    num = int(input("Informe um número: "))
    if num > 0:
        cont += 1
        listas.append(num)
        if num % 2 == 0:
            numerospares.append(num)
            contadorpares += 1

    if num == 0:
        break
media =sum(listas)/cont
print(f"A soma dos números digitados foi: {sum(listas)} ")
print(f"A quantidade de números digitados foi : {cont}")
print(f"A média dos númers digitados foi: {media} ")
print(f"O maior número digitado foi: {max(listas)}") 
print(f"O menor número digitado foi: {min(listas)}") 
print(f"A média dos números pares foi: {sum(numerospares)/ contadorpares}")